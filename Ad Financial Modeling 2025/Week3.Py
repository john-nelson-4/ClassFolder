# Take stock price as input
price = float(input("Enter the stock price: "))

# Check the price category
if price > 100:
    print("High-priced stock")
elif 50 <= price <= 100:
    print("Medium-priced stock")
else:
    print("Low-priced stock")

# Get user inputs
P = float(input("Enter the principal amount: "))  # Initial investment
r = float(input("Enter the annual interest rate (in %): ")) / 100  # Convert percentage to decimal
n = int(input("Enter the number of times interest is compounded per year: "))
t = int(input("Enter the number of years: "))

# Initialize amount
A = P  

# Calculate compound interest using a loop
for year in range(1, t + 1):
    A *= (1 + r / n) ** n  # Apply compound interest
    print(f"Year {year}: ${A:.2f}")  # Print balance at the end of each year

# Final result
print(f"\nFinal amount after {t} years: ${A:.2f}")

# List of stock prices (can be modified or taken as input)
stock_prices = [150, 155, 160, 145, 170, 165, 180, 175, 140, 155]

# Find highest and lowest prices
highest_price = max(stock_prices)
lowest_price = min(stock_prices)

# Calculate average price
average_price = sum(stock_prices) / len(stock_prices)

# Count the number of days the price was above average
above_avg_days = sum(1 for price in stock_prices if price > average_price)

# Display results
print(f"Highest stock price: ${highest_price}")
print(f"Lowest stock price: ${lowest_price}")
print(f"Average stock price: ${average_price:.2f}")
print(f"Number of days stock price was above average: {above_avg_days}")


# List of daily stock prices (sample data)
stock_prices = [145, 148, 152, 160, 155, 140, 135, 170, 175, 180, 165, 155]

# Trading variables
cash = 1000  # Starting cash balance ($)
shares_held = 0  # Number of shares owned
portfolio_value = []  # To track portfolio value over time

# Trading loop
for day, price in enumerate(stock_prices):
    if price < 150:  # Buy condition
        if cash >= price:
            shares_held += 1
            cash -= price
            print(f"Day {day + 1}: Bought 1 share at ${price}")
    elif price > 170 and shares_held > 0:  # Sell condition
        shares_held -= 1
        cash += price
        print(f"Day {day + 1}: Sold 1 share at ${price}")

    # Calculate total portfolio value (cash + stock holdings)
    total_value = cash + (shares_held * price)
    portfolio_value.append(total_value)

# Final results
print("\nFinal Portfolio Summary:")
print(f"Cash balance: ${cash:.2f}")
print(f"Shares held: {shares_held}")
print(f"Final portfolio value: ${portfolio_value[-1]:.2f}")


# Investment details input
principal = float(input("Enter initial investment ($): "))
monthly_contribution = float(input("Enter monthly contribution ($): "))
annual_interest_rate = float(input("Enter annual interest rate (%): ")) / 100
years = int(input("Enter number of years: "))

# Constants
n = 12  # Compounded monthly
t = years

# Future Value calculation with monthly contributions
future_value = principal * (1 + annual_interest_rate/n) ** (n*t)  # Grows initial investment

for month in range(1, n*t + 1):
    future_value += monthly_contribution * (1 + annual_interest_rate/n) ** (n*t - month)

# Display results
print(f"\nTotal future value of investment: ${future_value:.2f}")


# User inputs
principal = float(input("Enter loan amount ($): "))
annual_interest_rate = float(input("Enter annual interest rate (%): ")) / 100
years = int(input("Enter loan duration (years): "))

# Calculations
monthly_interest_rate = annual_interest_rate / 12
num_payments = years * 12

# Calculate fixed monthly payment using amortization formula
monthly_payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / \
                  ((1 + monthly_interest_rate) ** num_payments - 1)

# Display results
print(f"\nMonthly Payment: ${monthly_payment:.2f}\n")
print("Payment Schedule:")
print("=" * 40)
print(f"{'Month':<10}{'Payment':<15}{'Remaining Balance'}")
print("=" * 40)

# Track balance over time
remaining_balance = principal
for month in range(1, num_payments + 1):
    interest_paid = remaining_balance * monthly_interest_rate
    principal_paid = monthly_payment - interest_paid
    remaining_balance -= principal_paid

    # Display month-wise payment details
    print(f"{month:<10}${monthly_payment:<12.2f}${remaining_balance:.2f}")

    # Stop loop if the loan is fully paid
    if remaining_balance <= 0:
        break
