import random

print("\t\tWelcome to 'Guess My Number'1")
print("\nI'm Thinking of a number between 1 and 100.")
print("Try to guess it in as few attenpts as possible.")

guess = random.randrange(1, 101)

i=0
n = input("\nTake a guess: ")
n = int(n)

while n != guess:
    n = int(n)
    i+=1
    if n > guess:
        print("Lower...")
        n = input("Take a guess: ")
        continue
    elif n < guess:
        print("Higher...")
        n = input("Take a guess: ")
        continue
    else:
        break


print("You guessed it!\tThe number was",guess)
print("And it only took you",i,"tries!")
