QUIZ_QUESTIONS = [
    {
        "question": "What is the capital of England?",
        "choices": ["Birmingham", "Paris", "London", "Tokoyo"],
        "correct": 2
    },
    {
        "question": "What is the capital of France?",
        "choices": ["Birmingham", "Paris", "London", "Tokoyo"],
        "correct": 1
    },
]

username = ""
question_number = 0
score = 0

def welcome():
    """
    Welcomes user and asks for name.
    """
    print("Welcome! to my very short quiz\n")

    global username
    while username == "":
        username = input("Please enter your name: ").strip()
        if username == "":
            print("No, you must enter something!")

    print("\nHello, " + username)
    print("Get ready for the QUIZ...")



def ask_question():
    """
    Get the questions according to their order.
    """
    quest = QUIZ_QUESTIONS[question_number]
    print("\nQuestion number " + str(question_number + 1) + ": " + quest["question"])

    for i, choice in enumerate(quest["choices"], 1):
        print(f"{i}. {choice}")  # Print the choices with numbering

    global answer
    answer = int(input("\n: ").strip()) - 1 # Substract the answer to get the right index


def check_answer(user_answer):
    """
    Check the user answer if it is correct.
    """
    quest = QUIZ_QUESTIONS[question_number]

    if user_answer == quest["correct"]:
        global score
        score += 1


def main():
    """
    Run all program functions.
    """
    welcome()

    for i in range(len(QUIZ_QUESTIONS)):
        ask_question()
        check_answer(answer)
        global question_number
        question_number += 1
    
    print("\nYou got " + str(score) + " out of " + str(len(QUIZ_QUESTIONS)))

main()