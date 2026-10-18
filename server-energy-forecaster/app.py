import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

st.set_page_config(page_title="Power Surge Forecaster", page_icon="⚡", layout="wide")

st.title("⚡ Server Power Consumption & Surge Forecaster")
st.write("Upload an hourly wattage log or evaluate the default dataset to forecast power demand and detect hardware power surges.")

# Load saved ML model and threshold
@st.cache_resource
def load_ml_assets():
    return joblib.load("energy_assets.pkl")

assets = load_ml_assets()
model = assets["model"]
threshold = assets["threshold"]

# File uploader widget
uploaded_file = st.file_uploader("Upload Hourly Power CSV Log:", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.info("Using default log file (`server_power_usage.csv`). Upload a custom CSV to evaluate external logs.")
    df = pd.read_csv("server_power_usage.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])

# Feature Engineering
df["lag_1"] = df["wattage"].shift(1)
df["lag_24"] = df["wattage"].shift(24)
df["rolling_mean_6"] = df["wattage"].shift(1).rolling(window=6).mean()
df["hour"] = df["timestamp"].dt.hour
df["day_of_week"] = df["timestamp"].dt.dayofweek

df_clean = df.dropna().copy()

if len(df_clean) > 0:
    X = df_clean[["lag_1", "lag_24", "rolling_mean_6", "hour", "day_of_week"]]
    
    # ML Prediction & Anomaly Calculation
    df_clean["predicted_wattage"] = model.predict(X)
    df_clean["residual"] = np.abs(df_clean["wattage"] - df_clean["predicted_wattage"])
    df_clean["is_anomaly"] = df_clean["residual"] > threshold

    # Dashboard Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Scanned Records", len(df_clean))
    col2.metric("Peak Power Draw", f"{df_clean['wattage'].max():.1f} W")
    col3.metric("Average Power Load", f"{df_clean['wattage'].mean():.1f} W")
    
    anomalies_found = df_clean["is_anomaly"].sum()
    col4.metric("🚨 Surges Detected", anomalies_found, delta=f"{anomalies_found} Anomalies", delta_color="inverse")

    st.divider()

    # Interactive Plotly Time-Series Chart
    fig = go.Figure()

    # Blue Line: Actual Power Draw
    fig.add_trace(go.Scatter(
        x=df_clean["timestamp"],
        y=df_clean["wattage"],
        mode="lines",
        name="Actual Power (W)",
        line=dict(color="#1f77b4", width=2)
    ))

    # Green Line: ML Predicted Baseline
    fig.add_trace(go.Scatter(
        x=df_clean["timestamp"],
        y=df_clean["predicted_wattage"],
        mode="lines",
        name="ML Expected Baseline (W)",
        line=dict(color="#2ca02c", width=2, dash="dash")
    ))

    # Red Markers: Injected Surges / Anomalies
    anomalies_df = df_clean[df_clean["is_anomaly"]]
    if not anomalies_df.empty:
        fig.add_trace(go.Scatter(
            x=anomalies_df["timestamp"],
            y=anomalies_df["wattage"],
            mode="markers",
            name="🚨 Power Surge / Anomaly",
            marker=dict(color="red", size=10, symbol="x")
        ))

    fig.update_layout(
        title="Hourly Server Power Draw vs. Machine Learning Expected Baseline",
        xaxis_title="Timestamp",
        yaxis_title="Power Consumption (Watts)",
        legend=dict(x=0, y=1.1, orientation="h"),
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Detailed Anomaly Log Table
    if anomalies_found > 0:
        st.subheader("🚨 Detected Power Surge Incident Log")
        st.dataframe(
            anomalies_df[["timestamp", "wattage", "predicted_wattage", "residual"]].rename(
                columns={
                    "timestamp": "Timestamp",
                    "wattage": "Actual Wattage (W)",
                    "predicted_wattage": "Expected Baseline (W)",
                    "residual": "Surge Deviation (W)"
                }
            )
        )