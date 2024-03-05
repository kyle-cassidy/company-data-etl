from llama_index.core.indices.loading import load_index_from_storage
from llama_index.core.storage.storage_context import StorageContext
from dotenv import load_dotenv
import streamlit as st
import pathlib
import os

# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Get the absolute path of the current file's directory
current_file_dir = pathlib.Path(__file__).parent.absolute()
# Construct the path to the storage directory relative to the current file's location
storage_dir = current_file_dir.joinpath("../storage")


def load_from_db():
    storage_context = StorageContext.from_defaults(persist_dir=str(storage_dir))
    index = load_index_from_storage(storage_context)
    return index


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
        # ss["api_key"] = {}

    # st.write(f"<style>{css.v1}</style>", unsafe_allow_html=True)
    # header1 = st.empty()  # for errors / messages
    # header2 = st.empty()  # for errors / messages
    # header3 = st.empty()  # for errors / messages


# chatbot


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
    content = "Ask me a question about Uber or Lyft in 2021!"
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": content}]


###1
def chatbot(st):
    assign_chat_engine(st)
    assign_messages(st)
    st.markdown("## Chatbot")
    prompt = display_chatbox_and_store_questions(st)
    display_message_history(st)
    submit_prompt_display_result(st, prompt)


def launch_chatbot(st):
    if os.getenv("OPENAI_API_KEY"):
        chatbot(st)
    else:
        st.write(
            "## Enter your OpenAI API key"
            "You can sign up to OpenAI and/or create your API key [here](https://platform.openai.com/account/api-keys)"
        )
        api_key = st.text_input("OpenAI API key", type="password", key="api_key")
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
            chatbot(st)


###2
# def launch_bot_api_key(ss, st):
#     st.write("## Enter your OpenAI API key")
#     # Use the on_change callback to handle API key input
#     api_key = st.text_input(
#         "OpenAI API key",
#         type="password",
#         key="api_key",
#         on_change=api_key_entered,
#         args=(ss, st),
#     )


# def api_key_entered(ss, st):
#     # This function is called when the API key input changes.
#     # Check if the API key is provided and store it in the session state and as an environment variable.
#     if "api_key" in ss and ss["api_key"]:
#         os.environ["OPENAI_API_KEY"] = ss["api_key"]
#         # Directly call sidebar_chatbot after setting the API key.
#         sidebar_chatbot(st)
#     else:
#         # If the API key is somehow not set, you might want to handle this case, e.g., show a warning.
#         st.warning("Please enter your OpenAI API key.")


# ## load last: end of main app.
# # Ensure sidebar_chatbot is called if the API key already exists in the session state when the page is loaded or rerun.
# if "api_key" in ss and ss["api_key"]:
#     sidebar_chatbot(st)
