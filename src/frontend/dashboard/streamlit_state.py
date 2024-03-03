from view_functions import load_from_db
from llama_index.core.storage.storage_context import StorageContext

def assign_chat_engine(st):
    if "chat_engine" not in st.session_state.keys():
        index = load_from_db()
        st.session_state.chat_engine = index.as_query_engine()
    
def assign_messages(st):
    content = "Ask me a question about Uber or Lyft in 2021!"
    if "messages" not in st.session_state.keys(): 
        st.session_state.messages = [
            {"role": "assistant", "content": content}
        ]