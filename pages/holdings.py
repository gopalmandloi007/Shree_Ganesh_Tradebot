import streamlit as st
from tradebot.holdings_manager import HoldingsManager

hm = HoldingsManager()

st.title("📊 Holdings")
holdings_data = hm.get_holdings()  # function in holdings_manager.py
st.table(holdings_data)
