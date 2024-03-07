from ...models.phase_1.sp_company import SPCompany
from ...models.phase_1.sp_stock import SPStock
from ...models.phase_1.sp_index_level import SPIndexLevel

# from app.models.phase_1.sp_company import SPCompany
# from app.models.phase_1.sp_stock import SPStock
# from app.models.phase_1.sp_index_level import SPIndexLevel

from sqlalchemy.orm import Session
from app import db
import pandas as pd
import os
import datetime


# TODO: add financial statement adapters


class SP500Seeder:
    def __init__(self, session):
        self.session = session

    def close(self):
        """Close the database session."""
        self.session.close()

    def seed_companies(self, companies_csv_directory):
        # sourcery skip: class-extract-method

        try:
            for filename in os.listdir(companies_csv_directory):
                if filename.endswith(".csv"):
                    # Construct the full path to the CSV file
                    companies_csv_path = os.path.join(companies_csv_directory, filename)
                    companies_df = pd.read_csv(companies_csv_path)
                    # Iterate over each row in the DataFrame
                    for _, row in companies_df.iterrows():
                        # Map CSV row to company_data dictionary
                        company_data = {
                            "exchange": row["Exchange"],
                            "symbol": row["Symbol"],
                            "short_name": row["Shortname"],
                            "long_name": row["Longname"],
                            "sector": row["Sector"],
                            "industry": row["Industry"],
                            "current_price": row["Currentprice"],
                            "market_cap": row["Marketcap"],
                            "ebitda": row["Ebitda"],
                            "revenue_growth": row["Revenuegrowth"],
                            "city": row["City"],
                            "state": row["State"],
                            "country": row["Country"],
                            "long_business_summary": row["Longbusinesssummary"],
                            "weight": row["Weight"],
                        }
                        # Create an instance of SPCompany with the mapped data
                        new_company = SPCompany(**company_data)
                        # Add the new instance to the session
                        self.session.add(new_company)

            # After all companies have been added to the session, commit the session to save changes to the database
            self.session.commit()
            print("Companies seeded to the database successfully")
        except Exception as e:
            print("Error seeding companies to the database. Rolling back changes.")
            self.session.rollback()
            # Raise the error for further handling
            raise e
        finally:
            print("Closing the session")
            self.session.close()

    def seed_stocks(self, stocks_csv_directory):
        try:
            for filename in os.listdir(stocks_csv_directory):
                if filename.endswith(".csv"):
                    stocks_csv_path = os.path.join(stocks_csv_directory, filename)
                    stocks_df = pd.read_csv(stocks_csv_path)
                    for _, row in stocks_df.iterrows():
                        date_object = datetime.datetime.strptime(
                            row["Date"], "%Y-%m-%d"
                        ).date()
                        stock_data = {
                            "date": date_object,
                            "symbol": row["Symbol"],
                            "adj_close": row["Adj Close"],
                            "close": row["Close"],
                            "high": row["High"],
                            "low": row["Low"],
                            "open": row["Open"],
                            "volume": row["Volume"],
                        }
                        new_stock = SPStock(**stock_data)
                        self.session.add(new_stock)
            self.session.commit()
            print("Stocks seeded to the database successfully")

        except Exception as e:
            print("Error seeding stocks to the database. Rolling back changes.")
            self.session.rollback()
            raise e

        finally:
            print("Stocks seeding process completed.")

    def seed_index(self, index_csv_directory):
        try:
            for filename in os.listdir(index_csv_directory):
                if filename.endswith(".csv"):
                    index_csv_path = os.path.join(index_csv_directory, filename)
                    index_df = pd.read_csv(index_csv_path)
                    for _, row in index_df.iterrows():
                        index_data = {
                            "date": row["Date"],
                            "index_level": row["IndexLevel"],
                            "index_name": "S&P 500",
                        }
                        new_index = SPIndexLevel(**index_data)
                        self.session.add(new_index)
            self.session.commit()
            print("Index levels seeded to the database successfully")

        except Exception as e:
            print("Error seeding index levels to the database. Rolling back changes.")
            self.session.rollback()
            raise e

        finally:
            print("Index seeding process completed.")


# ------------------------------------------------------------------------------------------------------------------------#
# data selction notes:
# companies
# sp500_companies.csv rows: Exchange,Symbol,Shortname,Longname,Sector,Industry,Currentprice,Marketcap,Ebitda,Revenuegrowth,City,State,Country,Fulltimeemployees,Longbusinesssummary,Weight
# SPCompany model columns: columns = ['exchange', 'symbol', 'short_name', 'long_name', 'sector', 'industry', 'current_price', 'market_cap', 'ebitda', 'revenue_growth', 'city', 'state', 'country', 'fulltime_employees', 'long_business_summary', 'weight']
# stocks
# sp500_stocks.csv rows: Date,Symbol,Adj Close,Close,High,Low,Open,Volume
# SPStock model columns: columns = ['date', 'symbol', 'adj_close', 'close', 'high', 'low', 'open', 'volume']
# index
# sp500_index.csv rows: Date,IndexLevel,IndexName
# SPIndexLevel model columns: columns = ['date', 'index_level', 'index_name']
