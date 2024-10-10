# Hangman game
# 
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # Allways False till all letters are righte
    for i in secret_word:
        if i not in letters_guessed:
            return False
      
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    guessed_word =  []

    for i in secret_word:
       if i in letters_guessed:
          guessed_word.append(i)
       else:
          guessed_word.append("_")
    return"".join(guessed_word)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    lowercase_letters = string.ascii_lowercase

    available_letters = [i for i in lowercase_letters if i not in letters_guessed]
    return''.join(available_letters)



                    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    '''

    '''
    * At the start of the game, let the user know how many 
      letters the secret_word contains.
    
    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    letters_guessed = []
    guesses = 0
    limit = 8


    print(f"Hello! Guess the secret word before you tries run out. Your word has {len(secret_word)} letters")

    while guesses < limit + 1:

      #### Ending the Game: ####

      #Winning

      if is_word_guessed(secret_word, letters_guessed) == True:
        print(f"Wuuh - you won the word is {secret_word}")
        break

      #Loosing

      else:
        if guesses == limit:
          print(f"Oh no you lost :( the word woulf have been {secret_word}")
          break

        else:
           guess = input("Enter a letter you want to guess,").lower()

           if guess in letters_guessed:
            print(f"You allready tried letter {guess} , choos anotherone")
            print(f"You have {limit - guesses} left")
            continue

           if guess in secret_word:
            
            letters_guessed.append(guess)
            
            print(f"Good guess the letter {guess} is in the search word")
            print(f"You have {limit - guesses} left")

            progress = get_guessed_word(secret_word, letters_guessed)
            print(f"This is the progress you made so far: {progress}")

            available_letters = get_available_letters(letters_guessed)
            print(f"You can choose one of the follwing letters: {available_letters}")

            continue

           else:
            letters_guessed.append(guess)

            progress = get_guessed_word(secret_word, letters_guessed)
            print(f"This is the progress you made so far: {progress}")

            available_letters = get_available_letters(letters_guessed)
            print(f"You can choose one of the follwing letters: {available_letters}")
            guesses += 1
            print(f"You have {limit - guesses} left")
       




secret_word = choose_word(wordlist).lower()
hangman(secret_word) 
