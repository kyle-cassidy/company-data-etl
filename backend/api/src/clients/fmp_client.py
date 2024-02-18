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
    
    
    