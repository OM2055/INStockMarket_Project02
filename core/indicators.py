import yfinance as yf
import pandas as pd

def get_technical(symbol):
    df = yf.download(symbol + ".NS", period="1y", progress=False)

    if df is None or df.empty:
        return None

    df["dma50"] = df["Close"].rolling(50).mean()
    df["dma200"] = df["Close"].rolling(200).mean()

    df = df.dropna()

    if df.empty:
        return None

    latest = df.iloc[-1]

    # 🔴 SAFE extraction (important fix)
    dma50 = latest["dma50"]
    dma200 = latest["dma200"]
    close = latest["Close"]

    # If somehow still Series → take scalar
    if isinstance(dma50, pd.Series):
        dma50 = dma50.iloc[0]

    if isinstance(dma200, pd.Series):
        dma200 = dma200.iloc[0]

    if isinstance(close, pd.Series):
        close = close.iloc[0]

    return {
        "dma50": float(dma50),
        "dma200": float(dma200),
        "close": float(close)
    }