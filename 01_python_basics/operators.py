# ==========================================================
# File Name: 02_operators.py
# Description: Demonstration of Python Operators
# ==========================================================


# ----------------------------------------------------------
# 1️⃣ Arithmetic Operators
# Used for mathematical calculations
# ----------------------------------------------------------

product_price = 500
quantity = 3

# Addition
addition_result = product_price + 100
print("Addition:", addition_result)

# Subtraction
discounted_price = product_price - 50
print("Subtraction:", discounted_price)

# Multiplication
total_cost = product_price * quantity
print("Multiplication (Total Cost):", total_cost)

# Division
average_cost = total_cost / quantity
print("Division (Average Cost):", average_cost)

# Floor Division
floor_value = total_cost // quantity
print("Floor Division:", floor_value)

# Modulus (Remainder)
remainder = total_cost % quantity
print("Modulus (Remainder):", remainder)

# Exponentiation (Power)
square_value = 5 ** 2
print("Exponentiation:", square_value)

print("-----------------------------------")


# ----------------------------------------------------------
# 2️⃣ Comparison Operators
# Used to compare values (Returns True or False)
# ----------------------------------------------------------

sales_2024 = 50000
sales_2025 = 65000

print("Equal to:", sales_2024 == sales_2025)
print("Not Equal to:", sales_2024 != sales_2025)
print("Greater than:", sales_2025 > sales_2024)
print("Less than:", sales_2024 < sales_2025)
print("Greater than or Equal to:", sales_2025 >= sales_2024)
print("Less than or Equal to:", sales_2024 <= sales_2025)

print("-----------------------------------")


# ----------------------------------------------------------
# 3️⃣ Logical Operators
# Used to combine conditions
# ----------------------------------------------------------

is_logged_in = True
has_subscription = False

print("AND Operator:", is_logged_in and has_subscription)
print("OR Operator:", is_logged_in or has_subscription)
print("NOT Operator:", not has_subscription)

print("-----------------------------------")


# ----------------------------------------------------------
# 4️⃣ Assignment Operators
# Used to assign and update values
# ----------------------------------------------------------

orders = 100

orders += 20   # orders = orders + 20
print("After += :", orders)

orders -= 10   # orders = orders - 10
print("After -= :", orders)

orders *= 2    # orders = orders * 2
print("After *= :", orders)

orders /= 5    # orders = orders / 5
print("After /= :", orders)

print("-----------------------------------")


# ----------------------------------------------------------
# 5️⃣ Identity Operators
# Used to compare memory location
# ----------------------------------------------------------

x = 10
y = 10

print("x is y:", x is y)
print("x is not y:", x is not y)

print("-----------------------------------")


# ----------------------------------------------------------
# 6️⃣ Membership Operators
# Used to check if value exists in a sequence
# ----------------------------------------------------------

product_list = ["Laptop", "Mobile", "Tablet"]

print("Laptop in list:", "Laptop" in product_list)
print("TV not in list:", "TV" not in product_list)

print("-----------------------------------")


# ==========================================================
# End of Operators Demonstration
# ==========================================================