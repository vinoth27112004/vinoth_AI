import streamlit as st
import google.generativeai as genai


genai.configure(api_key="gemini_api")
def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Vinoth created this AI "+txt)
    return response.text




st.title("Welcome to Vinoth's AI")

command = st.chat_input("how can I help you?")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])


if command:
    with st.chat_message("USER"):
        st.write(command)
        st.session_state.message.append({"role":"USER","message":command})
    if "hello" in command:
        with st.chat_message("BOT"):
            st.write("Hi,How are you?")
            st.session_state.message.append({"role":"BOT","message":"Hi How are you?"})
    elif "who" in command:
        with st.chat_message("BOT"):
            st.write("I am Vinoth's AI Assistant")
            st.session_state.message.append({"role":"BOT","message":"I am Vinoth's AI Assistant"})
    
    elif "how you made" in command:
        with st.chat_message("BOT"):
            st.write("I made by Vinoth kumar")
            st.session_state.message.append({"role":"BOT","message":"I made by Vinoth kumar"})

    elif "fine" in command:
        with st.chat_message("BOT"):
            st.write("Good")
            st.session_state.message.append({"role":"BOT","message":"Good"})

    elif "Vishali merin" in command:
        with st.chat_message("BOT"):
            st.write("Ohh Vinoth's Sister!. How are you Sister")
            st.session_state.message.append({"role":"BOT","message":"Ohh Vinoth's Sister. How are you Sister"})

    elif "vishali merin" in command:
        with st.chat_message("BOT"):
            st.write("Ohh Vinoth's Sister!. How are you Sister")
            st.session_state.message.append({"role":"BOT","message":"Ohh Vinoth's Sister!. How are you Sister"})

    elif "Hello" in command:
        with st.chat_message("BOT"):
            st.write("Hi,How are you?")
            st.session_state.message.append({"role":"BOT","message":"Hi,How are you?"})

    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"BOT","message":data})




print(st.session_state.message)
