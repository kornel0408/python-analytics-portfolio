# *************************************************************
#               SETS
# *************************************************************

sets  = {1, 3, 4, 5, 6}

print(type(sets))

sets = {}            # NOte this is not an empty set, it is an empty dictionary 
print(type(sets)) 

empty_set = set()
print(type(empty_set))



# ------------------------------------------------------
# Remove Duplicate Numbers
# -----------------------------------------------------

numbers = [10, 20, 30, 20, 40, 10, 50]
print("*****************************")
print("Original list:")
print(numbers)
print("*****************************")
print("After removing duplicate:")
print(set(numbers))
print("*****************************")
#--------------------------------------------------------



#-----------------------------------------------------
# Add and removing elements in set
# ---------------------------------------------------
fruits = {"apple", "banana", "mango"}

print("*****************************")
print("Original set:")
print(fruits)
print("******************************")


print("modified set")
print(fruits.add("graphes"))
print(fruits)

print("after deleting :")
print(fruits.pop())
print(fruits)
#-----------------------------------------------------





#-----------------------------------------------------
# Finding common subject
# ---------------------------------------------------
student1 = {"Math", "Physics", "English"}
student2 = {"Physics", "Chemistry", "Math"}

print("Common subjects for both students:")
print(student1.intersection(student2))
#-----------------------------------------------------




#-----------------------------------------------------
# Finding all subjects
# ---------------------------------------------------
print("All subjects:")
print(student1.union(student2))
#----------------------------------------------------




#-----------------------------------------------------
# Finding different subjects
# ---------------------------------------------------
print("Different subjects:")
print(student1.difference(student2))
#------------------------------------------------------