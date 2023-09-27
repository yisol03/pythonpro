import random

mood = random.randrange(1, 4)
mood = int(mood)

print("I sense your energy. Your true emotions are coming across my screen.\n")
print("You are...\n\n")

if mood == 1:
    print("__________\n")
    print("|        |\n")
    print("| o   o  |\n")
    print("|   <    |\n")
    print("| .   .  |\n")
    print("|  ...   |\n")
    print("|________|\n")
    print("\n...today.")

if mood == 2:
    print("__________\n")
    print("|        |\n")
    print("| o   o  |\n")
    print("|   <    |\n")
    print("|        |\n")
    print("|  ....  |\n")
    print("|________|\n")
    print("\n...today.")

if mood == 3:
    print("__________\n")
    print("|        |\n")
    print("| o   o  |\n")
    print("|   <    |\n")
    print("|        |\n")
    print("|  ...   |\n")
    print("|_.___.__|\n")
    print("\n...today.")


