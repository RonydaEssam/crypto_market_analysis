import requests
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

# load API_KEY from .env file
load_dotenv()
API_KEY = os.getenv("COINMARKETCAP_API_KEY")

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}

params = {
  'start':'1',
  'limit':'25',
  'convert':'USD'
}

response = requests.get(url, headers=headers, params=params)
data = response.json()



coins = []

for coin in data['data']:
    coin_info = {
        "name": coin["name"],
        "symbol": coin["symbol"],
        "price_usd": coin["quote"]["USD"]["price"],
        "percent_change_24h": coin["quote"]["USD"]["percent_change_24h"],
        "market_cap_usd": coin["quote"]["USD"]["market_cap"]
    }
    coins.append(coin_info)

df = pd.DataFrame(coins)

today = datetime.today().strftime('%Y-%m-%d')
df.insert(0, "date", today)
filename = f"D:/0.0 Data Engineering/Projects/Crypto_market_analysis/crypto_market_analysis/data/prices_{today}.csv"
df.to_csv(filename, index=False)

'''
df1 = pd.read_csv("..\data\prices_2025-05-25.csv")
dated = "2025-05-25"
df1.insert(0, "date", dated)
df1.to_csv("..\data\prices_2025-05-25.csv")
'''

print(df.describe())