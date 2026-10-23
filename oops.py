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

                                                                      # OOPS

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



# class Student:
  
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
    
  

  
    

# student1 = Student("Kiran",20)
# student2 = Student("Suresh",25)
# print(student1.name,student1.age)
# print(student2.name,student2.age)


                                          # Instance Attribute and Class Attribute
                                          
class Student:
  
  college = "Dr. AIT" #class attribute
  
  def __init__(self,name,age):
    self.name = name #instance attribute
    self.age = age   #instance attribute
    
    
    
# student1 = Student("Kishore",32)
# # student1.city = "Bengaluru" #Instance attribute
# student2 = Student("Prasanth",12)
# print(student1.name)
# print(student1.age)
# print(student2.name)
# print(student2.age)
# print("--------------")
# print(student1.college)
# print(student2.college)
# print(Student.college)
# Student.country = "India" #Class attribute
# print(student1.country)
# print(Student.country)


# Modifying an Instance Attribute
# print(student1.name)
# student1.name = "Rajesh"
# print(student1.name)


# Modifying a class attribute

# print(Student.college)
# # Student.college = "Impact"
# # print(Student.college)


# # Modifying class attribute using objects will create a new instance attribute inside the object

# student1.college = "Lawrence college"
# print(Student.college)
# print(student1.college)


# student1 = Student("Nagraj",22)
# student2 = Student("Pavan",28)
# # Deleting an Instance attribute
# # del student1.age
# # print(student1.age)

# # Deleting Class Attribute
# del Student.college
# print(Student.college)


                                              # Instance Method


# class Student:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
    
#   # Instance Method
#   def display(self):
#     print(self.name)
#     print(self.age)
    
  
# student1 = Student("Raja",23)
# student1.display()


# Instance method can also modify object data
# class Student:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
    
#   def increase_age(self):
#     self.age  = self.age+1
    
  
# student1 = Student("Kishore",30)
# print(student1.age)
# student1.increase_age()
# print(student1.age)
# student1.increase_age()
# print(student1.age)

                                  # Class Method
                                  
# class Student:
#   college = "AIT College"
  
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
    
#   @classmethod
#   def change_college(cls,new_college):
#     cls.college = new_college
    

# student1 = Student("Ravi",25)
# print(Student.college)
# Student.change_college("ABC College")
# print(Student.college)
    
    
    
                                              #Static Method
# class Student:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
    
#   @staticmethod
#   def is_valid_age(age):
#     return age>=18
    
    
    
# name = "Mahesh"
# age = 20

# if Student.is_valid_age(age):
#   student1 = Student(name,age)
#   print("Student created")
# else:
#   print("Invalid age")
  
# print(student1.age)


                                        # Bank Management
                                        
class BankManagement:
  def __init__(self,acccountHolder,account_no,balance):
    self.accountHolder = acccountHolder
    self.account_no = account_no
    self.balance = balance
    
    
  def display_data(self):
    print(f"Name: {self.accountHolder}\nAccount Number: {self.account_no}\nBalance: {self.balance}")
    
  def check_balance(self):
    print(f"Your Current balance: {self.balance}")
    
  def deposit(self,amount):
    if amount<=0:
      print("Invalid Amount")
    else:
      self.balance = self.balance+amount
      print(f"{amount} Deposited successfully...New Balance: {self.balance}")
      
  def withdraw(self,amount):
    if amount>self.balance :
      print("Insufficient Funds..")
    elif amount<=0:
      print("Invalid Amount")
    else:
      self.balance = self.balance-amount
      print(f"{amount} Withdrawl successfully...Current Balance: {self.balance}")
      
      
account1 = BankManagement("Kishore",101,5000)
account2 = BankManagement("Shreya",102,2000)
account1.display_data()
account2.display_data()

account1.deposit(1000)
account1.withdraw(1500)
    


    
    
    









 