# lambda/spy_price.py
import yfinance as yf

def get_spy_price() -> float:
    tkr = yf.Ticker("SPY")

    # 1️⃣  Fast, lightweight endpoint
    if "last_price" in tkr.fast_info:
        return tkr.fast_info["last_price"]

    # 2️⃣  Fallback to .info if it still exists
    if "currentPrice" in tkr.info:
        return tkr.info["currentPrice"]

    # 3️⃣  Robust fallback: 1‑minute candle
    last_tick = tkr.history(period="1d", interval="1m")["Close"].iloc[-1]
    return float(last_tick)

