import os
import sqlite3
from ...db.db import get_db, save, find_or_create_by_name
from ...utils.seed_adapters.seed_adapters import SP500Seeder

# sp500_companies = 'backend/api/data/seed-sp500/sp500_companies'
# sp500_stocks = 'backend/api/data/seed-sp500/sp500_stocks'
# sp500_index = 'backend/api/data/seed-sp500/sp500_index'

# sp500_p1_sqlite = 'backend/api/data/sp500_p1.sqlite'

# Define the path to the database file relative to the project root
sp500_p1_sqlite = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'sp500_p1_sm.sqlite')

# Define the paths to the CSV directories relative to the project root
sp500_companies = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'seed-sp500', 'sp500_companies')
sp500_stocks = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'seed-sp500', 'sp500_stocks')
sp500_index = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'seed-sp500', 'sp500_index')


def seed_sp500_postgres(conn=None):
    if conn is None:
        conn = get_db()
    # conn = get_db()
    seeder = SP500Seeder(conn)

    seeder.seed_companies(sp500_companies)
    seeder.seed_stocks(sp500_stocks)

    seeder.seed_index(sp500_index)  
    seeder.close()

def seed_sp500_sqlite(conn=None, db_path=sp500_p1_sqlite):
    conn = sqlite3.connect(db_path, uri=True)
    seeder = SP500Seeder(conn)

    seeder.seed_companies(sp500_companies)
    seeder.seed_stocks(sp500_stocks)
    seeder.seed_index(sp500_index)

    seeder.close()





#------------------------------------------------------------------------------------------------------------------------#    
# data selction notes:    
# select columns matching model: 
    # convert csv:    
    # sp500_companies.csv:[Exchange,Symbol,Shortname,Longname,Sector,Industry,Currentprice,Marketcap,Ebitda,Revenuegrowth,City,State,Country,Fulltimeemployees,Longbusinesssummary,Weight]
    # [NMS,MSFT,Microsoft Corporation,Microsoft Corporation,Technology,Software - Infrastructure,404.06,3002343620608,118427000832,0.176,Redmond,WA,United States,221000,"Microsoft Corporation develops and supports software, services, devices and solutions worldwide. The Productivity and Business Processes segment offers office, exchange, SharePoint, Microsoft Teams, office 365 Security and Compliance, Microsoft viva, and Microsoft 365 copilot; and office consumer services, such as Microsoft 365 consumer subscriptions, Office licensed on-premises, and other office services. This segment also provides LinkedIn; and dynamics business solutions, including Dynamics 365, a set of intelligent, cloud-based applications across ERP, CRM, power apps, and power automate; and on-premises ERP and CRM applications. The Intelligent Cloud segment offers server products and cloud services, such as azure and other cloud services; SQL and windows server, visual studio, system center, and related client access licenses, as well as nuance and GitHub; and enterprise services including enterprise support services, industry solutions, and nuance professional services. The More Personal Computing segment offers Windows, including windows OEM licensing and other non-volume licensing of the Windows operating system; Windows commercial comprising volume licensing of the Windows operating system, windows cloud services, and other Windows commercial offerings; patent licensing; and windows Internet of Things; and devices, such as surface, HoloLens, and PC accessories. Additionally, this segment provides gaming, which includes Xbox hardware and content, and first- and third-party content; Xbox game pass and other subscriptions, cloud gaming, advertising, third-party disc royalties, and other cloud services; and search and news advertising, which includes Bing, Microsoft News and Edge, and third-party affiliates. The company sells its products through OEMs, distributors, and resellers; and directly through digital marketplaces, online, and retail stores. The company was founded in 1975 and is headquartered in Redmond, Washington.",0.06467215622566934]
    # to model:
    # company.py:['company_id', 'name', 'ticker_symbol', 'industry_id', 'sector_id', 'exchange_id', 'location_id', 'cik', 'isEtf', 'isActivelyTrading']
    
    # sp500_stocks.csv: [Date,Symbol,Adj Close,Close,High,Low,Open,Volume]
    # [2010-01-04,MMM,53.2953987121582,83.0199966430664,83.44999694824219,82.66999816894531,83.08999633789062,3043700]
    # stock.py:['stock_id', 'company_id', 'date', 'open_price', 'high_price', 'low_price', 'close_price', 'adjusted_close_price', 'volume']
    
    # sp500_index.csv: [Date,S&P500]
    # [2014-02-18,1840.76]
    # stock_market_index.py:['index_id', 'name', 'symbol', 'exchange_id', 'description']

