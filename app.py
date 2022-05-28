import os
import sys
import streamlit as st

sys.path.insert(0, './dashboard')
from applications import exploration
from multiapp import MultiApp

st.set_page_config(page_title="Rossmann Sales Predictions", layout="wide")

app = MultiApp()

st.sidebar.markdown("""
# Rossmann Sales Predictions
""")

# Add all your application here
app.add_app("visualizations", exploration.app)


# The main app
app.run()