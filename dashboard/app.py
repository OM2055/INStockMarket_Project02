import os
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
st.title("NSE AI Quant Dashboard")

# ✅ Get project root safely
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

stocks_path = os.path.join(BASE_DIR, "output", "stocks.csv")
portfolio_path = os.path.join(BASE_DIR, "output", "portfolio.csv")

# ✅ Debug (optional)
st.write("Looking for files at:")
st.write(stocks_path)

# ✅ Safe loading
if not os.path.exists(stocks_path):
    st.error("❌ stocks.csv not found. Run: python run_pipeline.py")
    st.stop()

if not os.path.exists(portfolio_path):
    st.error("❌ portfolio.csv not found. Run pipeline first.")
    st.stop()

df = pd.read_csv(stocks_path)
portfolio = pd.read_csv(portfolio_path)

# 📊 Display
st.subheader("Top Stocks")
st.dataframe(df.head(10))

st.subheader("Portfolio Allocation")
st.bar_chart(portfolio.set_index("symbol")["weight"])

# 🔍 Stock explorer
stock = st.selectbox("Select Stock", df["symbol"])

if stock:
    row = df[df["symbol"] == stock].iloc[0]
    st.subheader(f"Details: {stock}")
    st.write(row)