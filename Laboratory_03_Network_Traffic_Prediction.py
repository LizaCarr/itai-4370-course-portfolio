"""Laboratory 03: Network Traffic Prediction with Random Forest."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="h")
hour = dates.hour
day_of_week = dates.dayofweek
day_of_year = dates.dayofyear

traffic = (
    50
    + 20 * np.sin(2 * np.pi * hour / 24)
    + 10 * np.sin(2 * np.pi * day_of_week / 7)
    + 5 * np.sin(2 * np.pi * day_of_year / 365)
    + np.random.normal(0, 5, len(dates))
)
business_hours = (hour >= 9) & (hour <= 17) & (day_of_week < 5)
traffic += business_hours * 15

data = pd.DataFrame({
    "timestamp": dates,
    "hour": hour,
    "day_of_week": day_of_week,
    "is_weekend": day_of_week >= 5,
    "is_business_hours": business_hours,
    "traffic_gbps": np.maximum(traffic, 0),
})
data["traffic_lag_1h"] = data["traffic_gbps"].shift(1)
data["traffic_lag_24h"] = data["traffic_gbps"].shift(24)
data["traffic_rolling_7d"] = data["traffic_gbps"].rolling(24 * 7, center=True).mean()
data = data.dropna()

features = [
    "hour", "day_of_week", "is_weekend", "is_business_hours",
    "traffic_lag_1h", "traffic_lag_24h", "traffic_rolling_7d",
]
X = data[features]
y = data["traffic_gbps"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=False
)

model = RandomForestRegressor(
    n_estimators=100, max_depth=10, random_state=42, n_jobs=-1
)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print(f"Testing MSE: {mean_squared_error(y_test, predictions):.2f}")
print(f"Testing R2: {r2_score(y_test, predictions):.3f}")

plt.figure(figsize=(10, 5))
plt.plot(y_test.iloc[:168].to_numpy(), label="Actual")
plt.plot(predictions[:168], label="Predicted")
plt.title("Network Traffic Prediction: One Test Week")
plt.xlabel("Hourly Test Index")
plt.ylabel("Traffic (Gbps)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
