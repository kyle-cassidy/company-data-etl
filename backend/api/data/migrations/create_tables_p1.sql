


CREATE TABLE sectors (
    sector_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE industries (
    industry_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    sector_id INT REFERENCES sectors(sector_id),
    description TEXT
);
CREATE TABLE exchanges (
    exchange_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    short_name VARCHAR(255),
);

CREATE TABLE companies (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ticker_symbol VARCHAR(10) UNIQUE NOT NULL,
    industry_id INT REFERENCES industries(industry_id),
    sector_id INT REFERENCES sectors(sector_id),
    exchange_id INT REFERENCES exchanges(exchange_id),
    location_id INT REFERENCES locations(location_id),
    cik CHAR(10) UNIQUE,
    is_etf BOOLEAN,
    is_actively_trading BOOLEAN
);

CREATE TABLE income_statements (
    income_statement_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(company_id),
    period DATE NOT NULL,
    revenue DECIMAL(15,2),
    net_income DECIMAL(15,2),
    eps DECIMAL(10,2),
    reported_currency VARCHAR(10)
);

CREATE TABLE balance_sheets (
    balance_sheet_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(company_id),
    period DATE NOT NULL,
    total_debt DECIMAL(15,2),
    total_equity DECIMAL(15,2),
    reported_currency VARCHAR(10)
);

CREATE TABLE cashflow_statements (
    cashflow_statement_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(company_id),
    period DATE NOT NULL,
    net_operating_cashflow DECIMAL(15,2),
    net_investing_cashflow DECIMAL(15,2),
    net_financing_cashflow DECIMAL(15,2),
    net_change_in_cash DECIMAL(15,2),
    reported_currency VARCHAR(10)
);

CREATE TABLE stocks (
    stock_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(company_id),
    date DATE NOT NULL,
    open_price DECIMAL(10,2),
    high_price DECIMAL(10,2),
    low_price DECIMAL(10,2),
    close_price DECIMAL(10,2),
    adjusted_close_price DECIMAL(10,2),
    volume BIGINT
);

CREATE TABLE ownership (
    ownership_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(company_id),
    holder_name VARCHAR(255),
    shares_held BIGINT,
    date DATE NOT NULL
);

CREATE TABLE analyst_ratings (
    rating_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(company_id),
    analyst_name VARCHAR(255),
    rating VARCHAR(255),
    date DATE NOT NULL
);

CREATE TABLE stock_market_indexes (
    index_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    symbol VARCHAR(10) UNIQUE NOT NULL,
    exchange_id INT REFERENCES exchanges(exchange_id),
    description TEXT
);

CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country_id INT REFERENCES countries(country_id),
    state_id INT REFERENCES states(state_id),
    city_id INT REFERENCES cities(city_id),
    zip_code VARCHAR(10),
    address TEXT
);

CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE states (
    state_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country_id INT REFERENCES countries(country_id)
);

CREATE TABLE cities (
    city_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    state_id INT REFERENCES states(state_id)
);

CREATE TABLE zip_codes (
    zip_code_id SERIAL PRIMARY KEY,
    zip_code VARCHAR(10) NOT NULL,
    city_id INT REFERENCES cities(city_id)
);


-- Indexes
-- indexes work in the background to speed up the retrieval of rows by providing quick access paths to data.

CREATE INDEX idx_prices_company_id ON stocks(company_id);
CREATE INDEX idx_ownership_company_id ON ownership(company_id);
CREATE INDEX idx_income_statements_company_id ON income_statements(company_id);
CREATE INDEX idx_balance_sheets_company_id ON balance_sheets(company_id);
CREATE INDEX idx_cashflow_statements_company_id ON cashflow_statements(company_id);
CREATE INDEX idx_analyst_ratings_company_id ON analyst_ratings(company_id);
CREATE INDEX idx_stock_market_indexes_exchange_id ON stock_market_indexes(exchange_id);


