import fetchData as data
import matplotlib.pyplot as plt

# Calculate technical indicaotrs
data.calculateTechnicalIndicators()

# Create plot size
plt.figure(figsize=(14, 4))

# Plot closing price and moving averages
plt.plot(data.stockData["Close"], label="Close Price")
plt.plot(data.stockData["SMA50"], label="SMA")
plt.plot(data.stockData["EMA20"], label="EMA")

# Create data plot
plt.title(f"{data.ticker} Stock Price with SMA and EMA")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

