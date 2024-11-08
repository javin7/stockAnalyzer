from fetchData import *
from predictMarketMovement import *
import matplotlib.pyplot as plt

# Calculate technical indicaotrs
calculateTechnicalIndicators()

stockData["Prediction"] = model.predict(stockData[features])
stockData["Buy"] = np.where(stockData["Prediction"] == 1, stockData["Close"], np.nan)
stockData["Sell"] = np.where(stockData["Prediction"] == 0, stockData["Close"], np.nan)

# Create plot size
plt.figure(figsize=(16, 7))

# Plot closing price and moving averages
plt.plot(stockData["Close"], label="Close Price")
plt.plot(stockData["SMA"], label="SMA")
plt.plot(stockData["EMA"], label="EMA")

# Plot Buy and Sell indicators
plt.scatter(stockData.index, stockData["Buy"], marker="^", color="green", label="Buy Signal")
plt.scatter(stockData.index, stockData["Sell"], marker="v", color="red", label="Sell Signal")

# Create data plot
plt.title(f"{ticker} Stock Price with SMA and EMA")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()

