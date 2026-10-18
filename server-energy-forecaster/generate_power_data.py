import pandas as pd
import numpy as np

# Set random seed for reproducible results
np.random.seed(42)

# Generate 720 hourly timestamps (30 days)
timestamps = pd.date_range(start="2026-09-01", periods=720, freq="h")

# Convert hours to a mutable NumPy array using .to_numpy()
hours = timestamps.hour.to_numpy()

# Daily power cycle: Sine wave swinging between ~200W (night) and ~600W (day)
base_power = 400 + 200 * np.sin((hours - 6) * np.pi / 12)
noise = np.random.normal(0, 18, size=720)
wattage = base_power + noise  # Now a standard mutable NumPy array

# Inject 5 power surge anomalies
surge_indices = [98, 245, 412, 580, 695]
for idx in surge_indices:
    wattage[idx] += np.random.uniform(350, 500)

# Save to CSV spreadsheet
df = pd.DataFrame({
    "timestamp": timestamps,
    "wattage": np.round(wattage, 2)
})

df.to_csv("server_power_usage.csv", index=False)
print("✅ Generated 'server_power_usage.csv' (720 hourly records with 5 power surges).")