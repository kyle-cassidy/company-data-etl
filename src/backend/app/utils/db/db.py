from flask import Flask, current_app, g
from config_sqlite import current_config, TestingSQLiteConfig
# from config_postgres import current_config, TestingConfig, DevelopmentConfig, ProductionConfig
# from secrets_manager.settings import DB_USER, DB_NAME, DB_HOST, DB_PASSWORD, DEBUG, TESTING
import sqlite3
import psycopg2


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

def save(obj, conn, cursor):
    keys_list = keys(obj).split(', ')                                                       # Extracting keys (column names) and values from the object
    values_dict = {key: getattr(obj, key) for key in keys_list}
    
    column_names = ', '.join(keys_list)                                                     # Constructing the parameterized column names
    placeholders = ', '.join([f":{key}" for key in keys_list])                              # and values placeholders
    
    insert_query = f"""
    INSERT INTO {obj.__table__} ({column_names}) 
    VALUES ({placeholders});
    """                                                                                     # Constructing the INSERT statement
    cursor.execute(insert_query, values_dict)                                               # Executing the INSERT statement
    conn.commit()
    
    last_id = cursor.lastrowid if hasattr(cursor, 'lastrowid') else cursor.fetchone()[0]    # Get the last inserted id for SQLite or PostgreSQL
    
    cursor.execute(f"SELECT * FROM {obj.__table__} WHERE id = :id", {'id': last_id})        # Fetching the newly inserted record by its id
    record = cursor.fetchone()
    
    return build_from_record(type(obj), record)  # Convert the record back into an object of the same type


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
