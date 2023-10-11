import sys
import random
# Import whatever other libraries you need

# G and Y represent text formatting codes for green and
# yellow text output. Variable names are brief so as to
# be unobtrusive when interspersed with text
G = '\x1b[0;30;42m'  # green text
Y = '\x1b[0;30;43m'  # yellow text
N = '\x1b[0m'        # normal text/no highlighting

ALLOWED_GUESSES = 6
WORD_LENGTH = 5
NUMBER_ONE = 1


def main(args):
    # TODO: If there is an argument, set that argument to be the word.
    # Otherwise, the word should be randomly selected from valid
    # letters of WORD_LENGTH in the Scrabble words file. (Use a
    # separate function to get the valid words from the
    # Scrabble words files)
    if len(args[1]) == WORD_LENGTH:
       index_word = args[1].upper()
    else:
       index_word = get_valid_words()

    # TODO: Study the following string to underestand how G, Y and N
    # behave for colored text highlights
    print(f"Welcome to {Y}PY{G}WOR{Y}D{G}LE{N}!")
    # TODO: You'll want a list to collect failed guesses. You can use
    # this list to print the guesses each time, and also use
    # the list's length to keep track of how many guesses have
    # been made
    guss_word = ''
    failed_guess = []
       
    # TODO: You'll probably want a while loop to continue as long
    # as the user's answer is not correct and the guesses are
    # fewer than the allowed number of guesses.
    guess_word = ""
    while guess_word != f"{index_word}":
       # TODO: You may want yet another while loop to repeat the prompt
       # in case of invalid guesses
        guess_word = input("Enter your guess:\n").upper()
        while len(guess_word) != WORD_LENGTH:
          guess_word = input("Please enter the vaild guess:\n").upper()
       # TODO: Use a separate function, format_guess, to format
       # the guess with green and yellow highlighting for printing out.
       # That's where you'll compare it to the correct word.
        revise_word = format_guess(guess_word, index_word)
       # TODO: Print out the list of guesses so far with each new guess
        failed_guess = failed_guess.append(revise_word)
        for i in range (len(failed_guess)):
             print(i)
        # TODO: Print an appropriate message when the game ends
        if guess_word == f"{index_word}":
           print(f"Congrats! You got it in {len(failed_guess)} tries.")
        elif len(failed_guess) == ALLOWED_GUESSES:
           print(f"Sorry, the word was {index_word}")

def format_guess(guess_word, index_word):  # TODO: Add necessary parameters

    # TODO: Implement this function so that it returns
    # the guess string highlighted with green and yellow based
    # on comparing letters with the original word.
    revise_word = ""
    for i in range (WORD_LENGTH):
          if guess_word == index_word:
            revise_word += f"{G}{guess_word[i]}"
          elif guess_word[i] in index_word:
            revise_word += f"{Y}{guess_word[i]}"
          else:
            revise_word += f"{N}{guess_word[i]}"
    revise_word += f"{N}"
    return revise_word
   
    # See assignment instructions for specifics about how
    # letters should be highlighted


def get_valid_words():  # TODO: Add necessary parameters

    # TODO: Implement this function so that it returns
    # a list of words consisting of only words of the
    # correct length from the Scrabble word list
  with open('Collins Scrabble Words (2019).txt', 'r', encoding="utf-8") as f:
        file = f.read().split("\n")
        for word in file:
            if len(word) == WORD_LENGTH:
               with open("words.txt", 'w') as g:
                g.write(f"{word}\n")

main(sys.argv)
