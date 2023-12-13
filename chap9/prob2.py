#p16

class Critter:
    def __init__(self, crit1, crit2):
        self.crit1 = crit1
        self.crit2 = crit2

    def a(self):
        print("A new critter has been born!")

    def b(self):
        print("Hi. I'm an instance of class Critter.")


# Create instances
crit1 = Critter("value1", "value2")
crit2 = Critter("value3", "value4")

# Call methods on instances
crit1.a()
crit1.a()
print(" ")
crit2.b()
crit2.b()

print("\n\n")

a = input("Press the enter key to exit.")

if a == "":
    print(" ")
