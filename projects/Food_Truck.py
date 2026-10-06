menu = {"hamburger":3.00,
        "nachos": 4.50,
        "fries":2.50,
        "kebab":6.00,
        "pizza":8.00}


order =[]
total = 0


print("-------- menu ---------".upper())
for key,value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("------------------------")

while True:
    food = input("select an item(q to quit) ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        order.append(food)
print(order)

print("------YOUR ORDER--------")
for food in order:
    total+=menu.get(food)
    print(food,end = " ")
print()
print(f"total is ${total:.2f}")