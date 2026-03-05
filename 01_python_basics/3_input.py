# ************************************************************
#                  INPUT FUNCTION                             
# ************************************************************

# We use input funtion to take input from the user

name = input("Enter your name:") 

email = str(input("Enter your email:"))

age = int(input("Enter your age:")) 
# NOTE : input() function by default takes input as string if we want to enter numerical data we have to type conversion

percentage = float(input("Enter your percentage:")) 

print("Name :", name)
print("email :", email)
print("Age :", age)
print("Percentage:", percentage)

# lets print type of data 
print("Entered data type:")
print(type(name))
print(type(email))
print(type(age))
print(type(percentage))