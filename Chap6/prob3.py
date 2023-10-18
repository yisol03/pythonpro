geek = { "404" : "clueless.", "Uninstalled" : "being fired." }

while(1):
	print("\n\tGeek Translator")
	print("\n\t0 - Quit")
	print("\t1 - Look Up a Geek Term")
	print("\t2 - Add a Geek Term")
	print("\t3 - Delete a Geek Term")

	choice = input("\nChoice: ")
	choice = int(choice)

	if choice == 0:
		break

	elif choice == 1:
		look = input("What term do you want me to translate?: ")
		if look in geek:
			print("\n", look, "means", geek[look], ".  Especially popular during the dot-bomb era.")
		else:
			print("\nI have no idea what", look, "is.")

	elif choice == 2:
		get = input("\nEnter the term: ")
		get2 = input("Enter translation: ")
		geek[get] = get2

	else:
		dele = input("\nEnter the term to delete: ")
		del geek[dele]
