# Ask the user to input the stock price (float)
stock_price = float(input("Enter the stock price: "))  # Convert user input to a float

# Ask the user to input the number of shares (int)
number_of_shares = int(input("Enter the number of shares: "))  # Convert user input to an integer

# Ask the user to input the company ticker symbol (string)
company_ticker = input("Enter the company ticker symbol: ")  # Input is already a string

# Print the variables to confirm the values entered
print("\nHere are the values you entered:")
print("Stock Price:", stock_price)
print("Number of Shares:", number_of_shares)
print("Company Ticker Symbol:", company_ticker)
# Ask the user to input the stock price (float)
stock_price = float(input("Enter the stock price: "))  

# Ask the user to input the number of shares (int)
number_of_shares = int(input("Enter the number of shares: "))  

# Ask the user to input the company ticker symbol (string)
company_ticker = input("Enter the company ticker symbol: ")  

# Calculate the total value of the stock position
total_value = stock_price * number_of_shares

# Display the result
print(f"\nThe total value of your {company_ticker} stock position is: ${total_value:.2f}")

# Get user input
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display result
print(f"The simple interest for a principal of ${principal:.2f} at {rate}% for {time} years is: ${simple_interest:.2f}")

# Fixed exchange rate from USD to EUR (example: 1 USD = 0.85 EUR)
exchange_rate = 0.85

# Get user input
usd_amount = float(input("Enter the amount in USD: "))

# Convert to EUR
eur_amount = usd_amount * exchange_rate

# Display result
print(f"{usd_amount} USD is equivalent to {eur_amount:.2f} EUR")

# Get user input
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the number of years: "))

# Calculate future value
future_value = principal * (1 + rate / 100) ** years

# Display result
print(f"The future value of the investment is: ${future_value:.2f}")
# Get user input
principal = float(input("Enter the loan principal amount: "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the loan term in years: "))

# Calculate the monthly interest rate
monthly_rate = annual_rate / 100 / 12

# Calculate the total number of payments (months)
months = years * 12

# Calculate the monthly payment using the formula
monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

# Display result
print(f"The monthly loan payment is: ${monthly_payment:.2f}")
