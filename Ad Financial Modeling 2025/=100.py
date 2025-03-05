# Input: Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Process: Multiply the numbers
product = num1 * num2 * num3

# Output: Check if the product equals 100
if product == 100:
    print(f"The product of {num1}, {num2}, and {num3} equals 100!")
else:
    print(f"The product of {num1}, {num2}, and {num3} is {product}, which does not equal 100.")
