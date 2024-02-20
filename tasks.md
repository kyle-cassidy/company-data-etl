[[task-overview-company-data-etl]]

# tasks

## backend
- [x] Set up the environment.
- [x] Identify data sources.
- [x] Define the database schema.
- [x] Built initial API client for database connections
- [x] initialize the model classes.
- [x] build historical model **clases**
- [x] update schema to adhere to 2nd formal form. 


### adapters -> psql map
- [ ] company -> companies 
- [ ] 
### models
- [x] refactor the financial python model class into three models
- [ ] build model relations

### app
- [ ] Initialize Flask application.
- [ ] 

- [ ] Write utility scripts.
- [ ] Write tests.
- [ ] 

## phase 2
- [ ] analysis 
- [ ] streamlit

## phase 3
- [ ] unstructured data adapters to interact with [[endpoints]], models, postgres
- [ ] 


---

1. `settings.py` - Configures environment variables and application settings such as database connection details and debug flags.

2. `api/src/__init__.py` - Initializes the Flask application, sets up routes, and configures the database connection.

3. `api/src/db/db.py` - Contains functions for database operations such as connecting to the database, finding records, and building model instances from database records.

4. `api/src/db/migrations/create_tables.sql` - SQL script to create the necessary tables in the database with the appropriate constraints and indexes.

5. `api/src/models/__init__.py` - Imports all the model classes to make them available throughout the application.

6. `api/src/models/` - Define the ORM model classes that represent the tables in the database and include methods for interacting with the database.

7. `api/src/adapters/client.py` - Handles making requests to the external API and retrieving data.

8. `api/src/adapters/`- Contains builder classes that construct and persist model instances based on data from the API.

9. `manage.py` - Provides command-line interface commands for running the Flask application and other utility functions.

10. `run.py` - The entry point for running the Flask application.

11. `entrypoint.sh` - Shell script used as the entry point for running the application in a Docker container or similar environments.

12. `requirements.txt` - Lists the Python package dependencies required for the backend application.

13. `.gitignore` - Specifies intentionally untracked files to ignore in the Git version control system.

14. `console.py` - A script for interactive testing and debugging of the application's models and database operations.

15. `tests/` - Contains test cases for the application's models, adapters, and other components to ensure they work as expected.



```python

class StockBuilder:
    attributes = ['symbol', 'name', 'price', 'volume']

    def select_attributes(self, stock_data):
        # Extract and return relevant attributes from stock_data
        pass

    def run(self, stock_data, conn, cursor):
        selected = self.select_attributes(stock_data)
        stock = Stock.find_by_symbol(selected['symbol'], cursor)
        if stock:
            stock.exists = True
            return stock
        else:
            stock = db.save(Stock(**selected), conn, cursor)
            stock.exists = False
            return stock
```
