import math
import statistics

# Financial Calculations

def present_value(fv, rate, periods):
    """
    Calculate the Present Value (PV) of a future amount.
    :param fv: Future Value
    :param rate: Discount rate per period
    :param periods: Number of periods
    :return: Present Value
    """
    return fv / ((1 + rate) ** periods)

def future_value(pv, rate, periods):
    """
    Calculate the Future Value (FV) of a present amount.
    :param pv: Present Value
    :param rate: Interest rate per period
    :param periods: Number of periods
    :return: Future Value
    """
    return pv * ((1 + rate) ** periods)

def net_present_value(cash_flows, rate):
    """
    Calculate the Net Present Value (NPV) of a series of cash flows.
    :param cash_flows: List of cash flows (including initial investment as negative)
    :param rate: Discount rate per period
    :return: NPV
    """
    npv = 0
    for i, cf in enumerate(cash_flows):
        npv += cf / ((1 + rate) ** i)
    return npv

def internal_rate_of_return(cash_flows, max_iterations=1000, tolerance=0.0001):
    """
    Calculate the Internal Rate of Return (IRR) using the Newton-Raphson method.
    :param cash_flows: List of cash flows (including initial investment as negative)
    :param max_iterations: Maximum number of iterations
    :param tolerance: Tolerance level for convergence
    :return: IRR (approximate)
    """
    guess = 0.1
    for _ in range(max_iterations):
        npv = sum(cf / ((1 + guess) ** i) for i, cf in enumerate(cash_flows))
        derivative = sum(-i * cf / ((1 + guess) ** (i + 1)) for i, cf in enumerate(cash_flows))
        new_guess = guess - npv / derivative
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess
    return guess

# Stock Metrics

def daily_returns(prices):
    """
    Calculate daily returns from a list of stock prices.
    :param prices: List of stock prices
    :return: List of daily returns
    """
    returns = []
    for i in range(1, len(prices)):
        returns.append((prices[i] - prices[i - 1]) / prices[i - 1])
    return returns

def volatility(returns):
    """
    Calculate the volatility (standard deviation) of returns.
    :param returns: List of returns
    :return: Volatility (standard deviation)
    """
    return statistics.stdev(returns)

def sharpe_ratio(returns, risk_free_rate):
    """
    Calculate the Sharpe ratio.
    :param returns: List of returns
    :param risk_free_rate: Risk-free rate
    :return: Sharpe ratio
    """
    mean_return = statistics.mean(returns)
    return (mean_return - risk_free_rate) / volatility(returns)

# Bond Pricing

def bond_price(face_value, coupon_rate, years_to_maturity, market_rate):
    """
    Calculate the current price of a bond.
    :param face_value: Face value of the bond
    :param coupon_rate: Annual coupon rate (as a decimal)
    :param years_to_maturity: Years to maturity
    :param market_rate: Market interest rate (as a decimal)
    :return: Bond price
    """
    coupon_payment = face_value * coupon_rate
    price = 0
    for t in range(1, years_to_maturity + 1):
        price += coupon_payment / ((1 + market_rate) ** t)
    price += face_value / ((1 + market_rate) ** years_to_maturity)
    return price

# Portfolio Analysis

def portfolio_analysis(stock_prices, weights):
    """
    Analyze a portfolio of stocks.
    :param stock_prices: List of lists, where each inner list contains prices for a stock
    :param weights: List of weights for each stock in the portfolio
    :return: Dictionary with portfolio return and risk
    """
    portfolio_returns = []
    for i in range(len(stock_prices[0]) - 1):
        daily_return = 0
        for j in range(len(stock_prices)):
            daily_return += weights[j] * (stock_prices[j][i + 1] - stock_prices[j][i]) / stock_prices[j][i]
        portfolio_returns.append(daily_return)
    portfolio_return = statistics.mean(portfolio_returns)
    portfolio_risk = statistics.stdev(portfolio_returns)
    return {"Portfolio Return": portfolio_return, "Portfolio Risk": portfolio_risk}

# Loan Amortization

def loan_amortization(principal, annual_rate, years):
    """
    Generate a loan amortization schedule.
    :param principal: Loan amount
    :param annual_rate: Annual interest rate (as a decimal)
    :param years: Loan term in years
    :return: List of dictionaries representing the payment schedule
    """
    monthly_rate = annual_rate / 12
    months = years * 12
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** (-months))
    schedule = []
    remaining_balance = principal
    for month in range(1, months + 1):
        interest_payment = remaining_balance * monthly_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        schedule.append({
            "Month": month,
            "Payment": monthly_payment,
            "Principal": principal_payment,
            "Interest": interest_payment,
            "Remaining Balance": remaining_balance
        })
    return schedule

# Risk Metrics

def beta(stock_returns, market_returns):
    """
    Calculate the beta of a stock.
    :param stock_returns: List of stock returns
    :param market_returns: List of market returns
    :return: Beta
    """
    covariance = sum((s - statistics.mean(stock_returns)) * (m - statistics.mean(market_returns)) for s, m in zip(stock_returns, market_returns)) / len(stock_returns)
    market_variance = statistics.variance(market_returns)
    return covariance / market_variance

def standard_deviation(returns):
    """
    Calculate the standard deviation of returns.
    :param returns: List of returns
    :return: Standard deviation
    """
    return statistics.stdev(returns)

# Example Usage

if __name__ == "__main__":
    # Example usage of functions
    print("Present Value:", present_value(1000, 0.05, 5))
    print("Future Value:", future_value(1000, 0.05, 5))
    print("Net Present Value:", net_present_value([-1000, 200, 300, 400, 500], 0.05))
    print("Internal Rate of Return:", internal_rate_of_return([-1000, 200, 300, 400, 500]))
    print("Daily Returns:", daily_returns([100, 102, 105, 107, 110]))
    print("Volatility:", volatility([0.02, 0.03, 0.01, 0.02]))
    print("Sharpe Ratio:", sharpe_ratio([0.02, 0.03, 0.01, 0.02], 0.01))
    print("Bond Price:", bond_price(1000, 0.05, 10, 0.04))
    print("Portfolio Analysis:", portfolio_analysis([[100, 102, 105], [200, 205, 210]], [0.5, 0.5]))
    print("Loan Amortization:", loan_amortization(10000, 0.05, 5))
    print("Beta:", beta([0.02, 0.03, 0.01], [0.01, 0.02, 0.015]))
    print("Standard Deviation:", standard_deviation([0.02, 0.03, 0.01]))