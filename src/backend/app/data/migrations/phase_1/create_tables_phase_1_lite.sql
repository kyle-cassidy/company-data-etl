CREATE TABLE IF NOT EXISTS sp_500_companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exchange TEXT NOT NULL,
    symbol TEXT NOT NULL,
    short_name TEXT,
    long_name TEXT,
    sector TEXT,
    industry TEXT,
    current_price REAL,
    market_cap REAL,
    ebitda REAL,
    revenue_growth REAL,
    city TEXT,
    state TEXT,
    country TEXT,
    long_business_summary TEXT,
    weight REAL
);

CREATE TABLE IF NOT EXISTS sp_500_stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    symbol TEXT NOT NULL,
    adj_close REAL,
    close REAL,
    high REAL,
    low REAL,
    open REAL,
    volume TEXT
);

CREATE TABLE IF NOT EXISTS sp_500_index_levels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL, 
    index_level REAL,
    index_name TEXT NOT NULL
);

-- CREATE TABLE income_statements (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     company_id INTEGER,
--     period TEXT NOT NULL, -- SQLite uses TEXT for dates
--     revenue REAL,
--     net_income REAL,
--     eps REAL,
--     reported_currency TEXT,
--     FOREIGN KEY(company_id) REFERENCES sp_500_companies(id)
-- );

-- CREATE TABLE balance_sheets (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     company_id INTEGER,
--     period TEXT NOT NULL, -- SQLite uses TEXT for dates
--     total_debt REAL,
--     total_equity REAL,
--     reported_currency TEXT,
--     FOREIGN KEY(company_id) REFERENCES sp_500_companies(id)
-- );

-- CREATE TABLE cashflow_statements (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     company_id INTEGER,
--     period TEXT NOT NULL, -- SQLite uses TEXT for dates
--     net_operating_cashflow REAL,
--     net_investing_cashflow REAL,
--     net_financing_cashflow REAL,
--     net_change_in_cash REAL,
--     reported_currency TEXT,
--     FOREIGN KEY(company_id) REFERENCES sp_500_companies(id)
-- );
