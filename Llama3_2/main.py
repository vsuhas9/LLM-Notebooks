"""
 * author Suhas V
 * created on 26-09-2024-06h-53m
"""

import streamlit as st
from src import GetModels


__all__ = [
    "ChatWindow"
]


class ChatWindow:
    R""" Class to display strealit chat window
    """

    def __init__(self):
        R""" Creates an instance of the class 'ChatWindow'
        """
        self.models = GetModels()
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def handle_streamlit(self):
        R""" Method to handle streamlit UI
        """

        prompt = st.chat_input("How may i help you")
        if prompt is not None:
            with st.chat_message("user"):
                st.markdown(prompt)

            response = self.models.invoke_chain(prompt)
            response = response.content

            with st.chat_message("assistant"):
                st.markdown(response)

            st.session_state.messages.append(
                {"role": "user", "content": prompt})
            st.session_state.messages.append(
                {"role": "assistant", "content": response})


st.title("Chat LLama3.2")
ChatWindow().handle_streamlit()
