import csv
from backend.api.src.db.db import get_db, save, find_or_create_by_name
import backend.api.src.models as models


class SeedAdapter:
    @staticmethod
    def transform(data):
        return Company(**data)

    @staticmethod
    def load(data, conn, cursor):
        company = SeedAdapter.transform(data)
        return save(company, conn, cursor)
    
    
def seed_database_from_csv(csv_file_path):
    conn = get_db()
    cursor = conn.cursor()
    
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            # Assuming the CSV columns match the order and data needed for your database
            exchange_name, ticker_symbol, company_name, _, sector_name, industry_name, _, _, _, _, city, state, country, _ = row
            
            # Handle related data (sector, industry, exchange, location) 
            sector = find_or_create_by_name(models.Sector, sector_name, conn, cursor)
            industry = find_or_create_by_name(models.Industry, industry_name, conn, cursor)
            exchange = find_or_create_by_name(models.Exchange, exchange_name, conn, cursor)
            location = find_or_create_by_name(models.Location, f"{city}, {state}, {country}", conn, cursor)  # FIXME simplified
            
            # Create and save the company
            company_data = {
                'name': company_name,
                'ticker_symbol': ticker_symbol,
                'industry_id': industry.industry_id,
                'sector_id': sector.sector_id,
                'exchange_id': exchange.exchange_id,
                'location_id': location.location_id,
                'isEtf': False,  # Assuming this data is not in the CSV
                'isActivelyTrading': True  # Assuming this data is not in the CSV
            }
            company = Company(**company_data)
            save(company, conn, cursor)
    
    # Close the cursor and connection if necessary
    cursor.close()
    conn.close()
    
    
 