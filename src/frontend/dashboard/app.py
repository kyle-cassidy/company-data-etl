import streamlit as st
from streamlit_state import assign_chat_engine, assign_messages
from view_functions import (set_title, display_message_history,
 display_chatbox_and_store_questions, submit_prompt_display_result)
import os

assign_chat_engine(st)
assign_messages(st)

set_title(st)

prompt = display_chatbox_and_store_questions(st)

display_message_history(st)

submit_prompt_display_result(st, prompt)