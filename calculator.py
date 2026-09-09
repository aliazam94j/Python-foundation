# operator = input("Enter your operator (+ - * /): ")
# tal1 = float(input("Enter your 1st number: "))
# tal2 = float(input("Enter your 2nd number: "))

# if operator == "+":
#     result = tal1 + tal2
#     print(round(result, 3))
# elif operator == "-":
#     result = tal1 - tal2
#     print(round(result, 3))
# elif operator == "*":
#     result = tal1 * tal2
#     print(round(result, 3))
# elif operator == "/":
#     result = tal1 / tal2
#     print(round(result, 3))
# else:
#     print(f"{operator} is not a valid operator")

#function
def plus(x,y):
    return x + y

def minus(x,y):
    return x - y

def multi(x,y):
    return x * y

def divide(x,y):
    return x / y


#input from the user
operator = input("what operator are u looking for? (+ - * /) ")
x = float(input("please enter the first nr "))
y = float(input("please enter the second nr "))


# calling the function with an if statement
if operator == "+":
    result = plus(x,y)
elif operator == "-":
    result = minus(x,y)
elif operator == "*":
    result = multi(x,y)
elif operator == "/":
    result = divide(x,y)
else:
    result =(f"not valid operator {operator}")

#result
print(result)

