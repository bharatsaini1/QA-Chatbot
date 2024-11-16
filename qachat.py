import streamlit as st
import google.generativeai as genai

# Load environment variables
genai.configure(api_key="Add your api key")

# Load Gemini pro model and initialize chat
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get response from Gemini model
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    full_response = "".join(chunk.text for chunk in response)
    return full_response

# Streamlit app initialization
st.set_page_config(page_title="QA ChatBot", page_icon="Q&A Demo")
st.header("Chatbot 🙋‍♂️")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Input and submission
input_text = st.text_input("Ask your Question:", key="input")
submit = st.button("Generate Answer")

if submit and input_text:
    response = get_gemini_response(input_text)
    # Add user query and response to session chat history
    st.session_state["chat_history"].append(("You", input_text))
    st.session_state["chat_history"].append(("Bot", response))

    # Display response
    st.subheader("The Response is")
    st.write(response)

# Sidebar for chat history
with st.sidebar:
    if st.button("Show Chat History"):
        st.subheader("Chat History")
        for role, text in st.session_state["chat_history"]:
            st.write(f"**{role}:** {text}")
