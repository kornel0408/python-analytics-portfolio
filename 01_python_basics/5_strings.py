# ==================================================================================
#                                      STRINGS  
# ==================================================================================


#--------------------------------------------------                         
# Creating string
#--------------------------------------------------

name = "boyalapalli Kornel"
print(name)
name_length = len(name)
print("Lenght of the string:", name_length)

#-------------------------------------------------------------
# Accessing individual elements using index numbers(indexing)
#-------------------------------------------------------------

print(name[0])
print(name[1])  # positive indexing
print(name[2])

print(name[-3])
print(name[-1]) # Negative indexing
print(name[-18])


#---------------------------------------------------------
#       Slicing                              
#---------------------------------------------------------

print(name[0:18])
print(name[:18])
print(name[0:])      # Positive slicing
print(name[0:18:3])
print(name[::3])
print(name[0:len(name)])

print(name[-18:-1])
print(name[:-1])     # Negative slicing
print(name[-4:-2])


#-------------------------------------------------
# Basic string methods
#-------------------------------------------------

new_name = " boyalapalli kornel "

print("before cleaning :")
before_cleaning = print(new_name)

clean_new_name = new_name.strip()
print("After cleaning:")
print(clean_new_name)


print(clean_new_name.capitalize()) # capitalizing 

print(clean_new_name.find("a")) # finding first occurence

print(clean_new_name.upper()) # prints in uppercase

print(clean_new_name.lower()) # prints in lowercase

print(clean_new_name.replace('a', 'o')) # replace old string wih new string

print(clean_new_name.count('o')) # counts string occurence
