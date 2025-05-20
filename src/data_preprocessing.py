# src/data_preprocessing.py

import pandas as pd

def load_vehicle_sales_data(filepath):
    return pd.read_csv(filepath)

def clean_vehicle_sales_data(df):
    df['Date'] = pd.to_datetime(df['Invoice_Date'], errors='coerce')
    df = df.dropna(subset=['Date', 'Selling_Price'])
    return df

def aggregate_monthly_sales(df):
    monthly_sales = df.groupby(pd.Grouper(key='Date', freq='M'))['Selling_Price'].sum().reset_index()
    monthly_sales.columns = ['ds', 'y']
    return monthly_sales
