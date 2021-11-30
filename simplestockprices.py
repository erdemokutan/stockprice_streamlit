import yfinance as yf
import streamlit as st 
import pandas as pd


st.write(""" # Simple Stock Price App
 Shown are the stock **closing price** and **volume** of ***Google***
 
 | Syntax | Description |
| ----------- | ----------- |
| Test | Streamlit |
| Hello | There |
             
 
 {
  ```
{
  "firstName": "**Erdem**",
  "lastName": "**Okutan**",
  "age": **23**
}
```
}
 
 
 """)


tickerSymbol="GOOGL"

tickerData=yf.Ticker(tickerSymbol)

tickerDf=tickerData.history(period="id",start="2010-5-31",end="2021-11-30")

st.write("""
## Closing Price""")

st.line_chart(tickerDf.Close)

st.write("""
## Volume Price""")
st.line_chart(tickerDf.Volume)
