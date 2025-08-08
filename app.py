import streamlit as st
from chatbot_logic import get_bot_response

st.set_page_config(page_title="🏨 Hotel Chatbot", page_icon="🤖")
st.title("🏨 Welcome to The Serenity Bay Resort Chatbot")
st.markdown("Ask me anything about our hotel services, check-in timings, or room availability!")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.text_input("Type your question here:")

# On send
if st.button("Send") and user_input:
    response = get_bot_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Hotel Bot", response))

# Display chat history
for speaker, msg in st.session_state.chat_history:
    with st.chat_message(speaker):
        st.markdown(msg)




