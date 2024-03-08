import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error
import sqlite3
import os
import json


import os
import requests

# localhost API URL: src/backend/.flaskenv
API_URL = os.getenv('API_URL', 'http://127.0.0.1:80')

# API endpoints
COMPANIES_URL = f'{API_URL}/companies'
COMPANY_SYMBOL_URL = f'{API_URL}/companies/symbol/'
COMPANY_ID_URL = f'{API_URL}/companies/id/'
STOCKS_URL = f'{API_URL}/stocks'
INDEX_URL = f'{API_URL}/index_levels'


st.title("Public Company Insights")

# Connect to the database via API
def get_json(URL):
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()

companies_json = get_json(COMPANIES_URL)
index_json = get_json(INDEX_URL)
stocks_json = get_json(STOCKS_URL)

try:
    # companies = requests.get(COMPANIES_URL)
    # companies.raise_for_status()
    # companies_json = companies.json()
    st.write(companies_json)
except requests.exceptions.RequestException as e:
    st.write(e)



#TODO - pull out functions to a separate file


### DB Connection
# testing connection
# sp500_p1_sqlite = os.path.join(os.path.dirname(__file__), '..', 'backend', 'app', 'data', 'sp500_p1_sm.sqlite')
# conn = sqlite3.connect(sp500_p1_sqlite)
# cursor = conn.cursor()

# # Function to display information about a dataframe
# def information(df_name, df):
#     st.write(f"Information about {df_name}")
#     st.write("Column Data")
#     st.dataframe(df.info())
#     st.write("Sample Data")
#     st.dataframe(df.head(2))
#     df_null = round(df.isna().sum() / df.isna().count() * 100, 2).sort_values(ascending=False)
#     st.write("Null values are")
#     st.dataframe(df_null)
#     df.dropna(inplace=True)

# # Load data from the database
# @st.cache_data
# def load_data():
#     companies_query = "SELECT * FROM sp_500_companies"
#     sp_500_comp = pd.read_sql_query(companies_query, conn)
#     index_query = "SELECT * FROM sp_500_index_levels;"
#     sp_500_index = pd.read_sql_query(index_query, conn)
#     stocks_query = "SELECT * FROM SP_500_stocks;"
#     sp_500_stocks = pd.read_sql_query(stocks_query, conn)
#     return sp_500_comp, sp_500_index, sp_500_stocks

# sp_500_comp, sp_500_index, sp_500_stocks = load_data()

# # Display table schemas
# if st.button('Show Table Schemas'):
#     cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#     st.write(cursor.fetchall())
# ### End DB Connection

# Financial statements CSV data
# balanceSheetHistory_quarterly = pd.read_csv("./backend/api/data/seed/sp500/balanceSheetHistory_quarterly.csv")
# balanceSheetHistory_annually = pd.read_csv("./backend/api/data/seed/sp500/balanceSheetHistory_annually.csv")
# incomeStatementHistory_quarterly = pd.read_csv("./backend/api/data/seed/sp500/incomeStatementHistory_quarterly.csv")
# incomeStatementHistory_annually = pd.read_csv("./backend/api/data/seed/sp500/incomeStatementHistory_annually.csv")
# cashflowStatement_quarterly = pd.read_csv("./backend/api/data/seed/sp500/cashflowStatement_quarterly.csv")
# cashflowStatement_annually = pd.read_csv("./backend/api/data/seed/sp500/cashflowStatement_annually.csv")

sp_500_comp = pd.read_json(json.dumps(companies_json))
sp_500_index = pd.read_json(json.dumps(index_json))
sp_500_stocks = pd.read_json(json.dumps(stocks_json))

# Display head of dataframes
st.write("S&P 500 Companies")
st.dataframe(sp_500_comp.head())
st.write("S&P 500 Index Levels")
st.dataframe(sp_500_index.head())
st.write("S&P 500 Stocks")
st.dataframe(sp_500_stocks.head())


# Analyzing Public Companies
# Changing market_cap and EBITDA to billion values % Weight to percentage
sp_500_comp['market_cap'] = round(sp_500_comp['market_cap'] / 1e9, 2)
sp_500_comp['ebitda'] = round(sp_500_comp['ebitda'] / 1e9, 2)
sp_500_comp['weight'] = round(sp_500_comp['weight'] * 100, 2)

# Analysis and plots will be added in the following sections

# Breakdown of Sectors in S&P 500
st.markdown("## Breakdown of Sectors in S&P 500")
st.markdown("### Technology, industrials, health services, and financial services make up over half of the S&P 500")
sp_sec_brk = sp_500_comp.groupby(by='sector')['symbol'].apply(lambda x: round(x.count() / len(sp_500_comp) * 100, 2)).reset_index().sort_values(by='symbol', ascending=False)
fig, ax = plt.subplots(figsize=(10,8))
ax = sns.barplot(data=sp_sec_brk, x='sector', y='symbol')
ax.bar_label(ax.containers[0], fmt='%.0f%%')
plt.xticks(rotation=85)
plt.title("Breakdown of Sectors in S&P 500 (in %)\n")
ax.set_ylabel("Percentage")
st.pyplot(fig)

# Tech Companies Dominate S&P 500 by Market Cap
st.markdown("### Tech Companies Dominate S&P 500 by Market Cap")
estimators=['market_cap','weight']
color={'market_cap':'Blues_r','weight':'Oranges_r'}
for est in estimators:
    fig, ax = plt.subplots()
    sns.barplot(data=sp_500_comp.sort_values(by=est, ascending=False).head(10),y=est,x="symbol", palette=color[est])
    plt.xticks(rotation=45)
    plt.title("Tech Companies Dominate S&P 500 {}".format(est.replace("_", " ").title()))
    st.pyplot(fig)

# Additional Market Cap Analysis
st.markdown("#### Additional Market Cap Analysis")
top_comp_mkt_cap = sp_500_comp[['symbol', 'current_price', 'market_cap', 'ebitda', 'revenue_growth', 'weight']].sort_values(by='market_cap', ascending=False).head(10)
st.dataframe(top_comp_mkt_cap)

# Correlation Matrix
st.markdown("### Size and profitability of a company are closely linked to its weight")
st.markdown("Current price and revenue growth are not strongly connected to these factors.")
correlation_matrix = sp_500_comp[['current_price', 'market_cap', 'ebitda', 'revenue_growth', 'weight']].corr()
fig, ax = plt.subplots()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Profitability is correlated to weight')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
st.pyplot(fig)

# Top 5 Companies in Top 3 Industries of Top 5 Sectors
st.markdown("## Top 5 Companies in Top 3 Industries of Top 5 Sectors")
# The implementation of this section will require additional functions and logic to be adapted from the analysis_sqlite.py notebook.
# This will be implemented in the following updates.

# Number of companies for each exchange
st.markdown("### Number of companies for each exchange")
exchange_counts = sp_500_comp['exchange'].value_counts()
fig, ax = plt.subplots()
ax.pie(exchange_counts, labels=exchange_counts.index, autopct='%.2f%%')
plt.tight_layout()
st.pyplot(fig)

