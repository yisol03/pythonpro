from operator import itemgetter

scores = [ (1000, "Moe"), (1500, "Larry"), (3000, "Curly") ]
while True:
	print("\n\tHigh Scores Keeper")
	print("\n\t0 - Quit")
	print("\t1 - List Scores")
	print("\t2 - Add a Score")
	n = input("\nChoicie: ")
	n = int(n)

	if n == 0:
		break

	elif n == 2:
		name = input("What is player's name?: ")
		score = input("What score did the player get?: ")
		score = int(score)
		entry = (score, name)
		scores.append(entry)

	else:
		print("\nHigh Scores")
		print("\nNAME\tSCORE")
		scores.sort(reverse=True)
		for entry in scores:
			score, name = entry
			print(name, "\t", score)
