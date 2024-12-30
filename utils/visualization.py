import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def create_comparison_chart(crypto_histories):
    """
    Creates a comparison chart for cryptocurrency price histories.

    Parameters:
    crypto_histories (dict): A dictionary where keys are cryptocurrency IDs and values are DataFrames containing 'timestamp' and 'price'.

    Returns:
    plotly.graph_objects.Figure: A Plotly figure object with the comparison chart.
    """
    fig = go.Figure()
    for crypto_id, history in crypto_histories.items():
        fig.add_trace(go.Scatter(
            x=history['timestamp'],
            y=history['price'],
            mode='lines',
            name=crypto_id.capitalize()
        ))
    fig.update_layout(
        title="Comparison of Cryptocurrencies",
        xaxis_title="Date",
        yaxis_title="Price (USD)"
    )
    return fig

def display_crypto_prices(prices, cryptos, fees_data, blockchain_data):
    """
    Displays a table of cryptocurrency prices, fees, and blockchain/platform information.

    Parameters:
    prices (dict): A dictionary with cryptocurrency IDs as keys and price information as values.
    cryptos (list): A list of selected cryptocurrency IDs.
    fees_data (dict): A dictionary with cryptocurrency IDs as keys and fee information as values.
    blockchain_data (dict): A dictionary with cryptocurrency IDs as keys and blockchain/platform information as values.
    """
    if prices:
        data = []
        for crypto in cryptos:
            if crypto in prices:
                price = prices[crypto].get('usd', "N/A")  # Handle missing 'usd' key
                fees = fees_data.get(crypto, "N/A")  # Get fees if available
                blockchain = blockchain_data.get(crypto, "Unknown")  # Get blockchain/platform
                data.append({
                    "Cryptocurrency": crypto.capitalize(),
                    "Price (USD)": price,
                    "Fees (USD)": fees,
                    "Blockchain": blockchain
                })
            else:
                data.append({
                    "Cryptocurrency": crypto.capitalize(),
                    "Price (USD)": "N/A",
                    "Fees (USD)": "N/A",
                    "Blockchain": "Unknown"
                })

        # Convert data to a DataFrame for better display
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.warning("No data available for the selected cryptocurrencies.")