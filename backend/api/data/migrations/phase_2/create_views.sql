
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

