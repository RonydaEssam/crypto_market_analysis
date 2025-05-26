import pandas as pd
import glob
import streamlit as st
from matplotlib import pyplot as plt

# load ans sort csv files
csv_files = glob.glob("data/prices_*.csv")
csv_files.sort()

all_data = []

for i, file in enumerate(csv_files):
    df = pd.read_csv(file)
    df["day"] = i+1
    all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)

print(f"Combined data: {len(combined_df)} rows")
print(f"Days: {combined_df['day'].unique()}")

btc_data = combined_df[combined_df["symbol"] == "BTC"]
print(btc_data[['day', 'price_usd']])

btc_price_day1 = btc_data[btc_data.day == 1]["price_usd"].iloc[0]
btc_price_day5 = btc_data[btc_data.day == 5]["price_usd"].iloc[0]
btc_price_change = btc_price_day1 - btc_price_day5
print(f"Price Change = {btc_price_change:,.2f}")

btc_percent_change = (btc_price_change / btc_price_day1) * 100
print(f"Percentage Change = {btc_percent_change:,.2f}%")

