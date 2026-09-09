import os
os.system('cls')


# first_name = "Ali"
# last_name = "Azam"
# Food = "Burger"

# print(f"your first name is {first_name} and your last name is {last_name}")
# print(f"{first_name} {last_name}")
# print(f"you like {Food}")

# quanity = 3
# price = 25 
# total = quanity * price

# print(f"you choose {quanity} burgers")
# print(f"the price is {price}kr for each burger")
# print(f"the total is = {total}kr")

# is_student = False

# if is_student: 
#     print("you are a student! and u get a discount")
# else:
#     print("your not a student, PAY THE FULL PRICE")



# name = "ali"
# age = 32
# height = 182.1
# is_student = True


# height =str(height)

# print(type(height))



# item = input("what item would you like to buy? ")
# price =float(input("what is the price for the item "))
# quantity = int(input("how many do u want? "))

# total = quantity * price


# print(f"you have bought {quantity} x {item}/s")
# print(f"your total is {total}kr")


# x = 5.14
# y = -4
# z = 5

# # result = round(x)
# # result = abs(y)
# # result = pow(10,3)
# #result =max(x,y,z)
# result = min(x,y,z)
# print(result)


# import math

# # print(math.pi)
# # print(math.e)
# x = 9

# # result = math.sqrt(x)
# # result = math.ceil(x)
# result = math.floor(x)

# print(result)



# age = int(input("enter your age :"))

# if age >=18:
#     print("you can join")
# elif age < 0:
#     print(".......")
# else:
#     print("your to young ")



# Answer = input("Would you like the food? (Y/N) ")

# if Answer == "Y":
#     print("have da food")
# else:
#     print("stay hungry")

# for_sale=input("is the item for sale? ") == "true"

# if for_sale:
#     print("the item is for sale!")
# else:
#     print("the item is not for sale")






# Calculator:


# operator = input("Enter your operator (+ - * /): ")
# tal1 = float(input("Enter your 1st number: "))
# tal2 = float(input("Enter your 2nd number: "))


# if  operator == "+":
#     result = tal1 +tal2
#     print(round(result,3))
# elif operator == "-":
#     result = tal1 + tal2
#     print(round(result,3))
# elif operator == "*":
#     result = tal1 * tal2
#     print(round(result,3))
# elif operator == "/":
#     result = tal1 / tal2
#     print(round(result,3))
# else:
#     print(f"{operator} is not a valid operator")



#weight converter




# weight = float(input("Enter your weight: "))
# unit = input("Is it in kg or lb? (K or L): ").lower()


# if unit == "k":
#     weight = weight * 2.205
#     unit = "Lbs."
#     print(f"your weight is {round(weight,1)} {unit} ")

# elif unit == "l":
#     weight = weight / 2.205
#     unit = "Kgs."
#     print(f"your weight is {round(weight,1)} {unit} ")

# else:
#     print(f"{unit} is not valid")


# # resturant bill.

# # #user is asked for the price.
# price =float(input("what is the price of bill?  "))

# #How many people will split the bill

# while True:
#     split =int(input("how many people are splitting the bill?  "))
#     if split <= 0:
#         print("you cant split between 0 people must have atleast 1")
#         continue
#     break

# result = price/split


#     # here is the result, i used the round function to round the ammount with 2 decimal.
# print(f"this is how much each person needs to pay = {round(result,2)} kr")




# price = float(input("what is the price for the bill?: ")) 
# split = int(input("how many are splitting the bill?: "))

# if split <= 0:
#     print("NOT VALID CHOOSE ATLEAST 1")
#     exit(1)


# result = price / split
# print(f"this is how much each person needs to pay = {round(result,2)} kr")



# logical operators:
# temp = 25

# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("event canceled")
# else:
#     print("Event is still on")




