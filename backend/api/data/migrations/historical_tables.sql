

-- historical_companies_data
-- These historical tables allow us to track changes over time for each entity in the database. also need to implement triggers or application logic to populate these historical tables whenever changes are made to the main tables.

-- historical_companies_data
CREATE TABLE historical_companies (
    historical_company_id SERIAL PRIMARY KEY,
    company_id INT NOT NULL REFERENCES companies(company_id),
    name VARCHAR(255) NOT NULL,
    ticker_symbol VARCHAR(10) NOT NULL,
    industry_id INT REFERENCES industries(industry_id),
    sector_id INT REFERENCES sectors(sector_id),
    exchange_id INT REFERENCES exchanges(exchange_id),
    country_id INT REFERENCES countries(country_id),
    cik VARCHAR(255),
    is_etf BOOLEAN,
    is_actively_trading BOOLEAN,
    effective_date TIMESTAMP NOT NULL, -- `effective_date` is the timestamp when the change occurred.
    operation_type VARCHAR(10) NOT NULL CHECK (operation_type IN ('INSERT', 'UPDATE', 'DELETE')), -- `operation_type` indicates the type of operation that was performed on the data ('INSERT', 'UPDATE', 'DELETE').    
    reason TEXT, -- Reason for the operation
    snapshot JSONB -- Snapshot of the data before the operation
);

 -- historical_financials_data
CREATE TABLE historical_financials (
    historical_financial_id SERIAL PRIMARY KEY,
    financial_id INT NOT NULL REFERENCES financials(financial_id),
    company_id INT NOT NULL REFERENCES companies(company_id),
    period DATE NOT NULL,
    revenue DECIMAL(15,2),
    net_income DECIMAL(15,2),
    eps DECIMAL(10,2),
    total_debt DECIMAL(15,2),
    total_equity DECIMAL(15,2),
    reported_currency VARCHAR(10),
    effective_date TIMESTAMP NOT NULL,
    operation_type VARCHAR(10) NOT NULL CHECK (operation_type IN ('INSERT', 'UPDATE', 'DELETE'))
);

 -- historical_prices_data
CREATE TABLE historical_prices (
    historical_price_id SERIAL PRIMARY KEY,
    price_id INT NOT NULL REFERENCES prices(price_id),
    company_id INT NOT NULL REFERENCES companies(company_id),
    date DATE NOT NULL,
    open_price DECIMAL(10,2),
    high_price DECIMAL(10,2),
    low_price DECIMAL(10,2),
    close_price DECIMAL(10,2),
    adjusted_close_price DECIMAL(10,2),
    volume BIGINT,
    effective_date TIMESTAMP NOT NULL,
    operation_type VARCHAR(10) NOT NULL CHECK (operation_type IN ('INSERT', 'UPDATE', 'DELETE'))
);

-- historical_etf_holdings_data
CREATE TABLE historical_etf_holdings (
    historical_etf_holding_id SERIAL PRIMARY KEY,
    etf_holding_id INT NOT NULL REFERENCES etf_holdings(etf_holding_id),
    etf_company_id INT NOT NULL REFERENCES companies(company_id),
    holding_date DATE NOT NULL,
    holding_company_id INT NOT NULL REFERENCES companies(company_id),
    shares BIGINT,
    weight DECIMAL(5,2),
    effective_date TIMESTAMP NOT NULL,
    operation_type VARCHAR(10) NOT NULL CHECK (operation_type IN ('INSERT', 'UPDATE', 'DELETE'))
);
