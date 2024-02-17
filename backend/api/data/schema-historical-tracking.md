
### Historical Companies Data

for future implementation, each historical table:

- `effective_date` is the timestamp when the change occurred.
- `operation_type` indicates the type of operation that was performed on the data ('INSERT', 'UPDATE', 'DELETE').

These historical tables allow us to track changes over time for each entity in the database. also need to implement triggers or application logic to populate these historical tables whenever changes are made to the main tables.


```sql
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
    effective_date TIMESTAMP NOT NULL,
    operation_type VARCHAR(10) NOT NULL CHECK (operation_type IN ('INSERT', 'UPDATE', 'DELETE'))
);
```

### Historical Financials Data

```sql
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
```

### Historical Prices Data

```sql
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
```

### Historical ETF Holdings Data

```sql
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
```

