### basic hangman game which asks you for countries in the EU. There are 3 difficulties to choose from.
### the game shows you the word in "_" and your lives. Try it out and have some fun :)

import random

def main():
    print("HANGMAN\n")
    print("Choose a difficulty (enter the number): ")
    print("1. Easy \n2. Medium \n3. Hard")
    print("4. Quit")

    while True:
        try:
            mode = int(input("\n> "))
        except:
            print("Invalid input. Please try again.")
            continue

        if mode == 1:
            easy()
            break
        elif mode == 2:
            medium()
            break
        elif mode == 3:
            hard()
            break
        elif mode == 4:
            print("Quitting...")
            exit()
        else:
            print("Invalid input. Please try again.")
            continue

def easy():
    countries = ["bulgaria", "estonia", "france", "italy", "ireland", "monaco", "san marino", "spain", "vatican city"]
    word = random.choice(countries)
    lives = 9
    guessed = []

    while lives > 0:
        print("Lives:",lives)
        output = ""
        for letter in word:
            if letter in guessed:
                output += letter
            else:
                output += "_"

        print("\n" + output)
        if output == word:
            print("You win!")
            break

        try:
            guess = str(input("Please enter your guess: ")).lower()
        except:
            print("Invalid input. Please try again.")
            continue

        if guess in guessed:
            print("You already guessed that letter. Please try again.")
            continue
        elif guess not in word:
            print("Incorrect. You lose a life")
            lives -= 1
            continue
        else:
            guessed.append(guess)

    if lives == 0:
        print("You lose. The word was " + word)

def medium():
    countries = ["austria", "belgium", "croatia", "denmark", "finland", "germany", "greece", "hungary", "lithuania", "latvia", "malta", "netherlands", "poland", "slovakia", "slovenia", "switzerland"]
    word = random.choice(countries)
    lives = 9
    guessed = []

    while lives > 0:
        print("Lives:",lives)
        output = ""
        for letter in word:
            if letter in guessed:
                output += letter
            else:
                output += "_"

        print("\n" + output)
        if output == word:
            print("You win!")
            break

        try:
            guess = str(input("Please enter your guess: ")).lower()
        except:
            print("Invalid input. Please try again.")
            continue

        if guess in guessed:
            print("You already guessed that letter. Please try again.")
            continue
        elif guess not in word:
            print("Incorrect. You lose a life")
            lives -= 1
            continue
        else:
            guessed.append(guess)

    if lives == 0:
        print("You lose. The word was " + word)

def hard():
    countries = ["albania", "andorra", "armenia", "azerbaijan", "belarus", "bosnia and herzegovina", "cyprus", "czech republic", "georgia", "greenland", "iceland", "liechtenstein", "luxembourg", "macedonia", "moldova", "montenegro", "norway", "portugal", "romania", "russia", "serbia", "sweden", "ukraine", "united kingdom"]
    word = random.choice(countries)
    lives = 9
    guessed = []

    while lives > 0:
        print("Lives:",lives)
        output = ""
        for letter in word:
            if letter in guessed:
                output += letter
            else:
                output += "_"

        print("\n" + output)
        if output == word:
            print("You win!")
            break

        try:
            guess = str(input("Please enter your guess: ")).lower()
        except:
            print("Invalid input. Please try again.")
            continue

        if guess in guessed:
            print("You already guessed that letter. Please try again.")
            continue
        elif guess not in word:
            print("Incorrect. You lose a life")
            lives -= 1
            continue
        else:
            guessed.append(guess)

    if lives == 0:
        print("You lose. The word was " + word)

main()