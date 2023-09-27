import random

hero = random.randrange(50, 101)
monster = random.randrange(50, 101)

print("hero HP: ", hero, ", monster HP: ", monster, "\n")

i=0
while hero>0 and monster>0:
    
    heroatt = random.randrange(-10, 21)
    monsteratt = random.randrange(-10, 21)

    if heroatt <= 0:
        res1 = "fail"
    else:
        res1 = "success"

    if monsteratt <= 0:
        res2 = "fail"
    else:
        res2 = "success"

    if res1 == "success":
        monster = monster - heroatt
    if res2 == "success":
        hero = hero - monsteratt

    print("hero(HP:",hero,", attck:",heroatt,")", res1, "<-> monster(HP:",monster,", attck:",monsteratt,")", res2)

    i+=1
    if hero <= 0:
        win = "Monster"
    else:
        win = "Hero"

print("\n------------------------------------------------\n")
print("Total phase: ", i)
print("\n",win,"Win!!!!")
