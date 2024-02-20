# this area is used for testing.
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error

from api.src.clients.fmp_client import FMPClient
from api.src.utils.seed_adapters.run_seed_adapters import seed_sp500_data
from config import current_config
import psycopg2
from api.src import create_app 

from flask import current_app, g
from api.src.db import (
    get_db, close_db, save, build_from_record, build_from_records,
    find, find_all, values, keys, drop_tables, drop_records,
    find_or_create_by_name, find_or_build_by_name
)


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


# from api.src import create_app

# app = create_app()
# app.run(debug = True, host = '0.0.0.0')
from api.src.utils.seed_adapters.run_seed_adapters import seed_sp500_data
# seed_sp500_data()
