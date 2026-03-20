# ****************************************************************
#                 FILE MODES + DELETE FILE USING OS
# This program demonstrates:
# r, r+, w, w+, a, a+ modes
# deleting file using os module
# ****************************************************************


import os   # needed for delete file


path = r"C:\Users\boyal\OneDrive\Python\Files_input_output\demo.txt"


# -----------------------------------------------------------------
# r mode → read only
# -----------------------------------------------------------------
file = open(path, "r")

data = file.read()
print("Read mode:")
print(data)

file.close()



# -----------------------------------------------------------------
# r+ mode → read + write
# -----------------------------------------------------------------
file = open(path, "r+")

data = file.read()
print("r+ read:")
print(data)

file.write("\nAdded using r+")
file.close()



# -----------------------------------------------------------------
# w mode → overwrite file
# -----------------------------------------------------------------
file = open(path, "w")

file.write("Written using w mode\n")

file.close()



# -----------------------------------------------------------------
# w+ mode → write + read
# -----------------------------------------------------------------
file = open(path, "w+")

file.write("Written using w+\n")

file.seek(0)

print("w+ read:")
print(file.read())

file.close()



# -----------------------------------------------------------------
# a mode → append
# -----------------------------------------------------------------
file = open(path, "a")

file.write("Added using a\n")

file.close()



# -----------------------------------------------------------------
# a+ mode → append + read
# -----------------------------------------------------------------
file = open(path, "a+")

file.write("Added using a+\n")

file.seek(0)

print("a+ read:")
print(file.read())

file.close()



# ****************************************************************
# DELETE FILE USING OS MODULE
# ****************************************************************


# check if file exists
if os.path.exists(path):

    os.remove(path)
    print("File deleted successfully")

else:
    print("File not found")