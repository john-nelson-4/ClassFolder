import numpy as np

# 1. Portfolio Tracker
symbols = ['AAPL', 'MSFT', 'GOOGL']
quantities = [100, 50, 75]
prices = [190.50, 375.00, 140.50]

position_values = [q * p for q, p in zip(quantities, prices)]
total_value = sum(position_values)

print("Portfolio Value:", total_value)

# 2. Moving Average Calculator
historical_prices = [100, 102, 101, 105, 107, 110, 112, 115, 117, 120]
def moving_average(prices, window):
    return [np.mean(prices[i-window:i]) for i in range(window, len(prices)+1)]

ma5 = moving_average(historical_prices, 5)
ma20 = moving_average(historical_prices, 20) if len(historical_prices) >= 20 else []

signals = ["BUY" if ma5[i] > ma20[i] else "SELL" for i in range(len(ma5))] if ma20 else []
print("5-day MA:", ma5)
print("Signals:", signals)

# 3. Bond Calculator
bonds = [[1000, 0.05, 10], [1000, 0.06, 5]]  # [Face Value, Coupon, Maturity]
def calculate_ytm(face, coupon, years, price=1000):
    return (coupon * face + (face - price) / years) / ((face + price) / 2)

ytms = [calculate_ytm(*bond) for bond in bonds]
print("Yields to Maturity:", ytms)

# 4. Price Analyzer
daily_prices = np.array([100, 102, 101, 105, 107, 110, 112, 115, 117, 120])
daily_returns = np.diff(daily_prices) / daily_prices[:-1]

print("Highest Price:", np.max(daily_prices), "at index", np.argmax(daily_prices))
print("Lowest Price:", np.min(daily_prices), "at index", np.argmin(daily_prices))

# 5. Asset Allocation Tool
current_alloc = np.array([0.4, 0.3, 0.3])
target_alloc = np.array([0.5, 0.25, 0.25])
rebalancing = target_alloc - current_alloc
print("Rebalancing Needs:", rebalancing)

# 6. Risk Calculator
returns = np.random.randn(100, 3)  # Simulated returns for 3 assets
correlation_matrix = np.corrcoef(returns.T)
volatility = np.std(returns, axis=0)

print("Correlation Matrix:\n", correlation_matrix)
print("Portfolio Volatility:", volatility)
