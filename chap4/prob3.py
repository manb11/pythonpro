import random as r
num = r.randrange(1,100)

print("         Welcome to 'Guess My Number'!")
print("")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

a = 0

while True:
    
    a = a+1
    
    n = int(input("Take a guess: "))
    
    if num < n:
        print("Lower...")
    else:
        print("Higher...")
    
    if num == n:
        break
    

print("You guessed it! The number was ",n)
print("And it only took you ",a," tries!")
