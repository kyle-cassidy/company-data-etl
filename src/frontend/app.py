import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error
import json
import requests
import os
from dashboard.view_functions import (
    set_config,
    # set_title,
    display_message_history,
    display_chatbox_and_store_questions,
    submit_prompt_display_result,
    # launch_bot_api_key,
    # sidebar_chatbot,
    launch_chatbot,
    chatbot,
    assign_chat_engine,
    assign_messages,
)

# TODO - pull out analysis functions to a separate file


set_config(st)
st.title("Public Company Insights: S&P 500")
st.markdown("Note: the chatbot in the left sidebar is under active development.")

# API URL from flask backend api service
API_URL = os.getenv("API_URL", "http://backend:8000/")

# API endpoints
COMPANIES_URL = f"{API_URL}/companies"
COMPANY_SYMBOL_URL = f"{API_URL}/companies/symbol/"
COMPANY_ID_URL = f"{API_URL}/companies/id/"
STOCKS_URL = f"{API_URL}/stocks"
INDEX_URL = f"{API_URL}/index_levels"


# st.title("Public Company Insights")
# subtitle
st.markdown("## Industry Analysis on the S&P 500")


# Connect to the database via API
def get_json(URL):
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()
    # try:
    #     response = requests.post(URL)
    #     response.raise_for_status()
    #     return response.json()

    except requests.exceptions.HTTPError as err:
        raise SystemExit(err) from err


companies_json = get_json(COMPANIES_URL)
index_json = get_json(INDEX_URL)
stocks_json = get_json(STOCKS_URL)

# convert json to pandas dataframe
sp_500_comp = pd.read_json(json.dumps(companies_json))
sp_500_index = pd.read_json(json.dumps(index_json))
sp_500_stocks = pd.read_json(json.dumps(stocks_json))


# Analyzing Public Companies
# Changing market_cap and EBITDA to billion values % Weight to percentage
sp_500_comp["market_cap"] = round(sp_500_comp["market_cap"] / 1e9, 2)
sp_500_comp["ebitda"] = round(sp_500_comp["ebitda"] / 1e9, 2)
sp_500_comp["weight"] = round(sp_500_comp["weight"] * 100, 2)

# Analysis and plots will be added in the following sections

# Breakdown of Sectors in S&P 500
st.markdown(
    "### Technology, industrials, health services, and financial services make up over half of the S&P 500"
)
sp_sec_brk = (
    sp_500_comp.groupby(by="sector")["symbol"]
    .apply(lambda x: round(x.count() / len(sp_500_comp) * 100, 2))
    .reset_index()
    .sort_values(by="symbol", ascending=False)
)
fig, ax = plt.subplots(figsize=(10, 8))
ax = sns.barplot(data=sp_sec_brk, x="sector", y="symbol")
ax.bar_label(ax.containers[0], fmt="%.0f%%")
plt.xticks(rotation=85)
plt.title("Breakdown of Sectors in S&P 500 (in %)\n")
ax.set_ylabel("Percentage")
st.pyplot(fig)

# Tech Companies Dominate S&P 500 by Market Cap
st.markdown("### Tech Companies Dominate S&P 500 by Market Cap")
estimators = ["market_cap", "weight"]
color = {"market_cap": "Blues_r", "weight": "Oranges_r"}
for est in estimators:
    fig, ax = plt.subplots()
    sns.barplot(
        data=sp_500_comp.sort_values(by=est, ascending=False).head(10),
        y=est,
        x="symbol",
        palette=color[est],
    )
    plt.xticks(rotation=45)
    plt.title(
        "Tech Companies Dominate S&P 500 {}".format(est.replace("_", " ").title())
    )
    st.pyplot(fig)

# Additional Market Cap Analysis
st.markdown("#### Additional Market Cap Analysis")
top_comp_mkt_cap = (
    sp_500_comp[
        ["symbol", "current_price", "market_cap", "ebitda", "revenue_growth", "weight"]
    ]
    .sort_values(by="market_cap", ascending=False)
    .head(10)
)
st.dataframe(top_comp_mkt_cap)


# Correlation Matrix
st.markdown("### Size and profitability of a company are closely linked to its weight")
st.markdown(
    "Current price and revenue growth are not strongly connected to these factors."
)
correlation_matrix = sp_500_comp[
    ["current_price", "market_cap", "ebitda", "revenue_growth", "weight"]
].corr()
fig, ax = plt.subplots()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Profitability is correlated to weight")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
st.pyplot(fig)
st.markdown(
    "Weight is calculated by the S&P 500 index committee and is based on market cap and liquidity. Stock price x shares outstanding."
)

# Display head of dataframes
st.markdown("### Explore: S&P 500 Dataframes")
st.write("S&P 500 Companies")
st.dataframe(sp_500_comp.head())
st.write("S&P 500 Index Levels")
st.dataframe(sp_500_index.head())
st.write("S&P 500 Stocks")
st.dataframe(sp_500_stocks.head())

with st.sidebar:
    launch_chatbot(st)
