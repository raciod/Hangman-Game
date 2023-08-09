import random
from words import words

hangman = {
    1: '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''',
    2: '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''',
    3: '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''',
    4: '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''',
    5: '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    ''',
    6: '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    ''',
    7: '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    '''
}

word = random.choice(words).strip().upper()  # Convert the chosen word to uppercase and remove any extra spaces
word = set(word)
print(word)
guesses = []
tries = 7
index = 1

while tries > 0:
    if all(letter in guesses for letter in word):
        print("Congratulations! You guessed the word:", word)
        break
    
    letter = input("Type your letter: ").strip().upper()  # Convert the input to uppercase and remove extra spaces
    
    if letter in guesses:
        print("You already guessed that letter.")
        tries -= 1
    else:
        if letter in word:
            guesses.append(letter)
            print("Correct!")
        else:
            print(hangman[index])  # Print the corresponding hangman figure
            index += 1
            tries -= 1
            print("Incorrect!")
    
    print("Guessed letters:", guesses)

if tries == 0:
    print(hangman[7])
    print("Game over! The word was:", word)

