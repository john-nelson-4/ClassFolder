# This program prints "Hello, World!" to the screen
print("Hello, World!")

# Input: Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Process: Multiply the numbers
product = num1 * num2

# Output: Display the result
print(f"The product of {num1} and {num2} is {product}")

# Input: Get future cash flow, discount rate, and number of periods
future_cash_flow = float(input("Enter the future cash flow (FCF): "))
discount_rate = float(input("Enter the discount rate (as a percentage, e.g., 5 for 5%): ")) / 100
num_periods = int(input("Enter the number of periods: "))

# Process: Calculate the present value
present_value = future_cash_flow / (1 + discount_rate) ** num_periods

# Output: Display the result
print(f"The present value of the future cash flow is: ${present_value:.2f}")

