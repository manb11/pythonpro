import random

words = ["apple", "banana", "python", "catholic", "university", "mango"]
word_to_guess = random.choice(words)

mistakes_left = 6
guessed_letters = []

stages = [
    """
    --------  
    |      |   
    |      O   
    |     /|\\  
    |     / \\  
    |      
    ----------""",
    """
    --------  
    |      |   
    |      O   
    |     /|\\  
    |     / 
    |      
    ----------""",
    """
    --------  
    |      |   
    |      O   
    |     /|\\  
    |      
    |      
    ----------""",
    """
    --------  
    |      |   
    |      O   
    |     /|
    |       
    |      
    ----------""",
    """
    --------  
    |      |   
    |      O   
    |      | 
    |   
    |      
    ----------""",
    """
    --------  
    |      |   
    |      O   
    |     
    |     
    |      
    ----------""",
    """
    --------  
    |      |   
    |     
    |     
    |     
    |      
    ----------"""
]

display_word = ['_'] * len(word_to_guess)

def display_game():
    print("Word: " + " ".join(display_word))
    print("Mistakes left:", mistakes_left)
    print("Guessed letters:", " ".join(guessed_letters))
    print(stages[mistakes_left])

while mistakes_left > 0 and '_' in display_word:
    display_game()
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        mistakes_left -= 1

display_game()

if '_' not in display_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("You ran out of guesses. The word was:", word_to_guess)
