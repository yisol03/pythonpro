inventory = ()
if not inventory:
    print("You are empty-handed.")

inventory = [ "sword", "armor", "shield", "healing potion" ]
print("\nThe tuple inventory is:\n", inventory)

print("\nYour items:")
for item in inventory:
    print(item)

pos = input("\nPress the enter key to continue.")
if pos == "":
    print("You have", len(inventory), "items in your possession.")

day = input("\nPress the enter key to continue.")
if day == "":
    if "healing potion" in inventory:
        print("You will live to fight another day.")

ind = input("\nEnter the index number for an item int inventory: ")
ind = int(ind)
print("At index", ind, "is", inventory[ind])

begin = input("\nEnter the index number to begin a slice: ")
end = input("Enter the index number to end the slice: ")
begin = int(begin)
end = int(end)
print("inventory[", begin, ":", end, "]\t\t", inventory[begin:end])

con = input("\nPress the enter key to continue.")
if con == "":
    chest = ("gold", "gems")
    print("You find a chest. It contains:")
    print(chest)
    print("You add the contents of the chest to your inventory.")
    print("Your inventory is now: ")
    inventory += chest
    print(inventory)

trad = input("\nPress the enter key to continue.")
if trad == "":
	inventory[0] = "crossbow"
	print("You trade your sword for a crossbow.")
	print("Your inventroy is now: ")
	print(inventory)

tell = input("\nPress the enter key to continue.")
if tell == "":
	inventory[4:6] = ["orb of future telling"]
	print("You use your gold and gems to buy an orb of future telling.")
	print("Your inventory is now: ")
	print(inventory)

dest = input("\nPress the enter key to continue.")
if dest == "":
	del inventory[2]
	print("In a great battle, your shield is dstroyed.")
	print("Your inventory is now: ")
	print(inventory)

thie = input("\nPress the enter key to continue.")
if thie == "":
	del inventory[:2]
	print("Your crossbow and armor are stolen by thieves.")
	print("Your inventory is now: ")
	print(inventory)
	
