
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
