import random

# 사용할 단어 목록
words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "orange"]

# 무작위로 단어 선택
def choose_word():
    return random.choice(words)

# 게임 실행
def hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6  # 틀릴 수 있는 횟수

    print("Welcome to Hangman!")
    
    while True:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print("Word: " + display_word)
        print("Tries left: " + str(tries))
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            print("Wrong guess!")
            tries -= 1
        
        if "_" not in display_word:
            print("Congratulations! You've guessed the word: " + word)
            break
        
        if tries == 0:
            print("Out of tries! The word was: " + word)
            break

if __name__ == "__main__":
    hangman()
