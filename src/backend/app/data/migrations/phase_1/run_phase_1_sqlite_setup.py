import sqlite3
import os

# Define the path to the and create_tables & database files relative to the project root
db_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'sp500_p1_sm.sqlite')
sql_file_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'migrations', 'phase_1', 'create_tables_phase_1_lite.sql')

def create_tables_from_sql_file(db_path=db_path, sql_file_path=sql_file_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    with open(sql_file_path, 'r') as sql_file:
        sql_script = sql_file.read()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

# moved to seed_db.py
# if __name__ == "__main__":
#     db_path = 'backend/api/data/sp500_p1_sm.sqlite'
#     sql_file_path = 'backend/api/data/migrations/phase_1/create_tables_phase_1_lite.sql'
#     create_tables_from_sql_file(db_path, sql_file_path)