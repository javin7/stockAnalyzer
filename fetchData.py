# Libraries
import yfinance as yf

# Constants
MOVING_AVERAGE_WINDOW = 20

# Fetch data
ticker = yf.Ticker(input("Ticker: "))
stockData = ticker.history(period="1y")

# Get target prices
targetPrices = ticker.analyst_price_targets
meanTargetPrice = targetPrices.get("mean")
highTargetPrice = targetPrices.get("high")
lowTargetPrice = targetPrices.get("low")

# Calculate RSI (Relative Strength Index)
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
    stockData["SMA"] = stockData["Close"].rolling(window=MOVING_AVERAGE_WINDOW).mean()
    # Exponential Moving Average (EMA)
    stockData["EMA"] = stockData["Close"].ewm(span=MOVING_AVERAGE_WINDOW,adjust=False).mean()
    # Relative Strength Index (RSI)
    stockData["RSI14"] = calculateRSI(stockData["Close"], 14)






