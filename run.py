QUIZ_QUESTIONS = [
    {
        "question": "Where did the Titanic sink?",
        "choices": ["The Atlantic Ocean", "The Pacific Ocean", "The Indian Ocean", "The Arctic Ocean"],
        "correct": 0
    },
    {
        "question": "Which number would be next in this pattern: 8, 10, 13, 17, 22, ?",
        "choices": ["24", "28", "32", "36"],
        "correct": 1
    },
    {
        "question": "Complementary colors are colors that are:",
        "choices": ["Made by mixing two primary colors", 
                    "Mixed with black or white",
                    "Side by side on the color wheel",
                    "Opposite each other on the color wheel"],
        "correct": 3
    },
    {
        "question": "How many teeth does the average human have?",
        "choices": ["24", "30", "32", "40"],
        "correct": 2
    },
    {
        "question": "Which city hosted the most recent Olympic Games?",
        "choices": ["Rio de Janeiro, Brasil", "Pyeongchang, South Korea", "Tokyo, Japan", "Sochi, Russia"],
        "correct": 1
    },
    {
        "question": "Which is the last phase in cell reproduction?",
        "choices": ["Anaphase", "Prophase", "Cytokinesis", "Metaphase"],
        "correct": 2
    },
    {
        "question": "Which number would be next in this pattern: 8, 10, 13, 17, 22, ?",
        "choices": ["24", "28", "32", "36"],
        "correct": 1
    },
    {
        "question": "Which number would be next in this pattern: 8, 10, 13, 17, 22, ?",
        "choices": ["24", "28", "32", "36"],
        "correct": 1
    },
    {
        "question": "Which number would be next in this pattern: 8, 10, 13, 17, 22, ?",
        "choices": ["24", "28", "32", "36"],
        "correct": 1
    },
    {
        "question": "Which number would be next in this pattern: 8, 10, 13, 17, 22, ?",
        "choices": ["24", "28", "32", "36"],
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