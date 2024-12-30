import requests
import pandas as pd
import os
import streamlit as st


API_KEY = st.secrets["COINGECKO_API_KEY"]

@st.cache_data
def get_crypto_list():
    try:
        url = f"https://api.coingecko.com/api/v3/coins/list?x_cg_demo_api_key={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return [crypto['id'] for crypto in response.json()]
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching cryptocurrency list: {e}")
        return []

def get_crypto_fees(crypto_ids):
    # Mock data for transaction fees
    mock_fees = {
        "bitcoin": 1.5,
        "ethereum": 0.8,
        "ripple": 0.05,
        "litecoin": 0.2,
        "dogecoin": 0.01
    }
    # Return fees for the requested cryptocurrencies
    return {crypto: mock_fees.get(crypto, "N/A") for crypto in crypto_ids}

def get_crypto_price(crypto_ids):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": ",".join(crypto_ids), "vs_currencies": "usd", "x_cg_demo_api_key": API_KEY}
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else None

def get_crypto_history(crypto_id, days="max"):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart"
    params = {"vs_currency": "usd", "days": days, "x_cg_demo_api_key": API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['prices'], columns=["timestamp", "price"])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    return None

def get_crypto_blockchains(crypto_ids):
    """
    Fetch blockchain/platform details for the given cryptocurrencies from CoinGecko.
    """
    blockchains = {}
    print(crypto_ids)
    for crypto in crypto_ids:
        try:
            url = f"https://api.coingecko.com/api/v3/coins/{crypto}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                platform = data.get("platforms", {}).keys()  # Get platform/blockchain details
                blockchains[crypto] = ", ".join(platform) if platform else "Native Blockchain"
            else:
                blockchains[crypto] = "Unknown"
        except Exception as e:
            blockchains[crypto] = f"Error: {e}"
    return blockchains