# ---------------------------------------------
# Python List Practice Program
# This program demonstrates list creation,
# modifying list, and using list methods
# Real-world example: Shopping Cart System
# ---------------------------------------------

# Creating a list (shopping cart)
cart = ["Laptop", "Mouse", "Keyboard"]

print("Initial cart:", cart)


# ---------------------------------------------
# Adding item to list using append()
# ---------------------------------------------
cart.append("Headphones")
print("After adding item:", cart)


# ---------------------------------------------
# Removing item from list using remove()
# ---------------------------------------------
cart.remove("Mouse")
print("After removing item:", cart)


# ---------------------------------------------
# Adding item at specific position using insert()
# ---------------------------------------------
cart.insert(1, "USB Cable")
print("After inserting item:", cart)


# ---------------------------------------------
# Modifying list using indexing
# Changing Keyboard to Mechanical Keyboard
# ---------------------------------------------
cart[2] = "Mechanical Keyboard"
print("After modifying item:", cart)


# ---------------------------------------------
# Finding number of items using len()
# ---------------------------------------------
print("Total items in cart:", len(cart))


# ---------------------------------------------
# Checking if item exists in list
# ---------------------------------------------
if "Laptop" in cart:
    print("Laptop is in cart")


# ---------------------------------------------
# Removing last item using pop()
# ---------------------------------------------
cart.pop()
print("After pop:", cart)


# ---------------------------------------------
# Sorting list
# ---------------------------------------------
cart.sort()
print("Sorted cart:", cart)


# ---------------------------------------------
# Reversing list
# ---------------------------------------------
cart.reverse()
print("Reversed cart:", cart)


# ---------------------------------------------
# Final cart
# ---------------------------------------------
print("Final cart:", cart)