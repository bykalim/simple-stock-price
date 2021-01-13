import streamlit as st
import yfinance as yf

st.write("""
# Stock Exchange

""")
googleStock = yf.Ticker('GOOGL')
appleStock = yf.Ticker('AAPL')
samsungStock = yf.Ticker('AAPL')

googleStockData = googleStock.history(period='id', start='2020-01-01', end='2021-01-31')
appleStockData = appleStock.history(period='id', start='2020-01-01', end='2021-01-31')
samsungStockData = samsungStock.history(period='id', start='2020-01-01', end='2021-01-31')

st.line_chart(googleStockData.Close)
st.line_chart(appleStockData.Close)
st.line_chart(samsungStockData.Close)
