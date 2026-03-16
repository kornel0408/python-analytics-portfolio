# ===========================================================
#                        WHILE LOOP
# ===========================================================


# -----------------------------------------------------
# print numbers from 1 to 100
# -----------------------------------------------------

count = 1
while count <= 100:
    print(count)
    count += 1

print("done")
# -----------------------------------------------------






# -----------------------------------------------------
# print numbers from 100 to 1
# -----------------------------------------------------

i = 100
while i >= 1:
    print(i)
    i -= 1
print("done")

#------------------------------------------------------





# ----------------------------------------------------
# print the table of 10
# ----------------------------------------------------

print("table of 10 :")

i = 1
while i <= 10:
    print(i*10)
    i += 1
print("end")

# ----------------------------------------------------




# --------------------------------------------------
# print the following list items using while loop
# --------------------------------------------------
list = [10, 15, 20, 25, 26, 27]

indx = 0
while indx < len(list):
    print(list[indx])
    indx += 1
print("Done")
# --------------------------------------------------




# ---------------------------------------------
# Number Guessing Game using while loop
# This program keeps asking the user to guess
# the correct number until the guess is correct
# ---------------------------------------------
# correct number
correct_number = 7

# user guess (initial value)
guess = 0

# loop runs until guess becomes correct
while guess != correct_number:
    
    # taking input from user
    guess = int(input("Enter your guess: "))
    
    # checking guess
    if guess == correct_number:
        print("Correct Guess!")
    else:
        print("Wrong guess, try again")

print("Game Over")
#----------------------------------------------

