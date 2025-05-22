import requests
import os
from dotenv import load_dotenv

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

for coin in data["data"]:
    name = coin["name"]
    price = coin["quote"]["USD"]["price"]
    print(f"{name}: ${price:,.3f}")

