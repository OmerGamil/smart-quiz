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


def main():
    """
    Run all program functions.
    """
    welcome()
    ask_question()
    check_answer(answer)

main()