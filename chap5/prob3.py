import random as r

print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n")

words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')

rd_word = r.choice(words)
guessed_word = '_' * len(rd_word)
remaining_attempts = 6

print("Length of the selected word:", len(rd_word), "\n")

while remaining_attempts > 0:
    print("Remaining attempts:", remaining_attempts)
    
    gap = ' '.join(guessed_word)
    print("Current guessed word:", gap)

    input_word = input("Guess a letter: ")

    if input_word in rd_word:
        for i in range(len(rd_word)):
            if rd_word[i] == input_word:
                guessed_word = guessed_word[:i] + input_word + guessed_word[i+1:]
    else:
        print("Incorrect guess.")
        remaining_attempts -= 1

    if guessed_word == rd_word:
        print("Congratulations! You guessed the word:", rd_word)
        break

if guessed_word != rd_word:
    print("You've used up all your attempts. The correct word was", rd_word)

