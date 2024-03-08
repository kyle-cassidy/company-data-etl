from llama_index.core.indices.loading import load_index_from_storage
from llama_index.core.storage.storage_context import StorageContext
from dotenv import load_dotenv
import streamlit as st
import pathlib
import os

# chatbot
# Get the absolute path of the current file's directory
current_file_dir = pathlib.Path(__file__).parent.absolute()
# Construct the path to the storage directory relative to the current file's location
storage_dir = current_file_dir.joinpath("../storage")


def load_from_db():
    storage_context = StorageContext.from_defaults(persist_dir=str(storage_dir))
    index = load_index_from_storage(storage_context)
    return index


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
                st.session_state.messages.append(
                    message
                )  # Add response to message history


def assign_chat_engine(st):
    if "chat_engine" not in st.session_state.keys():
        index = load_from_db()
        st.session_state.chat_engine = index.as_query_engine()


def assign_messages(st):
    if "messages" not in st.session_state.keys():
        content = "Ask me a question about Uber or Lyft in 2021!"
        st.session_state.messages = [{"role": "assistant", "content": content}]


def chatbot(st):
    assign_chat_engine(st)
    assign_messages(st)
    st.markdown("## Chatbot")
    prompt = display_chatbox_and_store_questions(st)
    display_message_history(st)
    submit_prompt_display_result(st, prompt)


def launch_chatbot(st):
    load_dotenv()
    if os.getenv("OPENAI_API_KEY"):
        chatbot(st)
    else:
        st.write(
            "## Enter your OpenAI API key\n"
            "You can sign up to OpenAI and/or create your API key [here](https://platform.openai.com/account/api-keys)\n"
        )
        # Use named expression to simplify assignment and conditional
        if api_key := st.text_input("OpenAI API key", type="password", key="api_key"):
            os.environ["OPENAI_API_KEY"] = api_key
            chatbot(st)

        # api_key = st.text_input("OpenAI API key", type="password", key="api_key")
        # if api_key:
        #     os.environ["OPENAI_API_KEY"] = api_key
        #     chatbot(st)
