# ==========================================================
# File Name: 01_variables_and_datatypes.py
# Description: Demonstration of Python Variables and Data Types
# Author: Your Name
# ==========================================================


# ----------------------------------------------------------
# 1️⃣ What is a Variable?
# ----------------------------------------------------------
# A variable is a container used to store data.
# Python automatically detects the data type.


# ----------------------------------------------------------
# 2️⃣ Numeric Data Types
# ----------------------------------------------------------

# Integer (Whole numbers)
total_orders = 150
print("Total Orders:", total_orders)
print("Data Type:", type(total_orders))
print("-----------------------------------")

# Float (Decimal numbers)
product_price = 499.99
print("Product Price:", product_price)
print("Data Type:", type(product_price))
print("-----------------------------------")

# Complex (Used rarely in analytics but part of Python)
complex_number = 3 + 5j
print("Complex Number:", complex_number)
print("Data Type:", type(complex_number))
print("-----------------------------------")


# ----------------------------------------------------------
# 3️⃣ Text Data Type
# ----------------------------------------------------------

# String (Text data)
customer_name = "Kornelu"
product_category = "Electronics"

print("Customer Name:", customer_name)
print("Product Category:", product_category)
print("Data Type:", type(customer_name))
print("-----------------------------------")


# ----------------------------------------------------------
# 4️⃣ Boolean Data Type
# ----------------------------------------------------------

# Boolean (True or False)
is_payment_successful = True
is_stock_available = False

print("Payment Successful:", is_payment_successful)
print("Stock Available:", is_stock_available)
print("Data Type:", type(is_payment_successful))
print("-----------------------------------")


# ----------------------------------------------------------
# 5️⃣ Sequence Data Types
# ----------------------------------------------------------

# List (Ordered, Mutable)
sales_list = [2500, 3000, 4000, 1500]
print("Sales List:", sales_list)
print("Data Type:", type(sales_list))
print("-----------------------------------")

# Tuple (Ordered, Immutable)
top_products = ("Laptop", "Mobile", "Tablet")
print("Top Products:", top_products)
print("Data Type:", type(top_products))
print("-----------------------------------")

# Range (Sequence of numbers)
numbers_range = range(1, 6)
print("Range:", list(numbers_range))
print("Data Type:", type(numbers_range))
print("-----------------------------------")


# ----------------------------------------------------------
# 6️⃣ Set Data Type
# ----------------------------------------------------------

# Set (Unordered, No duplicates)
unique_regions = {"North", "South", "East", "West"}
print("Unique Regions:", unique_regions)
print("Data Type:", type(unique_regions))
print("-----------------------------------")


# ----------------------------------------------------------
# 7️⃣ Dictionary Data Type
# ----------------------------------------------------------

# Dictionary (Key-Value pairs)
student_data = {
    "name": "Rahul",
    "age": 21,
    "course": "BCA",
    "marks": 85
}

print("Student Data:", student_data)
print("Data Type:", type(student_data))
print("-----------------------------------")


# ----------------------------------------------------------
# 8️⃣ Type Casting (Type Conversion)
# ----------------------------------------------------------

# Converting integer to float
orders = 100
orders_float = float(orders)

print("Converted to Float:", orders_float)
print("Data Type:", type(orders_float))
print("-----------------------------------")

# Converting float to integer
price = 99.99
price_int = int(price)

print("Converted to Integer:", price_int)
print("Data Type:", type(price_int))
print("-----------------------------------")

# Converting number to string
order_id = 101
order_id_str = str(order_id)

print("Converted to String:", order_id_str)
print("Data Type:", type(order_id_str))
print("-----------------------------------")


# ----------------------------------------------------------
# 9️⃣ Multiple Variable Assignment
# ----------------------------------------------------------

# Assigning multiple values at once
product_name, quantity, discount = "Keyboard", 3, 10

print("Product:", product_name)
print("Quantity:", quantity)
print("Discount:", discount)
print("-----------------------------------")


# ----------------------------------------------------------
# 🔟 Checking Memory ID (Advanced Understanding)
# ----------------------------------------------------------

x = 10
y = 10

print("Memory Address of x:", id(x))
print("Memory Address of y:", id(y))
print("-----------------------------------")


# ==========================================================
# End of Variables and Data Types Demonstration
# ==========================================================