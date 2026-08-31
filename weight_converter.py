weight = float(input("Enter your weight: "))
unit = input("Is it in kg or lb? (K or L): ").lower()

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"your weight is {round(weight, 1)} {unit}")
elif unit == "l":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not valid")
