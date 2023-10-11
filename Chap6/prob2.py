from operator import itemgetter

scores = { "Moe" : 1000, "Larry" : 1500, "Curly" : 3000 }
zxcv = {}
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
		scores[name] = score

	else:
		print("\nHigh Scores")
		print("\nNAME\tSCORE")
		zxcv = sorted(scores.items(), key=lambda x: x[1], reverse=True)
		for key, value in zxcv.items():
			print(key,"\t",value)
