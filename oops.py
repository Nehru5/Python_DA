# account_number = 101
# name = "Rajesh"
# balance = 5000

# def deposit(amount):
#   global balance
#   balance = balance+amount
  
# def withdraw(amount):
#   global balance
#   balance = balance-amount
  
# def check_balance():
#   print(balance)
  
# deposit(10000)
# check_balance()
# withdraw(3500)
# check_balance()


# account1_number = 101
# account1_name = "Rajesh"
# account1_balance = 5000

# account2_number = 102
# account2_name = "Kiran"
# account2_balance = 6000

# account3_number = 103
# account3_name = "Santhosh"
# account3_balance = 10000


# # Display Account Details
# def display_account(acc_no,acc_name,acc_bal):
#   print(f"Account Number: {acc_no}")
#   print(f"Account Name: {acc_name}")
#   print(f"Account Balance: {acc_bal}")
#   print("-----------------------------")
  
  
# def deposit(acc_name,acc_bal,amount):
#   acc_bal = acc_bal+amount
#   print(f"{acc_name} Deposited Rs, {amount}")
#   print(f"New Balance: {acc_bal}")
#   return acc_bal

# def withdraw(acc_name,acc_bal,amount):
#   if amount<=acc_bal:
#     acc_bal = acc_bal-amount
#     print(f"{acc_name} withdrawn Rs, {amount}")
#     print(f"New Balance: {acc_bal}")
#     return acc_bal
#   else:
#     print("Insufficient balance")
#     return acc_bal
  
# def check_balance(acc_name,acc_bal):
#   print(f"{acc_name}: Balance: {acc_bal}")
  
  
  
# # Using Account 1

# display_account(account1_number,account1_name,account1_balance)
# account1_balance = deposit(account1_name,account1_balance,3000)
# check_balance(account1_name,account1_balance)
# account1_balance = withdraw(account1_name,account1_balance,1500)
# check_balance(account1_name,account1_balance)



# Creating a class

# class Student:
#   pass

# # objects
# student1 = Student()
# student2 = Student()

# # Adding data to the objects
# student1.name = "Kishore"
# student1.age = 20

# student2.name = "Pavan"
# student2.city = "Chennai"

# print(student1.name)
# print(student1.age)



class Student:
  
  def __init__(self,name,age):
    self.name = name
    self.age = age
    
  

  
    

student1 = Student("Kiran",20)
student2 = Student("Suresh",25)
print(student1.name,student1.age)
print(student2.name,student2.age)
    



 