from flask import Flask, current_app, g
from config_sqlite import current_config, TestingSQLiteConfig
# from config_postgres import current_config, TestingConfig, DevelopmentConfig, ProductionConfig
# from secrets_manager.settings import DB_USER, DB_NAME, DB_HOST, DB_PASSWORD, DEBUG, TESTING
import sqlite3
import psycopg2

# conn = psycopg2.connect(
#     host=DB_HOST,
#     database=DB_NAME,
#     user=DB_USER,
#     password=DB_PASSWORD
# )

# sqlite_conn = sqlite3.connect('sqlite:///sp500_test_db.sqlite', uri=True)

def get_db():
    if 'db' not in g:
        print(f"Current config type: {type(current_config)}")
        print(f"Is instance of TestingSQLiteConfig: {isinstance(current_config, TestingSQLiteConfig)}")
        print(f"Connecting to database at: {current_app.config['DB_URI']}")
        # Check if the current configuration is for testing with SQLite
        if isinstance(current_config, TestingSQLiteConfig):
            print("Connecting to SSSSSSQLite database")
            # Connect to the SQLite database for testing
            g.db = sqlite3.connect(current_config.DB_FILE)
            g.db.row_factory = sqlite3.Row
        else:
            print("Connecting to PostgreSQL database")
            # Connect to the PostgreSQL database
            g.db = psycopg2.connect(
                host=current_config.DB_HOST,
                database=current_config.DB_NAME,
                user=current_config.DB_USER,
                password=current_config.DB_PASSWORD
            )
    return g.db

# def get_db(db_path=None):
#     if current_app:
#         app_context = current_app.app_context()
#     else:
#         app = Flask(__name__)
#         app.config.from_object(current_config)      # config.py: configuration set up in the current_config object
#         app_context = app.app_context()
#         app_context.push()                          # Manually push an application context

#     with app_context:
#         if "db" not in g:
#             if db_path or isinstance(current_config, TestingSQLiteConfig):
#                 # Connect to SQLite database
#                 g.db = sqlite3.connect(db_path or current_config.DB_URI, uri=True)
#             else:
#                 # PostgreSQL connection
#                 g.db = psycopg2.connect(
#                     host=current_config.DB_HOST,
#                     user=current_config.DB_USER,
#                     password=current_config.DB_PASSWORD,
#                     dbname=current_config.DB_NAME)
#         return g.db


# conn = psycopg2.connect(
#     host = Config.DB_HOST, 
#     database = Config.DB_NAME,
#     user = Config.DB_USER, 
#     password = Config.DB_PASSWORD
#     )

# # conn = psycopg2.connect(host = DB_HOST, database = DB_NAME,
# #         user = DB_USER, password = DB_PASSWORD)

# test_conn = psycopg2.connect(
#     host = DB_HOST, 
#     database = DB_NAME,
#     user = DB_USER, 
#     password = DB_PASSWORD
#     )

# test_cursor = test_conn.cursor()

# def get_db():
#     with current_app.app_context():
#         if "db" not in g:
#             g.db = psycopg2.connect(
#                 host=current_config.DB_HOST,
#                 user=current_config.DB_USER,
#                 password=current_config.DB_PASSWORD,
#                 dbname=current_config.DB_NAME)
#         return g.db

# def get_db():
#     if "db" not in g:
#         g.db = psycopg2.connect(
#             host = current_app.config['DB_HOST'],
#             user = current_app.config['DB_USER'],
#             password = current_app.config['DB_PASSWORD'],
#             dbname = current_app.config['DATABASE']
#             )
#     return g.d

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def build_from_record(Class, record):
    if not record: return None
    attr = dict(zip(Class.columns, record))
    obj = Class()
    obj.__dict__ = attr
    return obj

def build_from_records(Class, records):
   return [build_from_record(Class, record) for record in records]

def find_all(Class, cursor):
    sql_str = f"SELECT * FROM {Class.__table__}"
    cursor.execute(sql_str)
    records = cursor.fetchall()
    return [build_from_record(Class, record) for record in records]



# def find(Class, id, cursor):                                          # find() was written for postgres
#     sql_str = f"SELECT * FROM {Class.__table__} WHERE id = %s"        # postgres %s convention for parameterized queries
#     cursor.execute(sql_str, (id,))
#     record = cursor.fetchone()
#     return build_from_record(Class, record)


# updated find() method for SQLite should also work for PostgreSQL. # TODO: test this method with PostgreSQL
def find(Class, id, cursor):
    sql_str = f"SELECT * FROM {Class.__table__} WHERE id = :id"
    cursor.execute(sql_str, {'id': id})
    record = cursor.fetchone()
    return build_from_record(Class, record)

def find_by_symbol(Class, symbol, cursor):
    sql_str = f"SELECT * FROM {Class.__table__} WHERE symbol = :symbol"
    cursor.execute(sql_str, {'symbol': symbol})
    record = cursor.fetchone()
    return build_from_record(Class, record)


# FIXME: toggling save method for SQLite and PostgreSQL. need to migrate to SQLalchemy ORM

###   original save method
# def save(obj, conn, cursor):
#     s_str = ', '.join(len(values(obj)) * ['%s'])
#     obj_str = f"""INSERT INTO {obj.__table__} ({keys(obj)}) VALUES ({s_str});"""
#     cursor.execute(obj_str, list(values(obj)))
#     conn.commit()
#     cursor.execute(f'SELECT * FROM {obj.__table__} ORDER BY id DESC LIMIT 1')
#     record = cursor.fetchone()
#     return build_from_record(type(obj), record)


###  SQLITE SAVE METHOD
def save(obj, conn, cursor):
    s_str = ', '.join(len(values(obj)) * ['?'])  # Changed from '%s' to '?'
    obj_str = f"""INSERT INTO {obj.__table__} ({keys(obj)}) VALUES ({s_str});"""
    cursor.execute(obj_str, list(values(obj)))
    conn.commit()
    last_id = cursor.lastrowid  # Get the last inserted id for SQLite
    cursor.execute(f"SELECT * FROM {obj.__table__} WHERE id = ?", (last_id,))  # Changed from '%s' to '?'
    record = cursor.fetchone()
    return build_from_record(type(obj), record)


# ###  POSTGRES SAVE METHOD
# def save(obj, conn, cursor):
#     # Extracting keys (column names) and values from the object
#     keys = [key for key in obj.columns if hasattr(obj, key)]
#     values = [getattr(obj, key) for key in keys]
    
#     # Correctly handling the column names for SQL
#     column_names = ', '.join(keys)
#     placeholders = ', '.join(['%s'] * len(values))
    
#     # Constructing the INSERT statement
#     insert_query = f"""INSERT INTO {obj.__table__} ({column_names}) VALUES ({placeholders}) RETURNING id;"""
    
#     # Executing the INSERT statement and getting the newly created id
#     cursor.execute(insert_query, values)
#     new_id = cursor.fetchone()[0]  # Assuming 'id' is the first column in the RETURNING clause
#     conn.commit()
    
#     # Fetching the newly inserted record by its id
#     cursor.execute(f"""SELECT * FROM {obj.__table__} WHERE id = %s;""", (new_id,))
#     record = cursor.fetchone()
    
#     # convert the record back into a Company object
#     return build_from_record(type(obj), record)



def values(obj):
    venue_attrs = obj.__dict__
    return [venue_attrs[attr] for attr in obj.columns if attr in venue_attrs.keys()]

def keys(obj):
    venue_attrs = obj.__dict__
    selected = [attr for attr in obj.columns if attr in venue_attrs.keys()]
    return ', '.join(selected)

def drop_records(cursor, conn, table_name):
    cursor.execute(f"DELETE FROM {table_name};")
    conn.commit()

def drop_tables(table_names, cursor, conn):
    for table_name in table_names:
        drop_records(cursor, conn, table_name)

# def drop_all_tables(conn, cursor):
#     table_names = [] 
#     drop_tables(table_names, cursor, conn)

def find_by_name(Class, name, cursor):
    query = f"""SELECT * FROM {Class.__table__} WHERE name = %s """
    cursor.execute(query, (name,))
    record =  cursor.fetchone()
    obj = build_from_record(Class, record)
    return obj

def find_or_create_by_name(Class, name, conn, cursor):
    obj = find_by_name(Class, name, cursor)
    if not obj:
        new_obj = Class()
        new_obj.name = name
        obj = save(new_obj, conn, cursor)
    return obj

def find_or_build_by_name(Class, name, cursor):
    obj = Class.find_by_name(name, cursor)
    if not obj:
        obj = Class()
        obj.name = name
    return obj

