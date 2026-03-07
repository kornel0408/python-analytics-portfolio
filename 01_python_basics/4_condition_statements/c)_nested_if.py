# ****************************************************************************
#                        nested if statement                                       
# ****************************************************************************



#---------------------------------------------------------------------------
# 1.Loan Eligibility Check
#-----------------------------------------------------------------------------
age = int(input("Enter your age: "))

if age >= 21:
    monthly_salary = int(input("Enter your monthly salary :"))

    if monthly_salary >= 25000:
        print("Loan is approved")

    else:
        print("loan is rejected")

else:
    print("Loan is rejected")
#-----------------------------------------------------------------------------



#---------------------------------------------------------------------------
# 2.Company Job Application Screening
#---------------------------------------------------------------------------

degree = input("Do you have Degree Enter 'Yes' or 'No' :")

if degree == "yes":
    experience = int(input("Enter your years of experience:"))

    if experience >= 2:
        print("Eligible for Interview")
    
    else:
        print("Need more experience")
else:
    print("Application Renected")
# #----------------------------------------------------------------------------

    



#-----------------------------------------------------------------------------
# 3. Online Shopping Free Delivery
#-----------------------------------------------------------------------------
order_ammount = int(input("Please enter your order amount:"))

if order_ammount >= 1000:

    member = input("Do you have membership enter 'Yes' or 'No' :")

    if member == "yes":
        print("Free Express Delivery")
    else:
        print("Standard Delivery")

else:
    print("Delivery Charges Applied")
#------------------------------------------------------------------------------

# I hope you got a clarity on nested if and if else statements THANK YOU