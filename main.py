import plotly.graph_objects as go
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from utils.api import get_crypto_list, get_crypto_price, get_crypto_history, get_crypto_fees, get_crypto_blockchains
from utils.calculations import calculate_crypto_tax
from utils.translations import get_translations
from utils.visualization import create_comparison_chart, display_crypto_prices
from utils.chatbot import chatbot

# Custom Top Navbar
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Cryptocurrency Dashboard and Tax Calculator")

with col2:
    # Language dropdown in the top-right
    language = st.selectbox(
        "Language / Langue",
        ["English", "Français"],
        key="language_select"
    )

# Update language in session state if it changes
if "language" not in st.session_state or language != st.session_state.language:
    st.session_state.language = language

# Load translations based on the selected language
labels = get_translations(st.session_state.language)

# Define global time ranges for all tabs
time_ranges = {
    "1D": "1",
    "1W": "7",
    "1M": "30",
    "1Y": "365",
    "5Y": "1825",
    "ALL": "max"
}

# Initialize context variable
if "app_context" not in st.session_state:
    st.session_state.app_context = {}

# Navbar Menu
selected_nav = option_menu(
    menu_title=None,  # Title for the menu (None to hide)
    options=["Prices", "Tax Calculator", "Historic"],  # Navigation tabs
    icons=["currency-bitcoin", "calculator", "bar-chart"],  # Optional: Add icons for tabs
    menu_icon="cast",  # Icon for the menu
    default_index=0,  # Default active tab
    orientation="horizontal",  # Display the menu horizontally
)

# Display the selected tab
if selected_nav == "Prices":
    st.header(labels["prices"])
    st.session_state.app_context["tab"] = "prices"

    # Fetch cryptos
    crypto_list = get_crypto_list()
    default_cryptos = ["bitcoin", "ethereum", "binancecoin", "cardano", "solana"]
    cryptos = st.multiselect(labels["crypto_selection"], crypto_list, default_cryptos, key="crypto_select")

    # Time ranges
    selected_time_range = st.selectbox(labels["time_range"], options=list(time_ranges.keys()), index=2, key="time_range_select")

    if cryptos:
        histories = {crypto: get_crypto_history(crypto, time_ranges[selected_time_range]) for crypto in cryptos}
        fig = create_comparison_chart(histories)
        st.plotly_chart(fig, use_container_width=True)

        prices = get_crypto_price(cryptos)
        fees_data = get_crypto_fees(cryptos)
        blockchain_data = get_crypto_blockchains(cryptos)
        display_crypto_prices(prices, cryptos, fees_data, blockchain_data)

        # Update context for Prices tab
        st.session_state.app_context.update({
            "selected_cryptos": cryptos,
            "selected_time_range": selected_time_range,
            "price_data": prices,
            "fees_data": fees_data,
            "blockchain_data": blockchain_data,
        })
    else:
        st.warning(labels["crypto_selection"])

elif selected_nav == "Tax Calculator":
    st.header(labels["tax_calculator"])
    st.session_state.app_context["tab"] = "tax_calculator"

    # Inputs for tax calculation
    crypto = st.selectbox(labels["crypto_selection"], get_crypto_list(), key="tax_crypto_select")
    buy_price = st.number_input(labels["buy_price"], min_value=0.0, step=0.01)
    sell_price = st.number_input(labels["sell_price"], min_value=0.0, step=0.01)
    quantity = st.number_input(labels["quantity"], min_value=0.0, step=0.01)
    fees = st.number_input(labels["fees"], min_value=0.0, step=0.01)
    tax_rate = st.slider(labels["tax_rate"], min_value=0, max_value=50, value=20)

    if st.button(labels["calculate_tax"], key="calculate_tax_button"):
        gain_loss, tax = calculate_crypto_tax(buy_price, sell_price, quantity, fees, tax_rate)
        st.write(f"{labels['tax_gain_loss']}: ${gain_loss:,.2f}")
        st.write(f"{labels['tax_amount']}: ${tax:,.2f}")

        # Update context for Tax Calculator tab
        st.session_state.app_context.update({
            "selected_crypto": crypto,
            "buy_price": buy_price,
            "sell_price": sell_price,
            "quantity": quantity,
            "fees": fees,
            "tax_rate": tax_rate,
            "gain_loss": gain_loss,
            "tax": tax,
        })

elif selected_nav == "Historic":
    st.header(labels["historic"])
    st.session_state.app_context["tab"] = "historic"

    # Inputs for historic data
    crypto = st.selectbox(labels["select_crypto_history"], get_crypto_list(), key="historic_crypto_select")
    selected_time_range = st.selectbox(labels["time_range"], options=list(time_ranges.keys()), key="historic_time_range_select")

    if crypto:
        history = get_crypto_history(crypto, time_ranges[selected_time_range])
        st.dataframe(history)

        # Update context for Historic tab
        st.session_state.app_context.update({
            "selected_crypto": crypto,
            "selected_time_range": selected_time_range,
            "historic_data": history.to_dict() if history is not None else None,
        })

# Pass context to chatbot
chatbot(chat_context=st.session_state.app_context)