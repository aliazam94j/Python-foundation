import random

questions = ("what energy drink is the best " ,
            "what martial arts is from korea? ",
            "what is the capital of sweden? ",
            "what is the capital of pakistan? ")

options = (("a.Nocco ", "b. Celsius ", "c.Redbull", "d. CleanDrink"),
           ("a. Judo", "b. Capoeria", "c. Taekwondo", "d. Fencing"),
           ("a.goteburg ", "b.sigtuna ", "c.Stockholm", "d.malmo "),
           ("a.lahore ", "b.Islambad", "c.Karachi ", "d.Gujrat"))

answers = ("d","c","c","b")

guesses = []
asked_answers = []

score = 0

qa = list(zip(questions, options, answers))
random.shuffle(qa)

for question, option, answer in qa:
    print("------------------------")
    print(question)
    for opt in option:
        print(opt)

    guess = input("Enter(a,b,c,d): ").lower()
    guesses.append(guess)
    asked_answers.append(answer)
    if guess == answer:
        score += 1
        print("correct")
    else:
        print("incorrect")
        print(f"{answer} is the correct answer")

print("------------------------")
print("        Results         ")
print("------------------------")


print("answers: ", end = "")
for answer in asked_answers:
    print(answer, end = " ")

print()

print("guesses: ", end = "")
for guess in guesses:
    print(guess, end = " ")

print()

score = int(score / len(questions) * 100)
print(f"your score is: {score}%")
