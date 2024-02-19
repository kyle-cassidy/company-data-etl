import json
from backend.api.src.models.company import Company
from backend.api.src.models.stock import Stock
from backend.api.src.db.db import save, find_or_create_by_name


class CompanyAdapter:
    @staticmethod
    def transform(data):
        return Company(**data)

    @staticmethod
    def load(data, conn, cursor):
        company = CompanyAdapter.transform(data)
        return save(company, conn, cursor)

class StockAdapter:
    @staticmethod
    def transform(data):
        return [Stock(**item) for item in data]

    @staticmethod
    def load(data, conn, cursor):
        stocks = StockAdapter.transform(data)
        for stock in stocks:
            save(stock, conn, cursor)


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def process_sample_data(conn, cursor):
    # Example usage for loading company data
    company_data = load_json('/path/to/sample-data/company_profile.json')
    CompanyAdapter.load(company_data, conn, cursor)

    # Example usage for loading stock data
    stock_data = load_json('/path/to/sample-data/stocks_eod_historical.json')
    StockAdapter.load(stock_data, conn, cursor)

