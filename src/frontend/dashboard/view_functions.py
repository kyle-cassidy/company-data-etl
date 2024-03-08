import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error
# import json
# import requests
# import os
# import pathlib


def set_config(st):
    st.set_page_config(
        page_title="Public Company Insights: S&P 500",
        page_icon="📈",
        layout="centered",
        initial_sidebar_state="auto",
        menu_items=None,
    )
    ss = st.session_state
    if "debug" not in ss:
        ss["debug"] = {}


# Sector Breakdown
def sector_breakdown(st, sp_500_comp):
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
def companies_market_cap(st, sp_500_comp):
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
def additional_market_cap_analysis(st, sp_500_comp):
    st.markdown("#### Additional Market Cap Analysis")
    top_comp_mkt_cap = (
        sp_500_comp[
            [
                "symbol",
                "current_price",
                "market_cap",
                "ebitda",
                "revenue_growth",
                "weight",
            ]
        ]
        .sort_values(by="market_cap", ascending=False)
        .head(10)
    )
    st.dataframe(top_comp_mkt_cap)

# Correlation Matrix
def correlation_matrix(st, sp_500_comp):
    st.markdown("### Size and profitability of a company are closely linked to its weight")
    st.markdown(
        "Current price and revenue growth are not strongly connected to these factors."
    )
    correlation_matrix = sp_500_comp[
        ["current_price", "market_cap", "ebitda", "revenue_growth", "weight"]
        .corr()
    fig, ax = plt.subplots()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Profitability is correlated to weight")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    st.pyplot(fig)
    st.markdown(
        "Weight is calculated by the S&P 500 index committee and is based on market cap and liquidity. Stock price x shares outstanding."
    )
    
# display head of dataframes
def display_dataframes(st, company=sp_500_comp, index=sp_500_index, stocks=sp_500_stocks):
    st.markdown("### Explore: S&P 500 Dataframes")
    st.write("S&P 500 Companies")
    st.dataframe(sp_500_comp.head())
    st.write("S&P 500 Index Levels")
    st.dataframe(sp_500_index.head())
    st.write("S&P 500 Stocks")
    st.dataframe(sp_500_stocks.head())
    
    # start of a refactored version of the function
    # for df in list_of_dataframes:
    #     st.write(df.head())