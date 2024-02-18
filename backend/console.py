from api.src.clients.fmp_client import FMPClient

client = FMPClient()

# these work
print(client.request_company_profile('AAPL'))
print(client.request_stock_list())
print(client.request_all_countries())
print(client.request_stock_screener('Technology', 'Software - Infrastructure'))
print(client.request_income_statement('AAPL'))
print(client.request_balance_sheet('AAPL'))
print(client.request_cash_flow_statement('AAPL'))
print(client.request_income_statement_as_reported('AAPL'))
print(client.request_historical_stock_prices('AAPL'))

# these may be defunct
# print(client.request_institutional_stock_ownership('AAPL'))
# print(client.request_analyst_stock_recommendations('AAPL'))
