operator = input("Enter your operator (+ - * /): ")
tal1 = float(input("Enter your 1st number: "))
tal2 = float(input("Enter your 2nd number: "))

if operator == "+":
    result = tal1 + tal2
    print(round(result, 3))
elif operator == "-":
    result = tal1 - tal2
    print(round(result, 3))
elif operator == "*":
    result = tal1 * tal2
    print(round(result, 3))
elif operator == "/":
    result = tal1 / tal2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")
