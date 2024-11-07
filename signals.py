from fetchData import *

stockData["Signal"] = 0
stockData["Signal"][MOVING_AVERAGE_WINDOW:] = [
    1 if stockData["SMA"].iloc[i] > stockData["EMA"].iloc[i] else -1
    for i in range(MOVING_AVERAGE_WINDOW, len(stockData))
]

# Buy & Sell Signals
