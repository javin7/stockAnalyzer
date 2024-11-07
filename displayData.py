import fetchData
import matplotlib.pyplot as plt

fetchData.calculateTechnicalIndicators()

plt.figure(figsize=(14, 8))
plt.plot(fetchData.stockData["Close"], label="Close RPice")
plt.plot(fetchData.stockData["SMA365"], label="Annual SMA")
plt.plot(fetchData.stockData["EMA365"], label="Annual EMA")
plt.plot(fetchData.stockData["RSI"], label="Annual RSI")


plt.title(f"{fetchData.ticker} Stock Price with SMA and EMA")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

