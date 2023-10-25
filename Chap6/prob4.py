import random

def draw_hangman(wrong_attempts):
    hangman = [
        "  ____",
        "  |  |",
        "  |",
        "  |",
        "  |",
        "  |",
        "  |",
        " / \\",
        "/   \\",
    ]

    if wrong_attempts == 0:
        return hangman[:3] + ["  |"] * 5
    elif wrong_attempts == 1:
        return hangman
    elif wrong_attempts == 2:
        hangman[2] = "  |  O"
        return hangman
    elif wrong_attempts == 3:
        hangman[3] = "  |  |"
        return hangman
    elif wrong_attempts == 4:
        hangman[4] = "  | /|"
        return hangman
    elif wrong_attempts == 5:
        hangman[4] = "  | /|\\"
        return hangman
    elif wrong_attempts == 6:
        hangman[5] = "  | /"
        return hangman
    elif wrong_attempts == 7:
        hangman[5] = "  | / \\"
        return hangman

def choose_word():
    words = [ 'difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university' ]
    return random.choice(words).upper()

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    word_to_guess = choose_word()
    guessed_letters = []
    correct = []
    max_attempts = 7
    wrong_attempts = 0

    while True:
        print("\n" + " ".join(guessed_letters))
        print("\n" + display_word(word_to_guess, guessed_letters))

        guess = input("Enter your guess: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter the correct letter.")
            continue

        if guess in guessed_letters:
            print("It's a letter I've already guessed.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Yes!", guess, "is in the word!")
            correct.append(guess)
            print(correct,"\n", word_to_guess)
            if word_to_guess == correct:
                print("Congratulations! The answer is" ,{word_to_guess})
                break
        else:
            wrong_attempts += 1
            print("Incorrect!")
            if wrong_attempts == max_attempts:
                print("Game Over! Word was", {word_to_guess})
                break

        hangman_display = draw_hangman(wrong_attempts)
        for line in hangman_display:
            print(line)

if __name__ == "__main__":
    main()
