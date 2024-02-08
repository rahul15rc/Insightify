import streamlit as st
from analytics import analytics_page
from home_page import home_page
from chatbot import chatbot_call

import streamlit as st
st.write('<p style="font-size:130%">Import Dataset</p>', unsafe_allow_html=True)
dataset = st.file_uploader(label = '')
def home_page():
    
    st.title("Welcome to Insightify")
    st.write("This is an universal tool for data science.")
    
# Sidebar navigation
st.sidebar.image('logo.png', width=200)
page = st.sidebar.radio("Select Page", ["Home", "Analytics","Research Assistant"])

# Render selected page
if page == "Home":
    home_page()
elif page == "Analytics":
    analytics_page(dataset)
elif page == "Research Assistant":
    chatbot_call(dataset)
