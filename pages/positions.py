import streamlit as st
from tradebot.positions_manager import PositionsManager

pm = PositionsManager()

st.title("📈 Positions")
positions_data = pm.get_positions()  # function in positions_manager.py
st.table(positions_data)
