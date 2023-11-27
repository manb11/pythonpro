#p20

class Critter:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("A new critter has been born!")
        print("Hi. I'm", self.name, "\n")

    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep


crit1 = Critter("poochie")
crit2 = Critter("Randolph")
crit1.talk()
crit2.talk()


num1 = int(input("chose 1 or 2: "))
print(" ")
if num1 == 1 :
    print("Printing crit1: ")
    print(crit1)
else :
    print("Printing crit2: ")
    print(crit2)

num2 = int(input("chose 1 or 2: "))
print(" ")
if num2 == 1 :
    print("Directly accessing crit1. name: ")
    print(crit1.name)
else :
    print("Directly accessing crit2. name: ")
    print(crit2.name)

a = input("\n\nPress the enter key to exit.")

if a == "":
    print(" ")
