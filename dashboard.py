import streamlit as st
import requests

st.title("AI Security Log Analyzer")

uploaded_file = st.file_uploader("Upload log file")

if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}

    response = requests.post("http://localhost:8000/analyze-log", files=files)

    if response.status_code == 200:
        results = response.json()["results"]

        st.subheader("Detection Results")
        for r in results:
            st.json(r)
    else:
        st.error("Error connecting to API")