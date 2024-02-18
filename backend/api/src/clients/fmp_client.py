import requests
from requests.exceptions import HTTPError
from secrets.settings import FMP_API_KEY

class FMPClient:

    def __init__(self,API_KEY=FMP_API_KEY):
        self.API_KEY = API_KEY
        self.base_URL = 'https://financialmodelingprep.com/api/v3/'       



    def make_request(self, endpoint: str, params=None)-> dict:
        """
        Makes a generic GET request to the specified endpoint.
        :endpoint: API endpoint to be appended to the base host URL.
        :params: Takes a dictionary as input. Additional parameters for the request.
        :return: JSON response from the API.
        """
        
        if params is None:                              # If no params are passed, 
            params = {}                                 # initialize an empty dictionary
        params['apikey'] = self.API_KEY                 # Include the API key in every request. add to params dict.
        URL = f'{self.base_URL}/{endpoint}'             # Construct the URL 
        response = requests.get(URL, params=params)     # Make the request
        params.pop('apikey', None)                      # Remove API key from params after request to avoid leaking it.
        
        if response.status_code != 200:
            raise HTTPError(f'API request failed with status code {response.status_code}: {response.text}')

        return response.json()


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
    

    def request_income_statement(self, symbol: str, period: str = 'annual', datatype: str = 'json', limit: int = 100) -> dict:
        """
        Get the income statement for a company.
        :param symbol: Stock ticker symbol.
        :param period: Period of the income statement ('annual', 'quarterly').
        :param datatype: Data type of the response ('json', 'csv').
        :param limit: Limit the number of items in the response.
        :return: JSON response containing the income statement.
        """
        endpoint = f"income-statement/{symbol}"
        params = {
            'period': period,
            'datatype': datatype,
            'limit': limit
        }
        return self.make_request(endpoint, params=params)

    def request_balance_sheet(self, symbol: str, period: str = 'annual', datatype: str = 'json', limit: int = 100) -> dict:
        """
        Get the balance sheet statement for a company.
        :param symbol: Stock ticker symbol.
        :param period: Period of the balance sheet ('annual', 'quarterly').
        :param datatype: Data type of the response ('json', 'csv').
        :param limit: Limit the number of items in the response.
        :return: JSON response containing the balance sheet.
        """
        endpoint = f"balance-sheet-statement/{symbol}"
        params = {
            'period': period,
            'datatype': datatype,
            'limit': limit
        }
        return self.make_request(endpoint, params=params)

    def request_cash_flow_statement(self, symbol: str, period: str = 'annual', datatype: str = 'json', limit: int = 100) -> dict:
        """
        Get the cash flow statement for a company.
        :param symbol: Stock ticker symbol.
        :param period: Period of the cash flow statement ('annual', 'quarterly').
        :param datatype: Data type of the response ('json', 'csv').
        :param limit: Limit the number of items in the response.
        :return: JSON response containing the cash flow statement.
        """
        endpoint = f"cash-flow-statement/{symbol}"
        params = {
            'period': period,
            'datatype': datatype,
            'limit': limit
        }
        return self.make_request(endpoint, params=params)

    def request_income_statement_as_reported(self, symbol: str, period: str = 'annual', limit: int = 50) -> dict:
        """
        Get the income statement as reported by the company.
        :param symbol: Stock ticker symbol.
        :param period: Period of the income statement ('annual', 'quarterly').
        :param limit: Limit the number of items in the response.
        :return: JSON response containing the income statement.
        """
        endpoint = f"income-statement-as-reported/{symbol}"
        params = {
            'period': period,
            'limit': limit
        }
        return self.make_request(endpoint, params=params)


    def request_historical_stock_prices(self, ticker):
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

