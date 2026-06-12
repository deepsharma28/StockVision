import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import joblib
import plotly.express as px
import plotly.graph_objects as go

# ==========================
# Page Config
# ==========================

st.set_page_config(
    page_title="StockVision",
    page_icon="assets/logo.png",
    layout="wide"
)

# ==========================
# LOGO + BRANDING
# ==========================

col_logo, col_title = st.columns([1, 5])

with col_logo:
    st.image("assets/logo.png", width=90)

with col_title:
    st.markdown("## StockVision")
    st.caption("AI Powered Stock Forecasting Dashboard")

st.divider()

# ==========================
# Sidebar
# ==========================

st.sidebar.title("Stock Selection")

stock = st.sidebar.selectbox(
    "Select Stock",
    ["TSLA", "AAPL", "MSFT"]
)

company_names = {
    "TSLA": "Tesla",
    "AAPL": "Apple",
    "MSFT": "Microsoft"
}

# ==========================
# Load Model
# ==========================

model = joblib.load(f"models/{stock}_model.pkl")

# ==========================
# Download Data (FIXED)
# ==========================

df = yf.download(stock, period="2y", auto_adjust=True)

# 🔥 FIX: handle MultiIndex columns
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

df.dropna(inplace=True)

# ==========================
# Feature Engineering
# ==========================

df['Lag_1'] = df['Close'].shift(1)
df['Lag_2'] = df['Close'].shift(2)
df['Lag_3'] = df['Close'].shift(3)
df['Lag_5'] = df['Close'].shift(5)

df['MA_5'] = df['Close'].rolling(5).mean()
df['MA_10'] = df['Close'].rolling(10).mean()
df['MA_20'] = df['Close'].rolling(20).mean()

df['Volatility'] = df['Close'].rolling(10).std()
df['Return'] = df['Close'].pct_change()

df.dropna(inplace=True)

latest = df.iloc[-1]

# ==========================
# SAFE FUNCTION
# ==========================

def safe_float(x):
    return float(np.array(x).squeeze())

# ==========================
# Features
# ==========================

feature_list = [
    latest['Lag_1'],
    latest['Lag_2'],
    latest['Lag_3'],
    latest['Lag_5'],
    latest['MA_5'],
    latest['MA_10'],
    latest['MA_20'],
    latest['Volatility'],
    latest['Return'],
    latest['Volume']
]

features = np.array(feature_list).reshape(1, -1)

# ==========================
# Prediction (SAFE)
# ==========================

prediction = safe_float(model.predict(features)[0])

# ==========================
# Current Price (SAFE)
# ==========================

current_price = safe_float(latest['Close'])

change = prediction - current_price

# ==========================
# HEADER
# ==========================

st.subheader(f"AI Forecasting for {company_names[stock]}")

# ==========================
# KPI CARDS
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Price", f"${current_price:.2f}")

with col2:
    st.metric("Predicted Price", f"${prediction:.2f}")

with col3:
    st.metric("Expected Change", f"${change:.2f}")

st.divider()

# ==========================
# PRICE CHART
# ==========================

st.subheader("Closing Price Trend")

fig = px.line(df, x=df.index, y="Close")
st.plotly_chart(fig, use_container_width=True)

# ==========================
# MOVING AVERAGES
# ==========================

st.subheader("Moving Averages")

fig_ma = go.Figure()
fig_ma.add_trace(go.Scatter(x=df.index, y=df['Close'], name="Close"))
fig_ma.add_trace(go.Scatter(x=df.index, y=df['MA_5'], name="MA 5"))
fig_ma.add_trace(go.Scatter(x=df.index, y=df['MA_20'], name="MA 20"))

st.plotly_chart(fig_ma, use_container_width=True)

# ==========================
# VOLUME
# ==========================

st.subheader("Volume")

fig_vol = px.bar(df, x=df.index, y="Volume")
st.plotly_chart(fig_vol, use_container_width=True)

# ==========================
# LATEST DATA
# ==========================

st.subheader("Latest Data")
st.dataframe(df.tail(10), use_container_width=True)

# ==========================
# MODEL METRICS
# ==========================

st.subheader("Model Performance")

metrics = pd.read_csv("metrics/metrics.csv")
metrics = metrics[metrics["Stock"] == stock]

st.dataframe(metrics, use_container_width=True)

# ==========================
# FEATURE IMPORTANCE
# ==========================

if hasattr(model, "feature_importances_"):

    st.subheader("Feature Importance")

    feature_names = [
        'Lag_1', 'Lag_2', 'Lag_3', 'Lag_5',
        'MA_5', 'MA_10', 'MA_20',
        'Volatility', 'Return', 'Volume'
    ]

    importance = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    }).sort_values("Importance", ascending=True)

    fig_imp = px.bar(
        importance,
        x="Importance",
        y="Feature",
        orientation="h"
    )

    st.plotly_chart(fig_imp, use_container_width=True)

# ==========================
# FOOTER
# ==========================

st.divider()
st.caption("Built with Machine Learning + Streamlit + Yahoo Finance")