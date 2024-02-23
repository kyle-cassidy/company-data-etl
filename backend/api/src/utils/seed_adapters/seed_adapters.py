from ...db.db import get_db, save
from ...models.phase_1.sp_company import SPCompany
from ...models.phase_1.sp_stock import SPStock
from ...models.phase_1.sp_index_level import SPIndexLevel
import pandas as pd
import os

class SP500Seeder:
    def __init__(self, db_connection):
        self.conn = db_connection
        self.cursor = self.conn.cursor()
    
    # csv rows: Exchange,Symbol,Shortname,Longname,Sector,Industry,Currentprice,Marketcap,Ebitda,Revenuegrowth,City,State,Country,Fulltimeemployees,Longbusinesssummary,Weight
    # model columns: columns = ['exchange', 'symbol', 'short_name', 'long_name', 'sector', 'industry', 'current_price', 'market_cap', 'ebitda', 'revenue_growth', 'city', 'state', 'country', 'fulltime_employees', 'long_business_summary', 'weight']
    
    def seed_companies(self, companies_csv_directory):
        
        for filename in os.listdir(companies_csv_directory):                            # Iterate over each CSV file in the directory
            if filename.endswith('.csv'):
                companies_csv_path = os.path.join(companies_csv_directory, filename)    # Iterate over each row in the DataFrame
                companies_df = pd.read_csv(companies_csv_path)
                
                for _, row in companies_df.iterrows():                                  # Map CSV row to company_data dictionary including all columns
                    company_data = {
                        'exchange': row['Exchange'],
                        'symbol': row['Symbol'],
                        'short_name': row['Shortname'],
                        'long_name': row['Longname'],
                        'sector': row['Sector'],
                        'industry': row['Industry'],
                        'current_price': row['Currentprice'],
                        'market_cap': row['Marketcap'],
                        'ebitda': row['Ebitda'],
                        'revenue_growth': row['Revenuegrowth'],
                        'city': row['City'],
                        'state': row['State'],
                        'country': row['Country'],
                        'long_business_summary': row['Longbusinesssummary'],
                        'weight': row['Weight']
                    }
                    save(SPCompany(**company_data), self.conn, self.cursor)

                    

    def seed_stocks(self, stocks_csv_directory):
        for filename in os.listdir(stocks_csv_directory):
            if filename.endswith('.csv'):
                stocks_csv_path = os.path.join(stocks_csv_directory, filename)
                stocks_df = pd.read_csv(stocks_csv_path)
                for _, row in stocks_df.iterrows():
                    stock_data = {
                        'date': row['Date'],
                        'symbol': row['Symbol'],
                        'adj_close': row['Adj Close'],
                        'close': row['Close'],
                        'high': row['High'],
                        'low': row['Low'],
                        'open': row['Open'],
                        'volume': row['Volume']
                    }
                    save(SPStock(**stock_data), self.conn, self.cursor)
    
    
    def seed_index(self, index_csv_directory):
        for filename in os.listdir(index_csv_directory):
            if filename.endswith('.csv'):
                index_csv_path = os.path.join(index_csv_directory, filename)
                index_df = pd.read_csv(index_csv_path)
                for _, row in index_df.iterrows():
                    index_data = {
                        'date': row['Date'],
                        'index_level': row['IndexLevel'],
                        'index_name': 'S&P 500' 
                    }
                    save(SPIndexLevel(**index_data), self.conn, self.cursor)

    def close(self):
        self.cursor.close()
        self.conn.close()