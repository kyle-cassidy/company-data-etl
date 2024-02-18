import requests
from requests.exceptions import HTTPError
from secrets.settings import FMP_API_KEY

class FMPClient:
    
    def __init__(self,API_KEY=FMP_API_KEY):
        self.API_KEY = API_KEY
        self.base_URL = 'https://financialmodelingprep.com/api/v3/'       
        self.sector_peers_endpoint = 'stock-screener'
    
    
    def make_request(self, endpoint: str, params=None)-> dict:
        """
        Makes a generic GET request to the specified endpoint.
        :endpoint: API endpoint to be appended to the base host URL.
        :params: Takes a dictionary as input. Additional parameters for the request.
        :return: JSON response from the API.
        """
        
        if params is None:                              # If no params are passed, 
            params = {}                                 # initialize an empty dictionary
        params['apikey'] = self.API_KEY                # Include the API key in every request. add to params dict.
        URL = f'{self.base_URL}/{endpoint}'             # Construct the URL 
        response = requests.get(URL, params=params)     # Make the request
        params.pop('apikey', None)                     # Remove API key from params after request to avoid leaking it.
        
        if response.status_code != 200:
            raise HTTPError(f'API request failed with status code {response.status_code}: {response.text}')

        return response.json()

    
    def request_sector_peers(self, sector='Technology', exchange='NASDAQ', market_cap_more_than=1000000000, volumeMoreThan=10000, limit=None):

        '''
        this endpoint is destined to populate the _______ table.                    #TODO: add table name
        the 'stock screener' endpoint will fetch the company, 
        industry peers, and basic stock summary of a given sector.
        '''
        
        params = {
            'sector': sector,
            'exchange': exchange,
            'marketCapMoreThan': market_cap_more_than,
            'volumeMoreThan': volumeMoreThan,
            'limit': limit
        }
        
        return self.make_request(self.sector_peers_endpoint, params=params)
    
    
    
    def request_company_profile(self, ticker):
        """
        Get company profile data.
        :param ticker: Stock ticker symbol.
        :return: JSON response containing company profile data.
        """
        endpoint = f"profile/{ticker}"
        return self.make_request(endpoint)

    def request_stock_list(self):
        """
        Get a list of all companies including the exchange they are traded on.
        :return: JSON response containing the stock list.
        """
        endpoint = "stock/list"
        return self.make_request(endpoint)

    def request_all_countries(self):
        """
        Get a list of all countries where stocks are traded.
        :return: JSON response containing the list of all countries.
        """
        endpoint = "get-all-countries"
        return self.make_request(endpoint)

    def request_stock_screener(self, sector, industry):
        """
        Filter companies by sector and industry.
        :param sector: Sector to filter by.
        :param industry: Industry to filter by.
        :return: JSON response containing the filtered company list.
        """
        endpoint = f"stock-screener?sector={sector}&industry={industry}"
        return self.make_request(endpoint)

    def request_financial_statements(self, ticker, statement_type):
        """
        Get financial statements (income statement, balance sheet, cash flow).
        :param ticker: Stock ticker symbol.
        :param statement_type: Type of financial statement ('income', 'balance_sheet', 'cash_flow').
        :return: JSON response containing the financial statements.
        """
        endpoint_map = {
            'income': "income-statement",
            'balance_sheet': "balance-sheet-statement",
            'cash_flow': "cash-flow-statement"
        }
        endpoint = f"{endpoint_map[statement_type]}/{ticker}"
        return self.make_request(endpoint)

    def request_historical_price_full(self, ticker):
        """
        Get historical stock prices.
        :param ticker: Stock ticker symbol.
        :return: JSON response containing historical stock prices.
        """
        endpoint = f"historical-price-full/{ticker}"
        return self.make_request(endpoint)

    def request_institutional_stock_ownership(self, ticker):
        """
        Get the institutional ownership of individual stocks.
        :param ticker: Stock ticker symbol.
        :return: JSON response containing institutional ownership data.
        """
        endpoint = f"institutional-ownership/symbol-ownership?symbol={ticker}"
        return self.make_request(endpoint)

    def request_analyst_stock_recommendations(self, ticker):
        """
        Get analyst stock recommendations.
        :param ticker: Stock ticker symbol.
        :return: JSON response containing analyst stock recommendations.
        """
        endpoint = f"analyst-stock-recommendations/{ticker}"
        return self.make_request(endpoint)

