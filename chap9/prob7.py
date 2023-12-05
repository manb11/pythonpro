class Critter(object):

    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom


    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        for mood, level in self.mood_levels.items():
            if unhappiness <= level:
                return mood


    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()


    def custom_talk(self, conversation_level=1):
        conversations = {
            1: "Hello there!",
            2: "I'm feeling good today.",
            3: "I'm soso.",
            4: "I'm not in the mood for talking."
        }

        if 1 <= conversation_level <= 4:
            print(conversations[conversation_level])
            self.__pass_time()
        else:
            print("Invalid conversation level.")


    def eat(self, food = 4):
        print("Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()


    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("What your critter's name ?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
        ("""
         Critter Caretakeer
         0 - Quit
         1 - Listen to your critter
         2 - Feed your critter
         3 - Play with your critter
         """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good bye.")

        elif choice == "1":
            conversation_level = int(input("Enter conversation level (1-4): "))
            crit.custom_talk(conversation_level)

        elif choice == "2":
            crit.eat()

        elif choice == "3":
            crit.play()

        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit")
