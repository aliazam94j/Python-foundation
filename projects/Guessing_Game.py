import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True


print("-----Guessing Game-----")
print(f"select a num between {lowest_num} and {highest_num}")


while is_running:

    guess = (input("enter your guess "))

    if guess.isdigit():
        guess = int(guess)
        guesses +=1

        if guess < lowest_num or guess > highest_num:
            print("that nr is out of range")
            print(f"please select a num between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("to low.. try again ")
        elif guess > answer:
            print("to high! try again ")
        else:
            print(f"Correct answer was {answer}")
            print(f"guesses it took{guesses}")
            is_running = False
        
    
    else:
        print("invalid guess")
        print(f"Please select a num between {lowest_num} and {highest_num}")