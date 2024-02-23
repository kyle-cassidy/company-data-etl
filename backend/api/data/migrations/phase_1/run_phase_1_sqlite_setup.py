import sqlite3

def create_tables_from_sql_file(db_path, sql_file_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    with open(sql_file_path, 'r') as sql_file:
        sql_script = sql_file.read()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_path = 'backend/api/data/sp500_p1.sqlite'
    sql_file_path = 'backend/api/data/migrations/phase_1/create_tables_phase_1_lite.sql'
    create_tables_from_sql_file(db_path, sql_file_path)