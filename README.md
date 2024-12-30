# Cryptocurrency Dashboard and Tax Calculator

This project is a Streamlit-based web application for tracking cryptocurrency prices, calculating taxes on cryptocurrency transactions, and exploring historic data. It also includes an integrated chatbot for assistance.

## Features

### 1. **Prices Tab**
- View real-time cryptocurrency prices.
- Select multiple cryptocurrencies to compare.
- Visualize historic trends with interactive charts.

### 2. **Tax Calculator Tab**
- Calculate taxes on cryptocurrency transactions.
- Input details like buy price, sell price, quantity, and fees.
- Get total gains/losses and tax amounts.

### 3. **Historic Data Tab**
- Fetch and display historic price data for selected cryptocurrencies.

### 4. **Chatbot Integration**
- Interact with a chatbot powered by OpenAI for assistance.

## Setup and Installation

### Prerequisites
- Python 3.9 or higher
- API keys for:
  - [CoinGecko API](https://www.coingecko.com/en/api)
  - [OpenAI API](https://openai.com/api/)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cryptocurrency-dashboard.git
   cd cryptocurrency-dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.streamlit/secrets.toml` file.
   - Add your API keys:
     ```toml
     [secrets]
     COINGECKO_API_KEY = "your_coingecko_api_key"
     OPENAI_API_KEY = "your_openai_api_key"
     ```

4. Run the application:
   ```bash
   streamlit run main.py
   ```

## Project Structure

```
.
├── main.py                   # Main application script
├── requirements.txt          # Python dependencies
├── utils/
│   ├── api.py                # API-related utility functions
│   ├── calculations.py       # Tax calculation logic
│   ├── chatbot.py            # Chatbot integration
│   ├── translations.py       # Language translations
│   ├── visualization.py      # Visualization and charting functions
└── .streamlit/
    └── secrets.toml          # API secrets (not included in version control)
```

## Usage

1. **Prices Tab**:
   - Select cryptocurrencies and a time range.
   - View interactive charts and detailed price, fee, and blockchain information.

2. **Tax Calculator Tab**:
   - Enter transaction details to calculate taxes.

3. **Historic Data Tab**:
   - Select a cryptocurrency and time range to view historic price data.

4. **Chatbot**:
   - Use the chatbot for help or guidance on cryptocurrency-related queries.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/)
- [Streamlit Option Menu](https://github.com/victoryhb/streamlit-option-menu)
- [OpenAI API](https://openai.com/api/)

## Future Improvements

- Add more advanced analytics for cryptocurrencies.
- Include support for additional APIs.
- Enhance chatbot capabilities.