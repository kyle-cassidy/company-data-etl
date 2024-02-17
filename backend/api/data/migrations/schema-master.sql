
CREATE TABLE Countries (
    country_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Industries (
    industry_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE Sectors (
    sector_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Exchanges (
    exchange_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    shortName VARCHAR(255),
    country_id INT REFERENCES Countries(country_id)
);

CREATE TABLE Companies (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ticker_symbol VARCHAR(10) UNIQUE NOT NULL,
    industry_id INT REFERENCES Industries(industry_id),
    sector_id INT REFERENCES Sectors(sector_id),
    exchange_id INT REFERENCES Exchanges(exchange_id),
    country_id INT REFERENCES Countries(country_id),
    cik VARCHAR(255) UNIQUE,
    isEtf BOOLEAN,
    isActivelyTrading BOOLEAN
);

CREATE TABLE Financials (
    financial_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES Companies(company_id),
    period DATE NOT NULL,
    revenue DECIMAL(15,2),
    net_income DECIMAL(15,2),
    eps DECIMAL(10,2),
    total_debt DECIMAL(15,2),
    total_equity DECIMAL(15,2),
    reported_currency VARCHAR(10)
);

CREATE TABLE Prices (
    price_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES Companies(company_id),
    date DATE NOT NULL,
    open_price DECIMAL(10,2),
    high_price DECIMAL(10,2),
    low_price DECIMAL(10,2),
    close_price DECIMAL(10,2),
    adjusted_close_price DECIMAL(10,2),
    volume BIGINT
);

CREATE TABLE Ownership (
    ownership_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES Companies(company_id),
    holder_name VARCHAR(255),
    shares_held BIGINT,
    date DATE NOT NULL
);

CREATE TABLE AnalystRatings (
    rating_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES Companies(company_id),
    analyst_name VARCHAR(255),
    rating VARCHAR(255),
    date DATE NOT NULL
);

CREATE TABLE ETFHoldings (
    etf_holding_id SERIAL PRIMARY KEY,
    etf_company_id INT REFERENCES Companies(company_id),
    holding_date DATE NOT NULL,
    holding_company_id INT REFERENCES Companies(company_id),
    shares BIGINT,
    weight DECIMAL(5,2)
);

CREATE TABLE TechnicalIndicators (
    indicator_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES Companies(company_id),
    date DATE NOT NULL,
    sma DECIMAL(10,2),
    ema DECIMAL(10,2),
    rsi DECIMAL(5,2),
    adx DECIMAL(5,2),
    standard_deviation DECIMAL(5,2)
);

CREATE TABLE EconomicData (
    economic_data_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    value DECIMAL(15,2),
    date DATE NOT NULL
);

CREATE TABLE EconomicIndicators (
    indicator_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    value DECIMAL(15,2),
    date DATE NOT NULL
);

CREATE TABLE MarketIndexes (
    index_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    price DECIMAL(15,2),
    date DATE NOT NULL
);

CREATE TABLE ESGData (
    esg_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES Companies(company_id),
    rating DECIMAL(5,2),
    date DATE NOT NULL
);

CREATE TABLE StockNewsSentiment (
    sentiment_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES Companies(company_id),
    date DATE NOT NULL,
    sentiment_score DECIMAL(5,2)
);

CREATE TABLE InsiderTransactions (
    transaction_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES Companies(company_id),
    insider_name VARCHAR(255),
    transaction_type VARCHAR(255),
    shares BIGINT,
    date DATE NOT NULL
);

CREATE TABLE StockOwnership (
    ownership_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES Companies(company_id),
    holder_id INT,
    shares_held BIGINT,
    date DATE NOT NULL
);

CREATE TABLE ETFInformation (
    etf_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    expense_ratio DECIMAL(5,2),
    assets_under_management DECIMAL(15,2),
    date DATE NOT NULL
);

CREATE TABLE ETFSectorWeightings (
    weighting_id SERIAL PRIMARY KEY,
    etf_id INT REFERENCES ETFInformation(etf_id),
    sector_id
);

-- Historical Companies Data

-- These historical tables allow us to track changes over time for each entity in the database. also need to implement triggers or application logic to populate these historical tables whenever changes are made to the main tables.

CREATE TABLE HistoricalCompanies (
    historical_company_id SERIAL PRIMARY KEY,
    company_id INT NOT NULL REFERENCES Companies(company_id),
    name VARCHAR(255) NOT NULL,
    ticker_symbol VARCHAR(10) NOT NULL,
    industry_id INT REFERENCES Industries(industry_id),
    sector_id INT REFERENCES Sectors(sector_id),
    exchange_id INT REFERENCES Exchanges(exchange_id),
    country_id INT REFERENCES Countries(country_id),
    cik VARCHAR(255),
    isEtf BOOLEAN,
    isActivelyTrading BOOLEAN,
    effective_date TIMESTAMP NOT NULL, -- `effective_date` is the timestamp when the change occurred.
    operation_type VARCHAR(10) NOT NULL CHECK (operation_type IN ('INSERT', 'UPDATE', 'DELETE')), -- `operation_type` indicates the type of operation that was performed on the data ('INSERT', 'UPDATE', 'DELETE').    
    reason TEXT, -- Reason for the operation
    snapshot JSONB -- Snapshot of the data before the operation
);

 -- Historical Financials Data


CREATE TABLE HistoricalFinancials (
    historical_financial_id SERIAL PRIMARY KEY,
    financial_id INT NOT NULL REFERENCES Financials(financial_id),
    company_id INT NOT NULL REFERENCES Companies(company_id),
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

 -- Historical Prices Data

CREATE TABLE HistoricalPrices (
    historical_price_id SERIAL PRIMARY KEY,
    price_id INT NOT NULL REFERENCES Prices(price_id),
    company_id INT NOT NULL REFERENCES Companies(company_id),
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

--Historical ETF Holdings Data

CREATE TABLE HistoricalETFHoldings (
    historical_etf_holding_id SERIAL PRIMARY KEY,
    etf_holding_id INT NOT NULL REFERENCES ETFHoldings(etf_holding_id),
    etf_company_id INT NOT NULL REFERENCES Companies(company_id),
    holding_date DATE NOT NULL,
    holding_company_id INT NOT NULL REFERENCES Companies(company_id),
    shares BIGINT,
    weight DECIMAL(5,2),
    effective_date TIMESTAMP NOT NULL,
    operation_type VARCHAR(10) NOT NULL CHECK (operation_type IN ('INSERT', 'UPDATE', 'DELETE'))
);

