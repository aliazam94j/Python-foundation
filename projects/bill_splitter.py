price = float(input("what is the price for the bill?: "))
split = int(input("how many are splitting the bill?: "))

if split <= 0:
    print("NOT VALID CHOOSE ATLEAST 1")
    exit(1)

result = price / split
print(f"this is how much each person needs to pay = {round(result, 2)} kr")
