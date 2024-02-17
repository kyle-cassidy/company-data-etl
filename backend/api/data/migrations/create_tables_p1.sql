
CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE industries (
    industry_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE sectors (
    sector_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE exchanges (
    exchange_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    short_name VARCHAR(255),
    country_id INT REFERENCES countries(country_id)
);

CREATE TABLE companies (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ticker_symbol VARCHAR(10) UNIQUE NOT NULL,
    industry_id INT REFERENCES industries(industry_id),
    sector_id INT REFERENCES sectors(sector_id),
    exchange_id INT REFERENCES exchanges(exchange_id),
    country_id INT REFERENCES countries(country_id),
    cik VARCHAR(255) UNIQUE,
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

CREATE TABLE statement_of_cashflows (
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
    price_id SERIAL PRIMARY KEY,
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


-- Indexes
-- indexes work in the background to speed up the retrieval of rows by providing quick access paths to data.

CREATE INDEX idx_prices_company_id ON stocks(company_id);
CREATE INDEX idx_companies_country_id ON companies(country_id);
CREATE INDEX idx_ownership_company_id ON ownership(company_id);

CREATE INDEX idx_income_statements_company_id ON income_statements(company_id);
CREATE INDEX idx_balance_sheets_company_id ON balance_sheets(company_id);
CREATE INDEX idx_statement_of_cashflows_company_id ON statement_of_cashflows(company_id);

CREATE INDEX idx_analyst_ratings_company_id ON analyst_ratings(company_id);


-- Create views for dynamic retrieval of the latest financials

-- income_statements
CREATE VIEW latest_income_statements AS
SELECT i.*
FROM income_statements i
INNER JOIN (
    SELECT company_id, MAX(period) as latest_period
    FROM income_statements
    GROUP BY company_id
) latest ON i.company_id = latest.company_id AND i.period = latest.latest_period;

-- balance_sheets
CREATE VIEW latest_balance_sheets AS
SELECT b.*
FROM balance_sheets b
INNER JOIN (
    SELECT company_id, MAX(period) as latest_period
    FROM balance_sheets
    GROUP BY company_id
) latest ON b.company_id = latest.company_id AND b.period = latest.latest_period;

-- statement_of_cashflows
CREATE VIEW latest_statement_of_cashflows AS
SELECT c.*
FROM statement_of_cashflows c
INNER JOIN (
    SELECT company_id, MAX(period) as latest_period
    FROM statement_of_cashflows
    GROUP BY company_id
) latest ON c.company_id = latest.company_id AND c.period = latest.latest_period;

-- combined_financial_statements 
CREATE VIEW combined_financial_statements AS
SELECT
    c.company_id,
    c.name AS company_name,
    i.period,
    i.revenue,
    i.net_income,
    i.eps,
    b.total_debt,
    b.total_equity,
    cf.net_operating_cashflow,
    cf.net_investing_cashflow,
    cf.net_financing_cashflow,
    cf.net_change_in_cash,
    i.reported_currency
FROM
    companies c
JOIN income_statements i ON c.company_id = i.company_id
JOIN balance_sheets b ON c.company_id = b.company_id AND i.period = b.period
JOIN statement_of_cashflows cf ON c.company_id = cf.company_id AND i.period = cf.period;

