from backend.api.src.db.db import get_db, save, find_or_create_by_name
import backend.api.src.models as models
import pandas as pd

class SP500Seeder:
    def __init__(self, db_connection):
        self.conn = db_connection
        self.cursor = self.conn.cursor()

    def seed_companies(self, companies_csv_path):
        companies_df = pd.read_csv(companies_csv_path)
        companies_selected_columns = ['Exchange', 'Symbol', 'Shortname', 'Sector', 'Industry', 'City', 'State', 'Country']
        for _, row in companies_df[companies_selected_columns].iterrows():
            exchange = find_or_create_by_name(models.Exchange, row['Exchange'], self.conn, self.cursor)
            sector = find_or_create_by_name(models.Sector, row['Sector'], self.conn, self.cursor)
            industry = find_or_create_by_name(models.Industry, row['Industry'], self.conn, self.cursor)
            location = find_or_create_by_name(models.Location, f"{row['City']}, {row['State']}, {row['Country']}", self.conn, self.cursor)
            company_data = {
                'name': row['Shortname'],
                'ticker_symbol': row['Symbol'],
                'industry_id': industry.industry_id,
                'sector_id': sector.sector_id,
                'exchange_id': exchange.exchange_id,
                'location_id': location.location_id
            }
            save(models.Company(**company_data), self.conn, self.cursor)

    def seed_stocks(self, stocks_csv_path):
        stocks_df = pd.read_csv(stocks_csv_path)
        for _, row in stocks_df.iterrows():
            company = find_or_create_by_name(models.Company, row['Symbol'], self.conn, self.cursor)
            stock_data = {
                'company_id': company.company_id,
                'date': row['Date'],
                'open_price': row['Open'],
                'high_price': row['High'],
                'low_price': row['Low'],
                'close_price': row['Close'],
                'adjusted_close_price': row['Adj Close'],
                'volume': row['Volume']
            }
            save(models.Stock(**stock_data), self.conn, self.cursor)

    def seed_index(self, index_csv_path):
        index_df = pd.read_csv(index_csv_path)
        for _, row in index_df.iterrows():
            index_data = {
                'name': 'S&P 500',
                'symbol': 'SPX',
                'description': 'Standard & Poor\'s 500 index'
            }
            save(models.StockMarketIndex(**index_data), self.conn, self.cursor)

    def close(self):
        self.cursor.close()
        self.conn.close()