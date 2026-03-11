# ---------------------------------------------
# Python Tuple Practice Program
# This program demonstrates tuple creation,
# indexing, slicing, and tuple methods
# ---------------------------------------------

# ---------------------------------------------
# Creating a tuple
# Example: storing days of week
# ---------------------------------------------
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

print("Tuple:", days)


# ---------------------------------------------
# Accessing elements using indexing
# ---------------------------------------------
print("First day:", days[0])
print("Last day:", days[-1])


# ---------------------------------------------
# Slicing tuple
# ---------------------------------------------
print("First three days:", days[0:3])
print("Last two days:", days[3:])


# ---------------------------------------------
# Tuple length
# ---------------------------------------------
print("Total days:", len(days))


# ---------------------------------------------
# Checking if item exists in tuple
# ---------------------------------------------
if "Monday" in days:
    print("Monday is present")


# ---------------------------------------------
# Tuple with numbers
# Example: storing product prices
# ---------------------------------------------
prices = (199, 299, 399, 499, 299, 199)

print("Prices:", prices)


# ---------------------------------------------
# count() method
# Counts how many times value appears
# ---------------------------------------------
print("Count of 199:", prices.count(199))


# ---------------------------------------------
# index() method
# Finds position of value
# ---------------------------------------------
print("Index of 399:", prices.index(399))


# ---------------------------------------------
# Tuple cannot be modified (immutable)
# So we convert to list to modify
# ---------------------------------------------
prices_list = list(prices)

prices_list.append(599)

prices = tuple(prices_list)

print("Updated tuple:", prices)


# ---------------------------------------------
# Real-world example: Student data
# ---------------------------------------------
student = ("Ravi", 20, "BCA")

print("Student name:", student[0])
print("Student age:", student[1])
print("Student course:", student[2])