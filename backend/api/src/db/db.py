from flask import current_app
from flask import g
# from backend.secrets.settings import DB_USER, DB_NAME, DB_HOST, DB_PASSWORD, DEBUG, TESTING #TODO: check config imports
from config import Config, DevelopmentConfig, TestingConfig, ProductionConfig
from secrets_manager.settings import DB_USER, DB_NAME, DB_HOST, DB_PASSWORD, DEBUG, TESTING

import psycopg2
from psycopg2 import connect
from psycopg2.extensions import make_dsn
from config import current_config

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

# dsn = make_dsn(
#     host=current_config.DB_HOST, 
#     dbname=current_config.DB_NAME,
#     user=current_config.DB_USER,
#     password=current_config.DB_PASSWORD
# )

# conn = connect(dsn)


#TODO: build main db connection

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

def get_db():
    with current_app.app_context():
        if "db" not in g:
            g.db = psycopg2.connect(
                host=current_config.DB_HOST,
                user=current_config.DB_USER,
                password=current_config.DB_PASSWORD,
                dbname=current_config.DB_NAME)
        return g.db

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

def find(Class, id, cursor):
    sql_str = f"SELECT * FROM {Class.__table__} WHERE id = %s"
    cursor.execute(sql_str, (id,))
    record = cursor.fetchone()
    return build_from_record(Class, record)

# def save(obj, conn, cursor):
#     s_str = ', '.join(len(values(obj)) * ['%s'])
#     obj_str = f"""INSERT INTO {obj.__table__} ({keys(obj)}) VALUES ({s_str});"""
#     cursor.execute(obj_str, list(values(obj)))
#     conn.commit()
#     cursor.execute(f'SELECT * FROM {obj.__table__} ORDER BY id DESC LIMIT 1')
#     record = cursor.fetchone()
#     return build_from_record(type(obj), record)

# alternate save method
# def save(obj, conn, cursor):
#     s_str = ', '.join(len(values(obj)) * ['%s'])
#     obj_str = f"""INSERT INTO {obj.__table__} ({keys(obj)}) VALUES ({s_str}) RETURNING {obj.columns[0]};""" #In this modification, the `INSERT` statement now includes a `RETURNING` clause that returns the value of the primary key column immediately after insertion. The `find` function is then used to retrieve the full record using the returned primary key value.}
#     cursor.execute(obj_str, list(values(obj)))
#     primary_key_value = cursor.fetchone()[0]
#     conn.commit()
#     return find(obj.__class__, primary_key_value, cursor)

# def save(obj, conn, cursor):
#     # Exclude the 'id' attribute if it exists since it's auto-generated
#     attr_to_save = {k: v for k, v in obj.__dict__.items() if k != 'id'}
    
#     # Construct the INSERT statement without the 'id'
#     columns_str = ', '.join(attr_to_save.keys())
#     values_str = ', '.join(['%s'] * len(attr_to_save))
    
#     # Create the SQL statement with RETURNING clause for 'id'
#     sql_str = f"INSERT INTO {obj.__table__} ({columns_str}) VALUES ({values_str}) RETURNING id;"
    
#     # Execute the statement and commit the changes
#     cursor.execute(sql_str, list(attr_to_save.values()))
#     obj_id = cursor.fetchone()[0] # Fetch the generated id
#     conn.commit()

def save(obj, conn, cursor):
    # Extracting keys (column names) and values from the object
    keys = [key for key in obj.columns if hasattr(obj, key)]
    values = [getattr(obj, key) for key in keys]
    
    # Correctly handling the column names for SQL
    column_names = ', '.join(keys)
    placeholders = ', '.join(['%s'] * len(values))
    
    # Constructing the INSERT statement
    insert_query = f"""INSERT INTO {obj.__table__} ({column_names}) VALUES ({placeholders}) RETURNING id;"""
    
    # Executing the INSERT statement and getting the newly created id
    cursor.execute(insert_query, values)
    new_id = cursor.fetchone()[0]  # Assuming 'id' is the first column in the RETURNING clause
    conn.commit()
    
    # Fetching the newly inserted record by its id
    cursor.execute(f"""SELECT * FROM {obj.__table__} WHERE id = %s;""", (new_id,))
    record = cursor.fetchone()
    
    # convert the record back into a Company object
    return build_from_record(type(obj), record)



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

