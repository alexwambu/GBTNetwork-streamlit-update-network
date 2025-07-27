import streamlit as st
from dotenv import load_dotenv
import os
import requests

load_dotenv()

st.image("static/logo.png", width=100)
st.title("Welcome to GBTNetwork Layer 1 🌐")

rpc_url = os.getenv("RPC_URL")

if st.button("Check RPC Status"):
    try:
        response = requests.get(f"{rpc_url}/")
        data = response.json()
        st.success(data["status"])
    except:
        st.error("RPC Server Not Reachable")
