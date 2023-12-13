#p44

class Critter:

    def __init__(self, name):
        self.__name = name

    def talk(self):
        print("A new critter has been born!\n")
        print("Hi. I'm", self.name, "\n")

    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        if new_name == "":
            print("A Critter's name can't be empty string.")
        else:
            self.__name = new_name
            print("\nName change successful.")
    
    name = property(get_name, set_name)


crit = Critter("Poochie")

crit.talk()

print("My critter's name is: ", crit.get_name(), "\n")

while True:
    new_name = input("Attemting to change my critter's name.\n")
    crit.set_name(new_name)
    if crit.get_name() != "":
        break

print("\nHi, I'm", crit.get_name())


a = input("\n\nPress the enter key to exit.")

if a == "":
    print(" ")
