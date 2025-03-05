import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf
from datetime import datetime, timedelta

# Set your API key (if needed for external API calls)
API_KEY = "EYJDZ6HFWO4REUT1"

st.title("Comprehensive Stock Analysis Dashboard")

# Sidebar inputs
stock_symbol = st.sidebar.text_input("Stock Symbol", value="AAPL")
start_date = st.sidebar.date_input("Start Date", value=datetime.now() - timedelta(days=365))
end_date = st.sidebar.date_input("End Date", value=datetime.now())
portfolio_symbols = st.sidebar.text_input("Portfolio Symbols (comma-separated)", value="AAPL, MSFT, GOOGL")

# Cache function for downloading data
@st.cache_data(show_spinner=False)
def get_data(symbol, start, end):
    try:
        df = yf.download(symbol, start=start, end=end)
    except Exception as e:
        st.error(f"Error downloading data for {symbol}: {e}")
        df = pd.DataFrame()
    return df

# Main stock data
data = get_data(stock_symbol, start_date, end_date)
if data.empty:
    st.error(f"No data returned for {stock_symbol}.")
    st.stop()

### Price Chart with Moving Averages
st.header("Price Chart with Moving Averages")
data['MA50'] = data['Adj Close'].rolling(window=50).mean()
data['MA200'] = data['Adj Close'].rolling(window=200).mean()
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(data.index, data['Adj Close'], label='Price')
ax.plot(data.index, data['MA50'], label='50-day MA')
ax.plot(data.index, data['MA200'], label='200-day MA')
ax.set_title(f"{stock_symbol} Price Chart with Moving Averages")
ax.set_xlabel("Date")
ax.set_ylabel("Price ($)")
ax.legend()
ax.grid(True)
st.pyplot(fig)

### Volume Analysis
st.header("Volume Analysis")
fig2, ax2 = plt.subplots(figsize=(12, 4))
ax2.bar(data.index, data['Volume'])
ax2.set_title(f"{stock_symbol} Trading Volume")
ax2.set_xlabel("Date")
ax2.set_ylabel("Volume")
st.pyplot(fig2)

### Returns Distribution
st.header("Returns Distribution")
data['Returns'] = data['Adj Close'].pct_change()
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.histplot(data['Returns'].dropna(), kde=True, ax=ax3)
ax3.set_title("Distribution of Daily Returns")
ax3.set_xlabel("Returns")
st.pyplot(fig3)

### Technical Indicators
st.header("Technical Indicators")

# RSI Calculation
def compute_rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

data['RSI'] = compute_rsi(data['Adj Close'])
fig4, ax4 = plt.subplots(figsize=(12, 4))
ax4.plot(data.index, data['RSI'], label='RSI')
ax4.axhline(70, color='red', linestyle='--')
ax4.axhline(30, color='green', linestyle='--')
ax4.set_title("Relative Strength Index (RSI)")
ax4.set_xlabel("Date")
ax4.set_ylabel("RSI")
ax4.legend()
st.pyplot(fig4)

# MACD Calculation
exp1 = data['Adj Close'].ewm(span=12, adjust=False).mean()
exp2 = data['Adj Close'].ewm(span=26, adjust=False).mean()
data['MACD'] = exp1 - exp2
data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
fig5, ax5 = plt.subplots(figsize=(12, 4))
ax5.plot(data.index, data['MACD'], label='MACD')
ax5.plot(data.index, data['Signal_Line'], label='Signal Line')
ax5.set_title("MACD")
ax5.set_xlabel("Date")
ax5.legend()
st.pyplot(fig5)

### Portfolio Visualization Tool
st.header("Portfolio Visualization Tool")
portfolio_list = [s.strip() for s in portfolio_symbols.split(',') if s.strip()]

@st.cache_data(show_spinner=False)
def get_portfolio_data(symbols, start, end):
    try:
        df = yf.download(symbols, start=start, end=end)['Adj Close']
    except Exception as e:
        st.error(f"Error downloading portfolio data: {e}")
        df = pd.DataFrame()
    return df

portfolio_data = get_portfolio_data(portfolio_list, start_date, end_date)
if portfolio_data.empty:
    st.error("No portfolio data available.")
else:
    # Performance Comparison
    st.subheader("Performance Comparison")
    portfolio_returns = portfolio_data.pct_change().dropna()
    cumulative_returns = (1 + portfolio_returns).cumprod() - 1
    fig6, ax6 = plt.subplots(figsize=(12, 6))
    for col in cumulative_returns.columns:
        ax6.plot(cumulative_returns.index, cumulative_returns[col], label=col)
    ax6.set_title("Cumulative Returns Comparison")
    ax6.set_xlabel("Date")
    ax6.set_ylabel("Cumulative Returns")
    ax6.legend()
    st.pyplot(fig6)

    # Risk-Return Scatter Plot
    st.subheader("Risk-Return Scatter Plot")
    annual_returns = portfolio_returns.mean() * 252
    annual_volatility = portfolio_returns.std() * np.sqrt(252)
    fig7, ax7 = plt.subplots(figsize=(8, 6))
    ax7.scatter(annual_volatility, annual_returns)
    for i, txt in enumerate(annual_returns.index):
        ax7.annotate(txt, (annual_volatility.iloc[i], annual_returns.iloc[i]))
    ax7.set_title("Risk vs. Return")
    ax7.set_xlabel("Annualized Volatility")
    ax7.set_ylabel("Annualized Return")
    st.pyplot(fig7)

    # Asset Allocation Pie Chart (Equal weights for demonstration)
    st.subheader("Asset Allocation")
    weights = np.array([1/len(portfolio_list)] * len(portfolio_list))
    fig8, ax8 = plt.subplots(figsize=(6,6))
    ax8.pie(weights, labels=portfolio_list, autopct='%1.1f%%', startangle=90)
    ax8.set_title("Asset Allocation (Equal Weights)")
    st.pyplot(fig8)

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    corr = portfolio_data.corr()
    fig9, ax9 = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax9)
    ax9.set_title("Portfolio Correlation Matrix")
    st.pyplot(fig9)

### Candlestick Charts
st.header("Candlestick Chart with Volume Overlay")
# Prepare a clean DataFrame with only the OHLCV columns
ohlc = data[['Open', 'High', 'Low', 'Close', 'Volume']].copy()
ohlc = ohlc.apply(pd.to_numeric, errors='coerce')
ohlc.dropna(subset=['Open', 'High', 'Low', 'Close', 'Volume'], inplace=True)
# Optional: Compute a pivot for support/resistance (example calculation)
ohlc['Pivot'] = (ohlc['High'] + ohlc['Low'] + ohlc['Close']) / 3

mc = mpf.make_marketcolors(up='g', down='r', inherit=True)
s_style = mpf.make_mpf_style(marketcolors=mc)

fig_candle = mpf.figure(style=s_style, figsize=(12,8))
ax_main = fig_candle.add_subplot(2,1,1)
ax_vol = fig_candle.add_subplot(2,1,2, sharex=ax_main)

# IMPORTANT: Use the cleaned "ohlc" DataFrame here, not "data"
mpf.plot(ohlc, type='candle', ax=ax_main, volume=ax_vol, style=s_style, show_nontrading=True)
st.pyplot(fig_candle)

### Optional: Market Analysis Visualizations
st.header("Market Analysis Visualizations (Optional)")
indices = ['^GSPC', '^DJI', '^IXIC']  # Major indices
index_data = yf.download(indices, start=start_date, end=end_date)['Adj Close']
index_corr = index_data.corr()
fig11, ax11 = plt.subplots(figsize=(8, 6))
sns.heatmap(index_corr, annot=True, cmap='coolwarm', ax=ax11)
ax11.set_title("Index Correlation Heatmap")
st.pyplot(fig11)

### Optional: Risk Analysis Charts
st.header("Risk Analysis Charts (Optional)")
def calculate_var(returns, confidence=0.05):
    return returns.quantile(confidence)

var_value = calculate_var(data['Returns'].dropna())
st.write(f"Value at Risk (VaR) at 95% confidence: {var_value:.2%}")
fig12, ax12 = plt.subplots(figsize=(10,6))
sns.histplot(data['Returns'].dropna(), kde=True, ax=ax12)
ax12.axvline(var_value, color='red', linestyle='--', label=f'VaR (95%): {var_value:.2%}')
ax12.set_title("Returns Distribution with VaR")
ax12.legend()
st.pyplot(fig12)

st.subheader("Volatility Analysis")
data['Volatility'] = data['Returns'].rolling(window=21).std() * np.sqrt(252)
fig13, ax13 = plt.subplots(figsize=(12,4))
ax13.plot(data.index, data['Volatility'], label='21-day Rolling Volatility')
ax13.set_title("Volatility Analysis")
ax13.set_xlabel("Date")
ax13.set_ylabel("Annualized Volatility")
ax13.legend()
st.pyplot(fig13)

### Optional: Options Analysis Dashboard
st.header("Options Analysis Dashboard (Optional)")
ticker = yf.Ticker(stock_symbol)
options_dates = ticker.options
if options_dates:
    st.subheader("Option Chain")
    selected_date = st.selectbox("Select Expiration Date", options_dates)
    option_chain = ticker.option_chain(selected_date)
    st.write("Calls", option_chain.calls.head())
    st.write("Puts", option_chain.puts.head())
else:
    st.write("No options data available for this stock.")

st.write("Dashboard built with API Key:", API_KEY)
