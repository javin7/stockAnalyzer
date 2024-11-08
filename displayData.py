from fetchData import *
from predictMarketMovement import *
import matplotlib.pyplot as plt

# Calculate technical indicaotrs
calculateTechnicalIndicators()

# Create plot size
plt.figure(figsize=(16, 7))

# Plot closing price and moving averages
plt.plot(stockData["Close"], label="Close Price")
plt.plot(stockData["SMA"], label="SMA")
plt.plot(stockData["EMA"], label="EMA")

stockData["Mean_Target"] = meanTargetPrice
stockData["High_Target"] = highTargetPrice
stockData["Low_Target"] = lowTargetPrice

plt.plot(stockData.index, stockData["Mean_Target"], label="Mean Analyst Target", color="purple", linestyle="--")
plt.plot(stockData.index, stockData["High_Target"], label="High Analyst Target", color="green", linestyle="--", linewidth="2")
plt.plot(stockData.index, stockData["Low_Target"], label="Low Analyst Target", color="red", linestyle="--",linewidth="2")

# Create data plot
plt.title(f"{ticker} Stock Price with SMA and EMA")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()

