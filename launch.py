import streamlit as st
import os
import requests

RPC_URL = os.getenv("RPC_URL", "https://GBTNetwork")

st.title("🔗 GBTNetwork Interface")

try:
    r = requests.get(f"{RPC_URL}/chain-info").json()
    st.success("Connected to GBTNetwork!")
    st.write(f"Chain ID: {r['chainId']}")
    st.write(f"Currency: {r['currency']}")
except Exception as e:
    st.error("❌ Could not connect to GBTNetwork.")
    st.code(str(e))
