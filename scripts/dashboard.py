import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt

#loading the data to pandas df
df = pd.read_csv("D:/0.0 Data Engineering/Projects/Crypto_market_analysis/crypto_market_analysis/data/combined_data.csv")

#creating streamlit sidebar
st.sidebar.title("Crypto Dashboard")
coin_list = df.symbol.unique()
selected_coin = st.sidebar.selectbox("Choose a coin", coin_list)

#filtering sidebar data
coin_df = df[df.symbol == selected_coin]

#adding title
st.title(f"{selected_coin}  Price Dashboard")

st.subheader("Price Over Time")
st.line_chart(coin_df.set_index('date')['price_usd'])
