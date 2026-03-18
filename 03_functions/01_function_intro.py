# ***********************************************************
#                   FUNCTIONS
# **********************************************************




# ***********************************************************
#                   FUNCTIONS IN PYTHON
# This file demonstrates basic function concepts:
# function definition, parameters, return values,
# default arguments, and function calling
# ***********************************************************


# -----------------------------------------------------------
# Function without parameters
# This function prints Hello world
# -----------------------------------------------------------
def hello():
    print("Hello world")
    return

# function call
hello()


# -----------------------------------------------------------
# Function with parameters
# This function adds two numbers and returns result
# -----------------------------------------------------------
def add(a, b):
    sum = a + b
    print(sum)
    return sum

# function call with arguments
add(10, 7)


# -----------------------------------------------------------
# Function to find square of a number
# Takes one parameter
# -----------------------------------------------------------
def square(a):
    sqr = a * a
    print(sqr)

# function call
square(8)


# -----------------------------------------------------------
# Function with default parameters
# If no values given, default values will be used
# -----------------------------------------------------------
def product(a=2, b=3):
    prod = a * b
    print(prod)
    return prod

# function call without arguments
product()


# -----------------------------------------------------------
# Function with one default parameter
# Here b has default value = 20
# -----------------------------------------------------------
def div(a, b=20):
    division = b / a
    print(division)
    return division

# function call with one argument
div(10)