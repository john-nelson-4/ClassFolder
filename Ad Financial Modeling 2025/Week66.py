print("\n🚀 Script started...")

import requests
import pandas as pd
import matplotlib.pyplot as plt
from config import API_KEY  # Import API key from config.py

# 🔹 Using Alpha Vantage API Key from config.py

# Function to fetch stock data
def get_stock_data(symbol):
    """Fetch historical stock prices from Alpha Vantage."""
    print(f"\n📡 Fetching data for {symbol}...")
    
    try:
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&outputsize=compact"
        response = requests.get(url)
        data = response.json()

        # Check for error messages in the API response
        if "Error Message" in data:
            print(f"❌ Error: {data['Error Message']}")
            return None
        elif "Note" in data:
            print(f"⚠️ API Note: {data['Note']}")
            # Continue processing if it's just a warning about API call frequency
        
        if "Time Series (Daily)" not in data:
            print(f"❌ Error: Could not fetch data for {symbol}")
            print(f"API Response: {data}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error: {e}")
        return None
    except ValueError as e:
        print(f"❌ JSON Parsing Error: {e}")
        return None

    df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()

    print(f"✅ Data for {symbol} fetched successfully!")
    print(df.head())  # Display first few rows

    return df

# Function to calculate daily returns
def calculate_daily_returns(data):
    """Calculate daily percentage returns."""
    print("\n📊 Calculating daily returns...")
    daily_returns = data["4. close"].pct_change().dropna()
    print(daily_returns.head())  # Print sample returns
    return daily_returns

# Function to calculate moving averages
def calculate_moving_averages(df, short_window=5, long_window=20):
    """Calculate moving averages."""
    print("\n📈 Calculating Moving Averages...")
    short_ma = df["4. close"].rolling(window=short_window).mean()
    long_ma = df["4. close"].rolling(window=long_window).mean()
    return short_ma, long_ma

# Function to generate trading signals
def generate_trading_signal(short_ma, long_ma):
    """Generate buy/sell trading signals."""
    print("\n🔔 Generating trading signals...")
    signal = (short_ma > long_ma).astype(int).diff()
    print(signal.dropna().head())  # Show sample signals
    return signal

# Function to calculate portfolio value
def calculate_portfolio_value(data, holdings):
    """Calculate total portfolio value."""
    print("\n💰 Calculating portfolio value...")
    total_value = 0
    
    for ticker in holdings:
        if ticker in data and data[ticker] is not None:
            total_value += holdings[ticker] * data[ticker]["4. close"].iloc[-1]
        else:
            print(f"⚠️ Warning: No data available for {ticker}, skipping in portfolio calculation")
    
    print(f"📌 Total Portfolio Value: ${total_value:.2f}")
    return total_value

# Function to calculate Sharpe Ratio
def calculate_sharpe_ratio(daily_returns, risk_free_rate=0.02):
    """Calculate the Sharpe Ratio."""
    print("\n📊 Calculating Sharpe Ratio...")
    excess_return = daily_returns.mean() - risk_free_rate / 252
    sharpe_ratio = excess_return / daily_returns.std()
    print(f"📌 Sharpe Ratio: {sharpe_ratio:.4f}")
    return sharpe_ratio

# Function to plot stock data
def plot_stock(data, short_ma, long_ma, ticker):
    """Plot stock prices with moving averages."""
    print(f"\n📈 Plotting {ticker} stock price and moving averages...")
    plt.figure(figsize=(12,6))
    plt.plot(data["4. close"], label=f"{ticker} Price", color="blue")
    plt.plot(short_ma, label="5-day MA", linestyle="--", color="red")
    plt.plot(long_ma, label="20-day MA", linestyle="--", color="green")
    plt.legend()
    plt.title(f"{ticker} Price & Moving Averages")
    plt.show()

# 🔹 Main script execution
tickers = ["AAPL", "MSFT", "GOOGL"]
holdings = {"AAPL": 100, "MSFT": 50, "GOOGL": 75}

# Fetch data
stock_data = {}
for ticker in tickers:
    stock_data[ticker] = get_stock_data(ticker)

# Portfolio analysis
portfolio_value = calculate_portfolio_value(stock_data, holdings)

# Technical analysis
for ticker in tickers:
    if stock_data[ticker] is not None:
        daily_returns = calculate_daily_returns(stock_data[ticker])
        short_ma, long_ma = calculate_moving_averages(stock_data[ticker])
        signals = generate_trading_signal(short_ma, long_ma)
        
        sharpe_ratio = calculate_sharpe_ratio(daily_returns)

        # Plot data
        plot_stock(stock_data[ticker], short_ma, long_ma, ticker)

print("\n✅ Market Dashboard Execution Completed!")
