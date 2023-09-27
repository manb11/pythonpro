import random

mood = random.randrange(0,2,1)

if mood == 0:
  print("I sense your happy. Your true emotions are coming across my screen.")
  print("you are . . .")
  print("          -----------")
  print("          |         |")
  print("          | ^    ^  |")
  print("          |   V     |")
  print("          -----------")

elif mood == 1:
  print("I sense your sed. Your true emotions are coming across my screen.")
  print("you are . . .")
  print("          ----------")
  print("          |        |")
  print("          | T   T  |")
  print("          |   o    |")
  print("          ----------")

elif mood == 2:
  print("I sense your angry. Your true emotions are coming across my screen.")
  print("you are . . .")
  print("          ----------")
  print("          |        |")
  print("          |\\  /   |")
  print("          |   n    |")
  print("          ----------")

else :
  print("Illegal moodcalue!")
print(mood)
