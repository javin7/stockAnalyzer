# Libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# Fetch data
ticker = yf.Ticker(input("Ticker: "))
stockData = ticker.history(period="2y")

# Technical Indicators
## Simple Moving Average (SMA)
stockData["SMA50"] = stockData["Close"].rolling(window=50).mean()

plt.figure(figsize=(14, 8))
plt.plot(stockData["SMA50"], label="50-day SMA")
plt.show()

