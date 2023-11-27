#p27

class Critter:
    total = 0

    def __init__(slef, name):
        Critter.total +=1

    def talk(self):
        print("A new critter has been born!")

    @staticmethod
    def status():
        print("Total critter", Critter.total)

print("Accessing the class attribute Critter.total: ",Critter.total)

print("\n")

crit1 = Critter("critter 1")
crit1.talk()
crit2 = Critter("critter 2")
crit2.talk()
crit3 = Critter("critter 3")
crit3.talk()

print("\n")

print("The total number of critters is ", crit1.total)

print("\n")

print("Accessing the class atrribute through an object: ", Critter.total)

a = input("\n\nPress the enter key to exit.")

if a == "":
    print(" ")
