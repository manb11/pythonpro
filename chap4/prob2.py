import random as r

hero = r.randrange(50, 100)
monster = r.randrange(50, 100)

hatt = r.randrange(-10, 20)
matt = r.randrange(-10, 20)

a = "fail"
b = "sucess"

print("hero HP: ,",hero, "monter HP: ,",monster)

while hero > 0 or monster > 0:
 
 hero1 = hero - hatt
 monster1 = monster - matt
 

 print("hero(HP:",hero1,", attck:",hatt,")",end='')

 if hatt<0:  print(a,end='')
 else: print(b,end='')

 print(" <-> monster(HP:",monster1,", attck:",matt,")")

 if matt<0: print(a,end='')
 else: print(b,end='')

