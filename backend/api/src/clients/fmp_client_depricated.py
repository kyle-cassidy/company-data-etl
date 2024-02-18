# import requests
# import numpy as np
# import pandas as pd
# from settings import FMP_API_KEY

# class FMPClient:
#     '''
#     base client for fetching data from the financialmodelingprep.com API
#     '''
#     # class varaibles
#     FMP_API_KEY = FMP_API_KEY
#     base_url =  'https://financialmodelingprep.com/api/v3/'
    
#     def __init__(self):...
    
    
#     def request_sector_peers(self, 
#                              sector = 'Technology', 
#                              exchange = 'NASDAQ', 
#                              market_cap_more_than = 1000000000, 
#                              limit_number_of_peers = 10):
        
#         '''
#         Fetches the company peers of a given sector.
#         default sector is 'Technology'
#         default exchange is 'NASDAQ'
#         default market cap is more than 1 billion
#         default limit of companies displayed is 10
#         '''
#         # verify that the inputs are strings. phase2: add more input validation
#         sector = str(sector)
#         exchange = str(exchange)
#         market_cap_more_than = str(market_cap_more_than)
#         limit_number_of_peers = str(limit_number_of_peers)
        
#         url = self.base_url + f'stock-screener?marketCapMoreThan={market_cap_more_than}&volumeMoreThan=10000§or={sector}&exchange={exchange}&limit={limit_number_of_peers}&apikey={FMP_API_KEY}'
                                                                                    
#         response = requests.get(url)
#         data = response.json()
        
#         return data
    
# ###

# import requests
# from backend.secrets.settings import FMP_API_KEY

# class FMPClient:
#     '''
#     Base client for fetching data from the financialmodelingprep.com API
#     '''
#     # Class variables
#     FMP_API_KEY = FMP_API_KEY
#     base_url = 'https://financialmodelingprep.com/api/v3/'
    
    
#     def __init__(self):
#         self.FMP_API_KEY = FMP_API_KEY
#         self.sector_peers_endpoint = 'stock-screener'
#         ...
    
    
#     def request_sector_peers(self, 
#                              sector='Technology', 
#                              exchange='NASDAQ', 
#                              market_cap_more_than=1000000000, 
#                              limit=None):
#         '''
#         the 'stock screener' endpoint will fetch the company, 
#         industry peers, and basic stock summary of a given sector.
#         '''
#         params = {
#             'sector': sector,
#             'exchange': exchange,
#             'marketCapMoreThan': market_cap_more_than,
#             'volumeMoreThan': 10000,
#             'limit': limit,
#             'apikey': self.FMP_API_KEY
#         }
        
#         response = requests.get(f"{self.base_url}{self.sector_peers_endpoint}", params=params)
#         data = response.json()
        
#         return data




