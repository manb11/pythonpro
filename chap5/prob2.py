import random as r

words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')

rd_word = r.choice(words)

word_list = list(rd_word)
r.shuffle(word_list)

shu = ''.join(word_list)

print("Welcome to Word Jumble!")
print("Unscramble the letters to make a word.")

print("Jumbled word:",shu)


str = input("Your guess:" )

if str == rd_word:
    print("Correct !")
else:
    print("Sorry, that's not correct. The word was :",rd_word)
