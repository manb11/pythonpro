import random

def trivia_game():
    questions_and_choices_and_explanations = {
        "What color is the sky on a clear day?": {
            "choices": ["1- Red", "2- Green", "3- Blue", "4- Yellow"],
            "correct_choice": "3",
            "explanation": "The sky is blue on a clear day."
        },
        "How many legs does a cat have?": {
            "choices": ["1- Two", "2- Four", "3- Six", "4- Eight"],
            "correct_choice": "2",
            "explanation": "A cat has four legs."
        },
        "What is the opposite of 'hot'?": {
            "choices": ["1- Cold", "2- Warm", "3- Cool", "4- Spicy"],
            "correct_choice": "1",
            "explanation": "'Cold' is the opposite of 'hot'."
        },
        "Which month comes after April?": {
            "choices": ["1- March", "2- May", "3- June", "4- July"],
            "correct_choice": "2",
            "explanation": "May comes after April in the calendar."
        },
        "What is the capital city of France?": {
            "choices": ["1- London", "2- Berlin", "3- Paris", "4- Rome"],
            "correct_choice": "3",
            "explanation": "Paris is the capital city of France."
        },
        "How many fingers does a human have on one hand?": {
            "choices": ["1- Three", "2- Five", "3- Eight", "4- Ten"],
            "correct_choice": "2",
            "explanation": "A human has five fingers on one hand."
        },
        "Which is the largest planet in our solar system?": {
            "choices": ["1- Earth", "2- Jupiter", "3- Mars", "4- Venus"],
            "correct_choice": "2",
            "explanation": "Jupiter is the largest planet in our solar system."
        },
        "What is the color of an apple?": {
            "choices": ["1- Blue", "2- Green", "3- Red", "4- Yellow"],
            "correct_choice": "3",
            "explanation": "Apples are typically red in color."
        }
    }

    question = random.choice(list(questions_and_choices_and_explanations.keys()))

    print(f"\nQuestion: {question}")
    for choice in questions_and_choices_and_explanations[question]["choices"]:
        print(choice)

    user_answer = input("Your Answer (Enter the letter of your choice): ")

    correct_choice = questions_and_choices_and_explanations[question]["correct_choice"]
    explanation = questions_and_choices_and_explanations[question]["explanation"]
    
    if user_answer.upper() == correct_choice:
        print(f"Correct! {explanation}\n")
    else:
        print(f"Wrong! The correct answer is: {correct_choice}. {explanation}\n")

if __name__ == "__main__":
    for _ in range(8):
        trivia_game()

