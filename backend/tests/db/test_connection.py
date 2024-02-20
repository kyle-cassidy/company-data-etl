import pytest
import psycopg2
from psycopg2 import OperationalError
from config import TestingConfig  # or wherever your config is

def test_db_connection():
    connection_params = {
        'host': TestingConfig.DB_HOST,
        'database': TestingConfig.DB_NAME,
        'user': TestingConfig.DB_USER,
        'password': TestingConfig.DB_PASSWORD
    }
    try:
        # Use your connection parameters to establish a connection
        conn = psycopg2.connect(**connection_params)
        
        # Create a cursor object using the cursor() method
        cursor = conn.cursor()
        
        # Execute a simple query to get the PostgreSQL version
        cursor.execute("SELECT version();")
        
        # Fetch and print the result of the query
        db_version = cursor.fetchone()
        print("Connected to PostgreSQL version:", db_version)
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
    except OperationalError as e:
        pytest.fail(f"Unable to connect to the database: {e}")

# You can run this test using the pytest command in the terminal