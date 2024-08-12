import streamlit as st
from langchainHelper import Create_Vector_DB,Get_QA_Chain

st.set_page_config(page_title="E-LEARNING CHATBOT",layout="centered")
st.title("🎓 E-LEARNING CHATBOT 🎓")
st.write("It is Powered by Google Gemini and trained on my specific data which is related to bootcamps of udemy courses")

if "history" not in st.session_state:
    st.session_state["history"] = []

# Display chat history
for user_message, bot_message in st.session_state.history:
    st.markdown(f"""
    <div style="
        background-color: #d1d3e0; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {user_message} 😊</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="
        background-color: #e1ffc7; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Answer:</b> {bot_message} 🤖</p>
    </div>
    """, unsafe_allow_html=True)

with st.form(key="chat_form", clear_on_submit=True):
    question = st.text_input("Question: ")
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if question:
            chain = Get_QA_Chain()
            response = chain(question)
            # st.header("Answer")
            st.session_state.history.append((question, response["result"]))

            # st.write(response["result"])
        else:
            st.warning("Please enter the question")
    