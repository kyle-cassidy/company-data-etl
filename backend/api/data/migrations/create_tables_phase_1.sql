
CREATE TABLE sp_500_companies (
    id SERIAL PRIMARY KEY,
    exchange VARCHAR(255) NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    short_name VARCHAR(255),
    long_name VARCHAR(255),
    sector VARCHAR(255),
    industry VARCHAR(255),
    current_price DECIMAL(15,2),
    market_cap DECIMAL(15,2),
    ebitda DECIMAL(15,2),
    revenue_growth DECIMAL(10,2),
    city VARCHAR(255),
    state VARCHAR(255),
    country VARCHAR(255),
    long_business_summary TEXT,
    weight DECIMAL(10,2)
);

CREATE TABLE sp_500_stocks (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    adj_close DECIMAL(15,2),
    close DECIMAL(15,2),
    high DECIMAL(15,2),
    low DECIMAL(15,2),
    open DECIMAL(15,2),
    volume VARCHAR(255)
);

CREATE TABLE sp_500_index_levels (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    index_level DECIMAL(15,2),
    index_name VARCHAR(255) NOT NULL
);

-- CREATE TABLE income_statements (
--     id SERIAL PRIMARY KEY,
--     company_id INT REFERENCES companies(id),
--     period DATE NOT NULL,
--     revenue DECIMAL(15,2),
--     net_income DECIMAL(15,2),
--     eps DECIMAL(10,2),
--     reported_currency VARCHAR(10)
-- );

-- CREATE TABLE balance_sheets (
--     id SERIAL PRIMARY KEY,
--     company_id INT REFERENCES companies(id),
--     period DATE NOT NULL,
--     total_debt DECIMAL(15,2),
--     total_equity DECIMAL(15,2),
--     reported_currency VARCHAR(10)
-- );

-- CREATE TABLE cashflow_statements (
--     id SERIAL PRIMARY KEY,
--     company_id INT REFERENCES companies(id),
--     period DATE NOT NULL,
--     net_operating_cashflow DECIMAL(15,2),
--     net_investing_cashflow DECIMAL(15,2),
--     net_financing_cashflow DECIMAL(15,2),
--     net_change_in_cash DECIMAL(15,2),
--     reported_currency VARCHAR(10)
-- );