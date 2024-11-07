from fetchData import *
import matplotlib.pyplot as plt

# Calculate technical indicaotrs
calculateTechnicalIndicators()

# Create plot size
plt.figure(figsize=(14, 4))

# Plot closing price and moving averages
plt.plot(stockData["Close"], label="Close Price")
plt.plot(stockData["SMA"], label="SMA")
plt.plot(stockData["EMA"], label="EMA")

# Create data plot
plt.title(f"{ticker} Stock Price with SMA and EMA")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

