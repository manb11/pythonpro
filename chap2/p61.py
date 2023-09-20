print("         Trust Fund Buddy  ")

print("Totals your monthly spending so that your trust fund doesn't run out")
print("<and you're forced to get a real job>.")

print("Please enter the requested, monthly costs. Since you're rich, ignore pennies and use only dollar amounts.")

car = int(input("Lamborghini Tune-Ups: "))
rent = int(input("Manthttan Apartment: "))
jet = int(input("Prinate Jet Rental: "))
gifts = int(input("Gifts: "))
food = int(input("Dinig Out: "))
staff = int(input("Staff (buters, chef, driver, assistant): "))
guru = int(input("Personal guru and Coach: "))
games = int(input("Computer Games: "))
total = car+rent+jet+gifts+food+staff+guru+games

print("Grand Total: ", total)
