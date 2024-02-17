
# fact / dimension

In a data warehouse context, tables are often categorized as either fact tables or dimension tables. Fact tables contain the quantitative metrics or measurements of a business process, while dimension tables contain descriptive attributes related to the fact data that provide context.

### Fact Tables

- **Financials**: Contains financial performance metrics like revenue and net income. It's a fact table that can be used to assess a company's financial health and growth over time, which is crucial for investment decisions.
- **Prices**: Tracks historical stock prices. As a fact table, it's essential for technical analysis and understanding market trends.
- **ETFHoldings**: Lists the assets held by an ETF. It's a fact table that can show the diversification and investment strategy of the ETF.
- **Ownership**: Details about shareholders. This fact table can indicate the confidence of investors in the company's management and future.
- **AnalystRatings**: Contains opinions of financial analysts. As a fact table, it provides insights into market sentiment and potential investment risks or opportunities.
- **TechnicalIndicators**: Stores calculated indicators like SMA, EMA, etc. This fact table is used for technical analysis to predict stock price movements.
- **ESGData**: Holds ESG ratings which can be a fact table used to evaluate a company's ethical impact and sustainability, increasingly important for modern investors.
- **InsiderTransactions**: Records transactions by company insiders. This fact table can signal insider confidence in the company's future prospects.

### Dimension Tables

- **Companies**: Describes companies with attributes like name, ticker symbol, and industry. It's a dimension table that provides context to almost all fact tables.
- **Exchanges**: Contains details about stock exchanges. As a dimension table, it gives context to trading data and can indicate the regulatory environment a company operates in.
- **Countries**: Holds country-specific information. This dimension table can be used for regional analysis and geopolitical risk assessment.
- **Industries** and **Sectors**: Classify companies into industries and sectors. These dimension tables help in performing industry-specific analysis and diversification strategies.
- **MarketIndexes**: Describes major market indices. As a dimension table, it provides a benchmark for comparing company performance.

### Notes on Investment Worthiness

- **Financials**: A key table for fundamental analysis. Investors look at trends in revenue, net income, and EPS to gauge a company's profitability and growth potential.
- **Prices**: Essential for assessing historical performance and volatility. Price trends and patterns can inform buy or sell decisions.
- **Ownership**: Large stakes held by institutional investors or significant insider ownership can be positive indicators of a company's investment worthiness.
- **AnalystRatings**: Positive ratings can influence market perception and indicate a consensus on a company's prospects.
- **TechnicalIndicators**: Used to time the market and identify entry and exit points based on price movements and momentum.
- **ESGData**: Increasingly important as investors seek to invest in companies with responsible practices.
- **InsiderTransactions**: Buying trends by insiders can signal their belief in the company's future success, while selling might raise red flags.

Each table provides a different lens through which to assess investment worthiness. Fact tables often provide the data needed to perform various analyses, while dimension tables offer the descriptive context that allows for a deeper understanding of what the facts represent.

# categories


### Company and Market Data
- **Companies**: Details about individual companies.
- **Exchanges**: Information on stock exchanges where companies are listed.
- **Countries**: Country-specific information.
- **Industries**: Industry classifications.
- **Sectors**: Sector classifications.
- **MarketIndexes**: Information on major market indices.
- **ETFInformation**: Details about Exchange-Traded Funds (ETFs).
- **ETFSectorWeightings**: Sector weightings within ETFs.

### Financial Data
- **Financials**: Financial statements and metrics of companies.
- **Prices**: Historical stock price data.
- **Ownership**: Shareholder information.
- **AnalystRatings**: Analyst ratings for companies.
- **EconomicData**: Broader economic data points.
- **EconomicIndicators**: Specific indicators of economic performance.
- **TreasuryRates**: Interest rates on government securities.

### Investment and Trading Data
- **ETFSectorWeightings**: Weightings of sectors within ETFs.
- **ETFSectorWeightings**: Weightings of sectors within ETFs.
- **ETFHoldings**: Holdings within an ETF.
- **MutualFundHoldings**: Holdings within mutual funds.
- **InsiderTransactions**: Transactions by company insiders.
- **SenateTrading**: Trading activities by senators.
- **HouseDisclosure**: Financial disclosures by house representatives.

### Analytical Data
- **TechnicalIndicators**: Technical indicators for stocks.
- **ESGData**: Environmental, Social, and Governance ratings.
- **AnalystEstimates**: Future earnings and revenue estimates by analysts.
- **AnalystRecommendations**: Buy, sell, or hold recommendations from analysts.

### Event and News Data
- **StockNewsSentiment**: Sentiment analysis of news articles.
- **IPOCalendar**: Information on upcoming Initial Public Offerings.
- **MergersAcquisitions**: Details of M&A activities.
- **Dividends**: Dividend payouts.
- **StockSplits**: Stock split events.

### Additional Data
- **CompanyOutlook**: Overall outlook and profiles of companies.
- **StockPeers**: Information on peer companies in the same industry.
- **MarketPerformance**: Performance data of different market segments.
- **RevenueSegmentation**: Revenue breakdown by product or geography.
- **Fundamentals**: Fundamental financial data aggregating income, cash flow, and balance sheet information.
- **StockList**: List of stocks and their trading status.
- **CommitmentOfTradersReport**: Futures market positions.
- **EconomicCalendar**: Scheduled economic events.
- **MarketRiskPremium**: Risk premium data for different markets.
- **Constituents**: Constituent companies of market indices.
