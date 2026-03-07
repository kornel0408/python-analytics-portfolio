# ==========================================================================
#                              if-else
# ==========================================================================


# 1.ATM Withdrawal Check
#--------------------------------------------------------------------
# total_amount = float(input("Enter total amount:"))
# with_draw_amount = int(input("Enter withdraw amount:"))

# if with_draw_amount <= total_amount:
#     print("Withdrawa is succesfull")
# else:
#     print("Insufficent Balance")
#---------------------------------------------------------------------


# 2.Website Age Restriction
#---------------------------------------------------------------------
# user_age = int(input("Enter your age:"))
# if user_age >= 18:
#     print("Access granted")
# else:
#     print("Access Denied Age Restricted Content")
#----------------------------------------------------------------------

# 3.Even or Odd Order ID
#----------------------------------------------------------------------
order_id = int(input("Enter your Order Id : "))
if order_id % 2 == 0:
    print("Priority processing")
else:
    print("Normal praocessing")
#----------------------------------------------------------------------