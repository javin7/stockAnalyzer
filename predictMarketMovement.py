from fetchData import *
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Generate target column: 1 for 'up' and 0 for 'down' based on price movement
stockData["Target"] = np.where(stockData["Close"].shift(-1) > stockData["Close"], 1, 0)

calculateTechnicalIndicators()
stockData = stockData.dropna()

features = ["SMA", "EMA", "RSI14"]
x = stockData[features]
y = stockData["Target"]

# Split data into training and testing sets
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=42)

# Use RandomForestClassifier to train on the historical data
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(xTrain, yTrain)

predictions = model.predict(xTest)

# Predict the signal (buy or sell) for the most recent data point
latest_data = xTest.iloc[-1:]  # Select the most recent row
predictions = model.predict(latest_data)



