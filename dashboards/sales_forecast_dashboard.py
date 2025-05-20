# dashboards/sales_forecast_dashboard.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from prophet.plot import plot_plotly
from pathlib import Path

# Title
st.title("🚗 Vehicle Sales Forecast Dashboard")

# Load data
DATA_PATH = Path("data/vehicle_sales_data_2000_2025.csv")

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data(DATA_PATH)

# Sidebar options
st.sidebar.header("Forecast Settings")
periods_input = st.sidebar.slider('Months to forecast:', 1, 24, 12)

# Preprocess
monthly_sales = df.groupby(pd.Grouper(key='Date', freq='M'))['Selling_Price'].sum().reset_index()
monthly_sales.columns = ['ds', 'y']

# Prophet Model
model = Prophet()
model.fit(monthly_sales)

# Forecast
future = model.make_future_dataframe(periods=periods_input, freq='M')
forecast = model.predict(future)

# Plot forecast
st.subheader("📈 Forecast Plot")
fig1 = plot_plotly(model, forecast)
st.plotly_chart(fig1)

# Actual vs Forecasted
st.subheader("📊 Actual vs Forecasted Sales")
combined = pd.merge(monthly_sales, forecast[['ds', 'yhat']], on='ds', how='left')
st.line_chart(combined.set_index('ds')[['y', 'yhat']].rename(columns={'y': 'Actual', 'yhat': 'Forecasted'}))

# Show data
with st.expander("🔍 View Raw Data"):
    st.write(df.head())

# Footer
st.markdown("---")
st.caption("Created by Branton • Flatiron Data Science Project")
