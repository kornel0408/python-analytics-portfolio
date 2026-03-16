# ===========================================================
#                        FOR LOOP
# ===========================================================



# -----------------------------------------------------
# print numbers from 1 to 100
# -----------------------------------------------------
for i in range(101):
    print(i)
#------------------------------------------------------




# -----------------------------------------------------
# print even numbers between 1 to 100
# -----------------------------------------------------
print("Even numbers between 1 and 100")
for i in range(1, 100, 2):
    print(i)
#------------------------------------------------------



#-----------------------------------------------------
#             Sum of List Values
#-----------------------------------------------------

# list of numbers (example: sales, marks, prices)
numbers = [10, 20, 30, 40, 50]

# variable to store sum
total = 0

# loop through list
for num in numbers:
    total = total + num

# print result
print("List:", numbers)
print("Total sum:", total)



# -----------------------------------------
#     Print Multiplication Table
#------------------------------------------

for i in range (1,11):
    print(10*i)
#----------------------------------------




#----------------------------------------
# Count Occurrences in List
#---------------------------------------
numbers = [1, 2, 3, 2, 4, 2, 5]

count = 0
for i in numbers:
    if i == 2:
        count = count + 1

print("total occurance of 2 is,", count)
#---------------------------------------


#-------------------------------------------------------------
# Count Vowels in string
#------------------------------------------------------------

text = "python programming"

vowels = ['a', 'e', 'i', 'o', 'u']

vowels_count = 0
for i in text:
    if i in vowels:
        vowels_count += 1
print("total vowel count in the string :", vowels_count)

#-------------------------------------------------------------


#----------------------------------------------------------
#   Data Cleaning Task
#----------------------------------------------------------
# list with extra spaces
names = [" Ravi", "John ", "  Meena", "Amit "]

# new list to store cleaned names
clean_names = []

# loop through list
for name in names:
    
    # remove spaces using strip()
    cleaned = name.strip()
    
    # add cleaned name to new list
    clean_names.append(cleaned)

# print results
print("Original list:", names)
print("Cleaned list:", clean_names)
#-------------------------------------------------------