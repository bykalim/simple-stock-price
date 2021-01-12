import streamlit as st
import pandas as pd
import yfinance as yf

st.write("""
# Stock Exchange

""")
googleStock = yf.Ticker('GOOGL')
googleStockData = googleStock.history(period='id', start='2010-01-01', end='2021-01-31')

st.line_chart(googleStockData.Close)
