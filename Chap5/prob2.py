import random

words = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")

print("Welcome to Word Jumble!")
print("Unscramble the letters to make a word.")

jum = random.randrange(0, 7)

tmp = []
for x in words[jum]:
    tmp = tmp + [[random.random(), x]]

tmp.sort()
tmp2 = []
for y in tmp:
    tmp2 = tmp2 + [y[1]]

word = ''.join(tmp2)
print("Jumbled word: ", word)

guess = input("Your guess: ")
if guess == words[jum]:
    print("That's correct!!")
else:
    print("Sorry, that's not correct. The word was:", words[jum])
    
