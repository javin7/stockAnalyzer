# Libraries
import yfinance as yf
import pandas as pd

# Fetch data
ticker = yf.Ticker(input("Ticker: "))
stockData = ticker.history(period="1y")

def calculateRSI(data, wind):
    delta = data.diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avgGain = gain.rolling(window=wind).mean()
    avgLoss = loss.rolling(window=wind).mean()
    rs = avgGain / avgLoss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Technical Indicators
def calculateTechnicalIndicators():
    # Simple Moving Average (SMA)
    stockData["SMA50"] = stockData["Close"].rolling(window=20).mean()

    # Exponential Moving Average (EMA)
    stockData["EMA20"] = stockData["Close"].ewm(span=20,adjust=False).mean()

    # Relative Strength Index (RSI)
    stockData["RSI14"] = calculateRSI(stockData["Close"], 14)






