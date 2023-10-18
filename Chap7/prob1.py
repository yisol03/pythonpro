import random

board[3][3] = {' ', ' ', ' '
		 ' ', ' ', ' '
		 ' ', ' ', ' '}	 
def instructions():
		print("\n\tWelcome to the world's greatest game!")
		print("\tThis will be a showdown between your human brain and my silicon processor.")
		print("\n\n\tYou will make your move known by entering a number, 0 - 8.")
		print("\tThe number will correspond to the board position as illustrated:")
		print("\n\t\t\t\t\t0 | 1 | 2")
		print("\t\t\t\t\t---------")
		print("\t\t\t\t\t3 | 4 | 5")
		print("\t\t\t\t\t---------")
		print("\t\t\t\t\t6 | 7 | 8")
		print("\n\tPrepare yourself, human. The ultimate battle is about to begin.")

def ask(question):
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()
	return response

def game():
		
		print("I shall take square number 4")
		for i in board:
			if board[i] != ' ':
				
	while(1):
		hum = input("Where will you move? <0 - 8>: ")
		hum = int(hum)


instructions()
ans = ask("Do you require the first move? (y / n): ")
if ans == 'y':
	
