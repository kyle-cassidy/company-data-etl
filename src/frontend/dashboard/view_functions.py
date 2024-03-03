from llama_index.core.indices.loading import load_index_from_storage
from llama_index.core.storage.storage_context import StorageContext
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

os.environ['OPENAI_API_KEY'] =OPENAI_API_KEY

def load_from_db():
    storage_context = StorageContext.from_defaults(persist_dir="../storage")
    index = load_index_from_storage(storage_context)
    return index

def set_title(st):
    st.set_page_config(page_title="Uber and Lyft 10k Chatbot",
     layout="centered",
     initial_sidebar_state="auto", menu_items=None)
    st.title("Chat with the Uber or Lyft docs")

def display_message_history(st):
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

def display_chatbox_and_store_questions(st):
    if prompt := st.chat_input("Your question"):
        message = {"role": "user", "content": prompt}
        st.session_state.messages.append(message)
    return prompt

def submit_prompt_display_result(st, prompt):
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chat_engine.query(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message) # Add response to message history

