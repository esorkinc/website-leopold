import os
import streamlit as st

# Get the port from the environment variable
port = int(os.environ.get("PORT", 8501))

# Run Streamlit with the assigned port
st.run(port=port, host="0.0.0.0")


st.title("My First Web App")
st.write("Hello, friend")
