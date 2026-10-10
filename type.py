# Typecasting - converting one data into another type of data
# Implicit Typecasting
# a = 10
# b = 2.5
# print(type(a))
# print(type(b))
# c = a+b
# print(type(c))
# print(c)

# Explicit Typecasting
# x = int(input("Enter Number 1: "))
# y = int(input("Enter Number 2: "))
# print(x+y)

# Converting int to string datatype
# z = 10
# m = str(z)
# print(type(m))

              # Inputs
                
# a = input("Enter ur name: ")
# b = int(input("Enter ur age: "))
# c = eval(input("Enter some expression"))
# print(a)
# print(b)
# print(c)

              # Conditional statements
              
# if statement
# age = 15
# if age>=18:
#   print("U R eligible to vote")
  
  
# if-else
# age = 16
# if age>=18:
#   print("u r eligible")
# else:
#   print("Not eligible")

# if elif else

# marks = 90
# if marks>=90:
#   print("A Grade")
# elif marks>=75:
#   print("B Grade")
# else:
#   print("Fail")

# Finding Positive, negative and zero
# num = -5

# if num>0:
#   print("Positive")
# elif num<0:
#   print("Negative")
# else:
#   print("Zero")

# Nested Conditions
# age = 25
# citizen = True

# if age>=18:
#   if citizen==True:
#     print("Eligible to vote")
#   else:
#     print("Citizenship Required")
# else:
#   print("Age requirement not met")

# ATM withdrawl Logic(Nested Conditions)
# balance = 5000
# amount = int(input("Enter Withdrawl Amount: "))

# if amount>0:
#   if amount<=balance:
#     print("Withdrawl successfull....")
#   else:
#     print("Insufficient balance")
# else:
#   print("Invalid amount")
  
  
# Ternary Operator
# syntax - value_if_true if condition else value_if_false

# age = 22
# result = "Yes he is eligible" if age>=18 else "He is not eligible"
# print(result) 

# Practical:
# Discount Calculation
amount = int(input("Enter amount: "))
if amount>=1000:
  discount = amount*0.10
  final_amount = amount-discount
  print(f"Discount Applied successfully: {discount}")
  print(f"Total Amount after Discount: {final_amount}")
else:
  print("No Discount applied")
  print(f"Total Amount: {amount}")

  

          


