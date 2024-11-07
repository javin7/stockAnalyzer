# Libraries
import yfinance as yf
import pandas as pd


# Fetch data
ticker = yf.Ticker(input("Ticker: "))
stockData = ticker.history(period="1y")

def calculateRSI(data, window):
    delta = data.diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avgGain = gain.rolling(window=window).mean()
    avgLoss = loss.rolling(window=window).mean()
    rs = avgGain / avgLoss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Technical Indicators
def calculateTechnicalIndicators():
    # Simple Moving Average (SMA)
    stockData["SMA365"] = stockData["Close"].rolling(window=20).mean()

    # Exponential Moving Average (EMA)
    stockData["EMA365"] = stockData["Close"].ewm(span=365,adjust=False).mean()

    # Relative Strength Index (RSI)
    stockData["RSI"] = calculateRSI(stockData["Close"], 20)






