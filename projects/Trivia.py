# list of questions


import random

questions = {
    "What country is Taekwondo from?:" "Korea",
    "What drink is something the body needs?:" "water"
    "What enerydrink is the best?:" "CleanDrink"
    }



def trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0


    selected_questions = random.sample(questions_list, total_questions)
    
    for i, question in enumerate(selected_questions):
        print(f"{i + 1}.{question}")

    trivia_game()