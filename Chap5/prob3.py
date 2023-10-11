import random

words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')

print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n")

word = random.choice(words)
n = len(word)

guessed = []

print("Length of the selected word: ", n)

while n > 0:
	if all(letter in guessed for letter in word):
		print("Congratulations! You guessed the word: ", word)
		break

	print("Remaining attempts: ", n)
	dword = ''.join([letter if letter in guessed else '_ ' for letter in word])
	print("Current guessed word: ", dword)
	guess = input("Guess a letter: ")

	if len(guess) == 1 and guess.isalpha() and guess not in guessed:
		guessed.append(guess)

	if guess in word:
		continue
	else:
		print("Incorrect guess.")
		n -= 1

if n == 0:
	print("You've used up all your attempts. The correct word was", word)
