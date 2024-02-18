from api.src.clients import FMPClient

def test_fmp_client_endpoints():
    client = FMPClient()

    # Test request_sector_peers
    sector_peers = client.request_sector_peers()
    print("Sector Peers:", sector_peers)

    # Test request_company_profile
    company_profile = client.request_company_profile('AAPL')
    print("Company Profile:", company_profile)

    # Test request_stock_list
    stock_list = client.request_stock_list()
    print("Stock List:", stock_list)

    # Test request_all_countries
    all_countries = client.request_all_countries()
    print("All Countries:", all_countries)

    # Test request_stock_screener
    stock_screener = client.request_stock_screener('Technology', 'Software—Infrastructure')
    print("Stock Screener:", stock_screener)

    # Test request_financial_statements
    financial_statements = client.request_financial_statements('AAPL', 'income')
    print("Financial Statements:", financial_statements)

    # Test request_historical_price_full
    historical_price_full = client.request_historical_price_full('AAPL')
    print("Historical Price Full:", historical_price_full)

    # Test request_institutional_stock_ownership
    institutional_stock_ownership = client.request_institutional_stock_ownership('AAPL')
    print("Institutional Stock Ownership:", institutional_stock_ownership)

    # Test request_analyst_stock_recommendations
    analyst_stock_recommendations = client.request_analyst_stock_recommendations('AAPL')
    print("Analyst Stock Recommendations:", analyst_stock_recommendations)

# Uncomment the line below to run the test when this script is executed
# test_fmp_client_endpoints()
# works
# client = FMPClient()
# test_top_peers = client.request_sector_peers()

