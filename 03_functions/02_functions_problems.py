# *****************************************************
# PROBLEMS ON FUNCTIONS
#*****************************************************



# ------------------------------------------------
# 1.Student Grade Calculator
#-------------------------------------------------

def student_grade():
    
    # taking input
    marks = int(input("Enter marks: "))
    
    # checking grade
    if 90 <= marks <= 100:
        print("Grade A")

    elif 75 <= marks < 90:
        print("Grade B")

    elif 50 <= marks < 75:
        print("Grade C")
        
    elif marks < 50:
        print("FAIL")

    else:
        print("Please enter valid marks")

    return marks


# function call
student_grade()
# ------------------------------------------------




#--------------------------------------------------
# login(username, password)
# -------------------------------------------------
user_name = "kornel"
password = "password"

def login(user_name, password):
    if user_name_val == user_name and user_pass == password:
        return True
    else:
        return False

while True:

    user_name_val = input("Enter username: ")
    user_pass = input("Enter password:")

    if user_name_val == user_name and password == user_pass:
        print("login successfully")
        break
    else:
        print("Invalid Credentials")



login(user_name, password)

#----------------------------------------------------





# ------------------------------------------------------
# Find Maximum in List using Function
# without using max() function
# ------------------------------------------------------

# function definition
def find_max(numbers):

    # assume first element is maximum
    maximum = numbers[0]

    # loop through list
    for num in numbers:
        
        # check if current number is greater
        if num > maximum:
            maximum = num

    return maximum


# list of numbers
nums = [10, 45, 32, 67, 21, 89, 54]


# function call
result = find_max(nums)


# print result
print("List:", nums)
print("Maximum value:", result)
#------------------------------------------------------






#-------------------------------------------------------
# removing duplicates
#------------------------------------------------------
def remove_dup(list):

    empty_list = []

    for i in list:
        if i not in empty_list:
            empty_list.append(i)
    
    return empty_list

student_id = [1, 2, 3, 4, 8, 3, 4, 5, 6]

print("list before cleaning")
print(student_id)

result = remove_dup(student_id)
print("after removing duplicates")

print(result)
#---------------------------------------------------------


