import streamlit as st
import pandas as pd
from tradebot.positions_manager import PositionsManager
from tradebot.session_manager import SessionManager

st.title("📈 Open Positions")

# Use current session from login
sm = SessionManager()  # Same session object as login
pm = PositionsManager(session=sm)

try:
    positions_data = pm.get_positions()
    if not positions_data:
        st.info("No open positions found")
    else:
        df = pd.DataFrame(positions_data)
        st.table(df)
except Exception as e:
    st.error(f"Error fetching positions: {str(e)}")
