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