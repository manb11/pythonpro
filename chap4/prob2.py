import random as r

hero = r.randrange(50, 100)
monster = r.randrange(50, 100)

num=0

print("hero HP:", hero, "monster HP:", monster)

while hero > 0 and monster > 0:
    
    num = num+1
    
    hatt = r.randrange(-10, 20)
    matt = r.randrange(-10, 20)

    hero1 = hero - matt
    monster1 = monster - hatt

    print("hero(HP:", hero1, ", attack:", hatt, ")", end=' ')
    if hatt <= 0:
        print("fail", end='')
    else:
        print("success", end='')

    print(" <-> monster(HP:", monster1, ", attack:", matt, ")", end=' ')
    if matt < 0:
        print("fail")
    else:
        print("success")

    hero = hero1
    monster = monster1

print("Total phase: ",num)

if hero <= 0:
    print("Hero Win!!!")
else:
    print("Monster Win!")

