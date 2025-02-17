from sqlalchemy import create_engine, text
import os

db_path = os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "data", "sp500_p1_sm.sqlite"
)
sql_file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "..",
    "data",
    "migrations",
    "phase_1",
    "create_tables_phase_1_lite.sql",
)
db_uri = f"sqlite:///{db_path}"


def create_tables_from_sql_file(db_uri=db_uri, sql_file_path=sql_file_path):
    engine = create_engine(db_uri)
    with engine.connect() as connection:
        with open(sql_file_path, "r") as sql_file:
            # Split the script into separate statements on the semicolon (excluding any that are empty after the split)
            sql_statements = [
                statement.strip()
                for statement in sql_file.read().split(";")
                if statement.strip()
            ]
        for statement in sql_statements:
            # Wrap the statement with text() for SQLAlchemy to execute
            connection.execute(text(statement))


# depricated
# import sqlite3
# import os

# # Define the path to the and create_tables & database files relative to the project root
# db_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'sp500_p1_sm.sqlite') #FIXME: need to update migration paths to match new project structure
# sql_file_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'migrations', 'phase_1', 'create_tables_phase_1_lite.sql')

# def create_tables_from_sql_file(db_path=db_path, sql_file_path=sql_file_path):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     with open(sql_file_path, 'r') as sql_file:
#         sql_script = sql_file.read()
#     cursor.executescript(sql_script)
#     conn.commit()
#     conn.close()

# moved to seed_db.py
# if __name__ == "__main__":
#     db_path = 'backend/api/data/sp500_p1_sm.sqlite'
#     sql_file_path = 'backend/api/data/migrations/phase_1/create_tables_phase_1_lite.sql'
#     create_tables_from_sql_file(db_path, sql_file_path)
