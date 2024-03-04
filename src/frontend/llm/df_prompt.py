# requirements: llama-index-llms-openai, llama-index-core, pandas, requests
import os
import requests
import pandas as pd
from llama_index.llms.openai import OpenAI
from llama_index.core import PromptTemplate
from llama_index.core.query_engine.pandas import PandasInstructionParser
from llama_index.core.query_pipeline import (
    QueryPipeline as QP,
    Link,
    InputComponent,
)
llm = OpenAI(model="gpt-3.5-turbo")

## UNDER CONSTRUCTION ## 
# This file will be used to create a pipeline for the llm to query the dataframes

# 1. Pandas prompt to infer pandas instructions from user query
# 2. Pandas output parser to execute pandas instructions on dataframe, get back dataframe
# 3. Response synthesis prompt to synthesize a final response given the dataframe


# localhost API URL: src/backend/.flaskenv
API_URL = os.getenv('API_URL', 'http://127.0.0.1:80')


# API endpoints: TODO - move to a separate file
COMPANIES_URL = f'{API_URL}/companies'
COMPANY_SYMBOL_URL = f'{API_URL}/companies/symbol/'
COMPANY_ID_URL = f'{API_URL}/companies/id/'
STOCKS_URL = f'{API_URL}/stocks'
INDEX_URL = f'{API_URL}/index_levels'


#financial statements have not been adapted to the backend yet: FIXME
seed_path="src/backend/app/data/seed-sp500/sp500_csv/"
balanceSheetHistory_quarterly=pd.read_csv(f"{seed_path}balanceSheetHistory_quarterly.csv")
balanceSheetHistory_annually=pd.read_csv(f"{seed_path}balanceSheetHistory_annually.csv")
incomeStatementHistory_quarterly=pd.read_csv(f"{seed_path}incomeStatementHistory_quarterly.csv")
incomeStatementHistory_annually=pd.read_csv(f"{seed_path}incomeStatementHistory_annually.csv")
cashflowStatement_quarterly=pd.read_csv(f"{seed_path}cashflowStatement_quarterly.csv")
cashflowStatement_annually=pd.read_csv(f"{seed_path}cashflowStatement_annually.csv")

# all dfs
dfs = [balanceSheetHistory_quarterly, balanceSheetHistory_annually, incomeStatementHistory_quarterly, incomeStatementHistory_annually, cashflowStatement_quarterly, cashflowStatement_annually]
#FIXME: need support for multiple dfs or a single df with all the data

instruction_str = (
    "1. Convert the query to executable Python code using Pandas.\n"
    "2. The final line of code should be a Python expression that can be called with the `eval()` function.\n"
    "3. The code should represent a solution to the query.\n"
    "4. PRINT ONLY THE EXPRESSION.\n"
    "5. Do not quote the expression.\n"
)

pandas_prompt_str = (
    "You are working with a pandas dataframe in Python.\n"
    "The name of the dataframe is `df`.\n"
    "This is the result of `print(df.head())`:\n"
    "{df_str}\n\n"
    "Follow these instructions:\n"
    "{instruction_str}\n"
    "Query: {query_str}\n\n"
    "Expression:"
)
response_synthesis_prompt_str = (
    "Given an input question, synthesize a response from the query results.\n"
    "Query: {query_str}\n\n"
    "Pandas Instructions (optional):\n{pandas_instructions}\n\n"
    "Pandas Output: {pandas_output}\n\n"
    "Response: "
)

pandas_prompt = PromptTemplate(pandas_prompt_str).partial_format(
    instruction_str=instruction_str, df_str=df.head(5)
)
pandas_output_parser = PandasInstructionParser(df)
response_synthesis_prompt = PromptTemplate(response_synthesis_prompt_str)
llm = OpenAI(model="gpt-3.5-turbo")