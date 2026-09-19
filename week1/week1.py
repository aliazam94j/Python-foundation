# #conditional express:

# a = int(input("enter your nr "))
# b = int(input("enter your nr "))


# #print("positive" if num > 0 else "negative")
# #result = "even" if num % 2 == 0 else "odd"
# max_num = a if a > b else b
# print(max_num)
# print(f"A:{a} and B:{b}")


#indexing 

# card_nr = "1234-434343-52-323232"
# print(card_nr[0])
# print(card_nr[3:])
# print(card_nr[::3])



#while

# name = input("enter your name ")

# while name == "":
#     print("mr nameless, you need to enter your name ")
#     name = input("enter your name ")

# print(f"Hello {name}")


# food = input("Enter a food you like (q to quit) ")


# while not food == "q":
#     print(f"you like {food}")
#     food = input("Enter another food you like (q to quit) ")

# print("bye")

# num = int(input("enter a nr between 1-10"))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("enter a nr between 1-10"))

# print(f"your num is {num}")




#for loops


# for x in range(1,21):
#     if x == 12:
#         break
#     else:
#         print(x)

# for x in reversed(range(1,11)):
#     print(x)

#count down


# import time

# my_time = int(input("enter the time in secs:"))

# for x in range(my_time , 0 , -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("time is up")


#nested loop


# for y in range(3):
#     for x in range(1,10):
#         print(x,end =" ")
#     print()

# import time

# rows = int(input("Enter the nr of rows "))
# columns = int(input("Enter the nr of colums " ))
# sympol = input("enter a symbol to use " )
# my_time = int(input("enter your time "))

# for y in range(my_time,0,-1):
#     seconds = y % 60
#     minutes = int(y/60) % 60
#     hours = int(y / 3600)
#     time.sleep(1)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
# for x in range(rows):
#     for y in range(columns):
#         print(sympol,end = " ")
#     print()



# list, set,tuple
# list = [] ordered and changeable,dup ok
#set = {} unordered and immutable, but add/remove ok. no dup
#tuple = () ordered and unchangeable. dup ok. faster.

#list
# fruits = ["apple","pear","dragon","coco"]
# fruits[0] = "pineapple"
# fruits.append("berry")
# fruits.insert(6,"blueberry")
# fruits.sort()
# fruits.reverse()

# for fruit in fruits:
#     print(fruit)

# # print("berry" in fruits)


# #set
# # fruits = {"apple","orange","pineapple","coconut"}
# # fruits.add("berry")
# # print(fruits)


# #tuple


# fruits = ("apple","banana","dragonapple")
# print(fruits)


# shopping cart program
import time

foods = []
prices = []
total = 0
my_time = 10


while True:
    food = input("Enter a food to buy(to exit press q ) ")
    if food.lower() == "q":
        print("Goodbye")
        break
    else:
        price = float(input(f"enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)


print("----YOUR CART----")
for y in range(my_time,0,-1):
    time.sleep(1)
    print(y)
for food in foods:
    print("what you chose ")
    print(food, end = " ")

for price in prices:
    total +=price

print("")
print(f"your total is: ${total}")


