# ***************************************************
#               DICTIONARY
# ***************************************************



#-------------------------------------------------
# Create a dictionary to store student details:
#-------------------------------------------------

dict = {
    "name"   : "kornel",
    "age"    : 21,
    "course" : "BCA"
}

# --------------------------------------------------




# -------------------------------------------------
# print student details
#-------------------------------------------------
print("******************")
print("Student details :")
print("******************")
print(dict)
#-------------------------------------------------





# -------------------------------------------------
# Updating, adding
# -------------------------------------------------
dict["age"] = 22
dict["marks"] = 96

print("updating student details")
print(dict)
# ------------------------------------------------




# ------------------------------------------------
# product details dictionary
#-------------------------------------------------
product = {
    "name"  : "Laptop",
    "price" :  50000,
    "stock" : 10
}

print("product details")
print("***************")
print(product)


# Updating product details
print("updating product details")
print("***************")

product["price"] = 80000
product["brand"] = "Lenovo"
print("all keys:")
print(product.keys())
print("all values")
print(product.values())
#-------------------------------------------------





# ---------------------------------------------------
# Marks dictionary analysis
#----------------------------------------------------
marks = {
    "maths" : 97,
    "Science" : 85,
    "English" : 88
}

print("Subjects:")
print(marks.keys())
print("highest marks")
highest = max(marks.values())
print(highest)

print("total_marks=", sum(marks.values()))

#----------------------------------------------------