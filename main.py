import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple stock price app

Shown are the stock ***closing price*** and ***volume*** of Google!

""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2010-5-31', end='2022-11-10')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
