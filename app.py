import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import streamlit as st
import yfinance
company = st.text_input("ENTER THE COMPANY TICKER ID")

today = date.today()
end_date = today.strftime("%Y-%m-%d")
start_date = (today - timedelta(days=7)).strftime("%Y-%m-%d")
data = yf.download(company, start=start_date, end=end_date, progress=False)

# Create a Streamlit app
st.text("SANKET PRECTION WEB PAGE")
st.title("STOCK INDEX DATA FOR PREDICTION")
st.write(data.head())
