
# import numpy as np
# import pandas as pd 


# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.metrics import mean_squared_error

# # from api.src.clients.fmp_client import FMPClient
# from api.src.utils.seed_adapters.run_seed_adapters import seed_sp500_data
# import api.src.models.phase_1 as models


# client = FMPClient()

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


import sqlite3

try:
    conn = sqlite3.connect('api/data/sp500_p1.sqlite')
    print("Connected to the database successfully")
    conn.close()
except sqlite3.OperationalError as e:
    print(f"Error: {e}")