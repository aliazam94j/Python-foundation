# week 2

#Function
#Reminder like C you put something in the parameter, u need to put something in the parameter when u call it.

# def happy_day(name,age):
#     print(f"today is a happy day mr {name} and you are {age}")
#     print("yes it is ")
#     print("today is a happy day")
#     print()


# happy_day("Ali",32)



# def display_invoice(username,amount,due_date):
#     print(f"Hello {username}")
#     print(f"your bill of ${amount:.2f} is due: {due_date}")


# display_invoice("post",25.50, "")



#return


# def add(x,y):
#     z = x + y
#     return z

# def subtract(x,y):
#     z = x - y
#     return z

# def multi(x,y):
#     z = x * y
#     return z

# def divide(x,y):
#     z = x / y
#     return z



# print(add(5,10))
# print(subtract(20,10))
# print(multi(5,3))
# print(divide(10,2))

# def create_name(first,last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# full_name = create_name("ali" , "azam" )

# print(full_name)



# default arguments

# import time

# def count(end, start = 0):
#     for x in range(start , end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE")

# count(30,15)


#keyword arguments

# # def hello(greeting,title,first,last):
# #     print(f"{greeting} {title} {first} {last}")

# # hello("hello",title ="mr",first ="Ali",last ="Azam" )


# # for x in range(1,11):
# #     print(x, end= " ")

# def get_phone(country,area,first,last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=1, area=123, first=693, last=8909)
# print(phone_num)



import pandas as pd

ingredients = {"Items":["Pasta","Tomatoes","Basil","Cheese","Meat"],
               "Grams":[500,300,150,250,200]}
               

result = pd.DataFrame(ingredients)
print(result)
