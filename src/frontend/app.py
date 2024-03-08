import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error
import json
import requests
import os
from dashboard.chatbot import launch_chatbot
from dashboard.view_functions import (
    set_config,
    sector_breakdown,
    companies_market_cap,
    additional_market_cap_analysis,
    correlation_matrix,
    display_dataframes,
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


# subtitle
st.markdown("## Industry Analysis on the S&P 500")


# Connect to the database via API
def get_json(URL):
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()

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


# Breakdown of Sectors in S&P 500
sector_breakdown(st, sp_500_comp)

# Tech Companies Dominate S&P 500 by Market Cap
companies_market_cap(st, sp_500_comp)

# Additional Market Cap Analysis
additional_market_cap_analysis(st, sp_500_comp)

# Correlation Matrix
correlation_matrix(st, sp_500_comp)

# Display head of dataframes
display_dataframes(st, sp_500_comp, sp_500_index, sp_500_stocks)

with st.sidebar:
    launch_chatbot(st)
