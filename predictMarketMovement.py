from fetchData import *
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Generate target column: 1 for 'up' and 0 for 'down' based on price movement
stockData["Target"] = np.where(stockData["Close"].shift(-1) > stockData["Close"], 1, 0)

calculateTechnicalIndicators()

features = ["SMA", "EMA", "RSI14"]
X = stockData[features]
Y = stockData["Target"]