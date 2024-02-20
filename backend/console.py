from api.src.clients.fmp_client import FMPClient
from api.src.utils.seed_adapters.run_seed_adapters import seed_sp500_data
from config import Config, DevelopmentConfig, TestingConfig, ProductionConfig 
import psycopg2

client = FMPClient()

# testing daily API requests 
# print(client.request_company_profile('AAPL'))
# print(client.request_stock_list())
# print(client.request_all_countries())
# print(client.request_stock_screener('Technology', 'Software - Infrastructure'))
# print(client.request_income_statement('AAPL'))
# print(client.request_balance_sheet('AAPL'))
# print(client.request_cash_flow_statement('AAPL'))
# print(client.request_income_statement_as_reported('AAPL'))
# print(client.request_historical_stock_prices('AAPL'))

# these may be defunct
# print(client.request_institutional_stock_ownership('AAPL'))
# print(client.request_analyst_stock_recommendations('AAPL'))


# test_conn = psycopg2.connect(
#     host = Config.DB_HOST, 
#     database = Config.DB_NAME,
#     user = Config.DB_USER, 
#     password = Config.DB_PASSWORD
#     )

# test_conn = psycopg2.connect(
#     host = TestingConfig.DB_HOST, 
#     database = TestingConfig.DB_NAME,
#     user = TestingConfig.DB_USER, 
#     password = TestingConfig.DB_PASSWORD
#     )
# test_cursor = test_conn.cursor()

# seed_database_with_sp500_data = seed_sp500_data(test_conn)


from api.src import create_app 
from api.src.utils.seed_adapters.run_seed_adapters import seed_sp500_data
import psycopg2

app = create_app(config_class=TestingConfig)
with app.app_context():
    seed_sp500_data()
