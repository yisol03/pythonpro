import random

words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')

print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n")

att = random.randrange(0, 8)
word = words[att]
n = len(word)
correct = [n]
print("Length of the selected word: ", n)
while n > 0:
    print("Remaining attempts: ", n)
    for i in word:
        print("_ ", end = " ")
    
    guess = input("Guess a letter: ")
    if guess in word:
        for i in word:
            if word[i] == guess:
                
    
