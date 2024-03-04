from db import load_data, persist_data
index = load_data()
persist_data(index, location = "../storage")
# query_engine = index.as_query_engine()
# query_engine.query("How did uber perform in 2021?")
