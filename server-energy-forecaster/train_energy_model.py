import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# 1. Load historical power log
df = pd.read_csv("server_power_usage.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# 2. Feature Engineering (Creating Lags and Time Signals)
df["lag_1"] = df["wattage"].shift(1)               # Wattage 1 hour ago
df["lag_24"] = df["wattage"].shift(24)             # Wattage same hour yesterday
df["rolling_mean_6"] = df["wattage"].shift(1).rolling(window=6).mean() # 6-hour average
df["hour"] = df["timestamp"].dt.hour               # Hour of day (0-23)
df["day_of_week"] = df["timestamp"].dt.dayofweek   # Day index (0-6)

# Drop missing rows created by time shifts
df_clean = df.dropna().copy()

X = df_clean[["lag_1", "lag_24", "rolling_mean_6", "hour", "day_of_week"]]
y = df_clean["wattage"]

# 3. Train Random Forest Regression Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 4. Compute Anomaly Error Threshold on Baseline
predictions = model.predict(X)
residuals = np.abs(y - predictions)
anomaly_threshold = np.mean(residuals) + (2.5 * np.std(residuals))

# 5. Save Model Assets to Disk
assets = {
    "model": model,
    "threshold": anomaly_threshold,
    "features": ["lag_1", "lag_24", "rolling_mean_6", "hour", "day_of_week"]
}

joblib.dump(assets, "energy_assets.pkl")
print(f"✅ Trained Random Forest Model. Anomaly Threshold set to: {anomaly_threshold:.2f} Watts deviation.")