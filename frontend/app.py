import streamlit as st
import httpx

BACKEND_URL = "http://backend:8000"

st.set_page_config(page_title="INTERRA", layout="wide")
st.title("INTERRA")

# Sidebar for configuration / experiment controls
with st.sidebar:
    st.header("Configuration")
    st.info("Experiment controls will go here.")

# Main area
st.subheader("Status")
try:
    resp = httpx.get(f"{BACKEND_URL}/health", timeout=3)
    if resp.status_code == 200:
        st.success("Backend is reachable")
    else:
        st.error(f"Backend returned {resp.status_code}")
except Exception as e:
    st.error(f"Cannot reach backend: {e}")
