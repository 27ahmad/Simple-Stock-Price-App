import yfinance as yf
import streamlit as st
import pandas as pd

with st.container():
    st.header("Simple Stock Price App :chart_with_upwards_trend:")
    st.subheader("Below are the closing stock prices and volume of Google since 2010")
    st.write("---")


tickerData = yf.Ticker('GOOGL')

tickerDf = tickerData.history(period= '1d', start = '2010-1-1', end='2024-1-1')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)