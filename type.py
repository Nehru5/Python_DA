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
# amount = int(input("Enter amount: "))
# if amount>=1000:
#   discount = amount*0.10
#   final_amount = amount-discount
#   print(f"Discount Applied successfully: {discount}")
#   print(f"Total Amount after Discount: {final_amount}")
# else:
#   print("No Discount applied")
#   print(f"Total Amount: {amount}")

                
                
                # Looping statements
                
# for loop

# for i in range(0,5):
#   print(i)

# name = "Python"
# for i in name:
#   print(i)

# users = ["Nehru","Rakesh","Kiran","Suresh"]
# for i in users:
#   print(i)

# While loop

# password = ""
# while password!="Rakesh@123":
#   password = input("Enter your password: ")

# print("Login successful")


# # Break statement
# for i in range(1,11):
#   if i==5:
#     break
#   print(i)

  # continue statement
# for i in range(1,6):
#   if i == 3:
#     continue
#   print(i)

# names = ["David","Ravi","Kiran","Sanjay"]

# for i in names:
#   if i == "Kiran":
#     continue
#   print(i)


  # pass statement
  
# def dashboard():
#  pass
  
# def reels():
#   print("This is ur reels....")
  
# reels()
# for i in "Python":
#   pass
# print("Done")


                          # List
# numbers = [10,20,30,40]
# data = [10,"Raja",25.5,True]
# print(numbers)
# print(data)
# print(data[2])
# print(data[-1])
# print(len(data))

# Looping through list
# sales = [200,350,400,150]
# for s in sales:
#   print(s)

# Find total Sales
# sales = [200,350,400,150]
# total = 0
# for s in sales:
#   total = total+s
# print(total)

# List is a mutable
# numbers = [10,20,30]
# numbers[1] = 50
# print(numbers)

# Calculating Marks
# marks = [80,90,70,85]
# total = 0
# for m in marks:
#   total = total+m
# print(f"Total Marks: {total}")
# avg = total/len(marks)
# print(f"Average: {avg}")

                                  # List Methods
# append() - Adding item at end of a list
# numbers = [10,20,30]
# numbers.append(40)
# print(numbers)

# pop()
# numbers = [10,20,30]
# numbers.pop()
# print(numbers)

# insert() - TO add element at specific position
# numbers = [10,20,30]
# numbers.insert(1,50)
# print(numbers)

# remove()
# numbers = [10,20,30]
# numbers.remove(20)
# print(numbers)

# sort()
# numbers = [10,40,20,100,30]
# numbers.sort() #Ascending order
# numbers.sort(reverse=True) #Descending order
# print(numbers)

# count()
# numbers = [10,20,10,10,40,10,50]
# print(numbers.count(10))

# extend()
# numbers = [10,20,30]
# numbers.extend([40,50,60])
# print(numbers)
# numbers.clear()
# print(numbers)
# b = numbers.copy()
# print(b)

# sales_day1 = [200,300,400]
# sales_day2 = [150,250,350]
# sales_day1.extend(sales_day2)
# print(sales_day1)

# print(type(sales_day1))

                        # tuple
# numbers = (10,20,30,10)
# print(type(numbers))
# print(numbers)
# print(numbers[2])
# print(numbers[-1])
# print(numbers.count(10))
# fruits = ("Mango","Apple","Orange","Watermelon")
# print(fruits.index("Orange"))
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# # Packing and unpacking Tuple
# student = ("Ravi",22,"Chennai")
# print(student)

# Unpacking
# name,age,city = student
# print(name,age,city)
# print(type(name))

# name = "Kishore"
# print(name)

# username = (name,)
# print(type(username))



                    #Dictionary
# student = {
#   "name":"Ravi",
#   "age":25,
#   "skills":["HTML","CSS","JS"],
#   "address":{
#     "city":"Bengaluru",
#     "state":"Karnataka"
#   }
# }
# print(student)
# # Accessing Values using square brackets
# print(student["name"])
# print(student["address"]["city"])
# print(student["skills"][2])
# # print(student["country"])
# # Accessing values using get()
# print(student.get("name"))
# print(student.get("age"))
# print(student.get("country","No country found"))
  
student = {
  "name":"Ravi",
  "age":22,
  "skills":["HTML","JS","Angular"]
}
# Adding the item
# student["city"] = "Bengaluru"
# print(student)

# # Updating multiple items
# student.update({"name":"Yogesh","age":30})
# print(student)
# student["skills"][2] = "React js"
# print(student)

# Deleting
# del student["age"]
# print(student)

# clear()
# student.clear()
# print(student)

# Dictionary methods

# keys()
# print(student.keys())
# print(student.values())
# print(student.items())

# Looping through dictionary
# for i,j in student.items():
#   print(i,j)
  
# for i in student.keys():
#   print(i)

# for i in student.values():
#   print(i)

                                # Sets
# numbers = {10,20,30,10}
# print(type(numbers))
# print(numbers)

# Adding elements
# numbers.add(40)
# print(numbers)

# Removing elements
# numbers.remove(20)
# print(numbers)
# numbers.discard(200)
# print(numbers)


# set operations

# a = {10,20,30}
# b = {30,50,60}
# print(a.union(b))
# print(a.intersection(b))
# print(b.difference(a))

                                        # Functions
# def greet():
#   print("Hello, Welcome")
  
# greet()
    
# Parameter

# Without parameter

# def greet():
#   print("Welcome Divya")

# greet()

# def greet2():
#   print("Welcome Rajesh")

# greet2()

# def greet3():
#   print("Welcome Manoj....")
  
# greet3()


# With parameter

# def greet(username):
#   print(f"Welcome {username}")
  
# greet("Divya")
# greet("Ramesh")

# No of parameters = No of Arguments


# Function with Return type

# def add(a,b):
#   return a+b

# a = add(2,3)
# print(a)
# if a >3:
#   print("You r eligible")

# Salary bonus(Return example)

# def bonus(salary):
#   return salary+2000

# first_salary = bonus(25000)
# print(first_salary)

# Returning multiple values

# def student():
#   return "Ravi", 23, "Python"

# name,age,course = student()
# print(name)
# print(age)
# print(course)

# Return is better - Can store value, Can reuse value, can perform calculations

# def test():
#   print("Hello")
#   return "Welcome"
#   print("Good night")
  
# a = test()
# print(a)

# Important rule - Once return executes, function stops immediately....



# Default parameter in Function

# def login(user="Guest"):
#   print(f"Welcome, {user}")
  
# login()
# login("Ganesh")

# def order(item,quantity=1):
#   print(f"Item Name: {item}")
#   print(f"Quantity: {quantity} - {quantity*1500}")
  
# order("Laptop")



# Positional Argument

# def student(name,age):
#   print(f"Name: {name}")
#   print(f"Age: {age}")
  
# student("Santhosh",25)



# Keyword arguments

# def student(name,age):
#   print(f"Name: {name}")
#   print(f"Age: {age}")
  
# student(age = 25,name="Santhosh")


# Positional argument + Keyword Argument(Mixed)

# def student(name,age,course):
#   print(name,age,course)

# student("Rakesh",age = 25,course="Python")

# Important Rule - Positional arguments must come before Keyword arguments

# *args(Multiple arguments)
# def numbers(*args):
#   print(args)
  
# numbers(10,20,30,40)

# def add(a,b):
#   print(a+b)
  
# add(2,3)

# def add1(a,b,c):
#   print(a+b+c)

# add1(10,20,30)

# def total(*numbers):
#   sum = 0
#   for i in numbers:
#     sum = sum+i
#   print(sum)
  
# total(1,2,3)
# total(10,20,30,40,50)


# def cart(*items):
#   print(f"Items in my Cart: {items}")
  
# cart("Laptop","Mouse","Keyboard")


# **kwargs()

# def student(**data):
#   print(data)
#   # Accessing values
#   print(data["name"])
#   print(data["age"])
#   print(data["course"])
  
#   for i,j in data.items():
#     print(i,j)

# student(name="Ravi",age=23,course="Java")




# Lambda function

# def add(a,b):
#   return a+b

# a = add(7,8)
# print(a)

# add = lambda a,b : a+b
# a = add(7,8)
# print(a)


  

  

  
  
  
  

  

          


