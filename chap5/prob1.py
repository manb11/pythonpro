# a reference site: https://devsnote.com/asks/2342

# 1. 
while True:
    inventory = ("sword", "armor", "shield", "healing potion")

    if not inventory:
        print("you are empty")
    else:
        print("Your items: ")

    for item in inventory:
        print(item)

    print("")
    text = input("Press the enter key to continue")
    if  text == '':
        break
    else:
        print("You must press 'enter'")

# 2. 
while True:
    print("You have", len(inventory), "items in your possesion.")

    print("")
    text = input("Press the enter key to continue")
    if  text == '':
        break
    else:
        print("You must press 'enter'")

# 3. 
if "healing potion" in inventory:
    print("You will live to fight another day.")
    print("")

# 4.
while True:
    index = int(input("Enter the index numver for an item in inventory: "))

    if 0<= index <len(inventory):
        item = inventory[index]
        print("At index", index, "is", item)

# 5. 
    print("")
    start = int(input("Enter the index to begin a slice: "))
    end = int(input("Enter the index to end the slice: "))

    if 0<= index <len(inventory) and 0<= index < len(inventory):
        sli = inventory[start:end]
        print("inventory[",start,":", end,"]       ",sli)
    else:
        print("doesn't exits index")
    
    print("")
    text = input("Press the enter key to continue")
    if  text == '':
        break
    else:
        print("You must press 'enter'")

# 6.
while True:
    chest = ("gold", "gems")

    print("")
    print("You find a chest. It contains: ")
    print(chest)
    
    print("You add the contents of the chest to your inventory.")
    
# 7.
    inventory += chest
    
    print("your inventory is now:")
    print(inventory)
    print("")


    text = input("Press the enter key to exit.")
    if  text == '':
        break
    else:
        print("You must press 'enter'")
