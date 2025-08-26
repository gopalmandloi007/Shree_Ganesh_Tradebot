import streamlit as st
import pandas as pd
from tradebot.holdings_manager import HoldingsManager
from tradebot.session_manager import SessionManager

st.title("📊 Current Holdings")

# Use current session from login
sm = SessionManager()  # Same session object as login
hm = HoldingsManager(session=sm)

try:
    holdings_data = hm.get_holdings()
    if not holdings_data:
        st.info("No holdings found")
    else:
        df = pd.DataFrame(holdings_data)
        st.table(df)
except Exception as e:
    st.error(f"Error fetching holdings: {str(e)}")
