# ****************************************************************************
#                        elif statement                                       
# ****************************************************************************


# 1.Internet Data Usage Plan
# -------------------------------------------------------------------------
data_usage = int(input("Enter data usage(GB) : "))

if data_usage <= 5:
    print("Basic Plan")

elif data_usage <=15:
    print("Standartd Plan")

else:
    print("Premium Plan")
# --------------------------------------------------------------------------


# 2.Salary Tax Category
#--------------------------------------------------------------------------
Monthly_salary = int(input("Enter your monthly salary(INR): "))

if Monthly_salary < 30000:
    print("No Tax")

elif Monthly_salary < 70000:
    print("10% Tax")

elif Monthly_salary <= 150000 :
    print("20% Tax")

else:
    print("50% Tax")
#---------------------------------------------------------------------------




# 3.Exam Grade System
#---------------------------------------------------------------------------

marks = int(input("Enter your marks:"))

if marks >= 90 and marks <=100:
    print("Grade A")

elif marks>= 75 and marks < 90:
    print("Grade B")

elif marks >= 50 and marks < 75:
    print("Grade C")

elif marks < 50:
    print("Fail")

else:
    print("Please enter valid marks")
#----------------------------------------------------------------------------

# I hope you got a clarity on elif statement THANK YOU