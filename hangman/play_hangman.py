"""This module contains hangman game logic"""
import random


def chose_word():
    """Choosing word from file function"""
    file = open('/home/gerrhorr/PycharmProjects'
                '/python-education/hangman'
                '/game_library.txt')
    words_list = [x.strip() for x in file]
    file.close()
    word = random.choice(words_list)
    return word


def check_guessed_words():
    """Read file of guessed words"""
    file = open('/home/gerrhorr/PycharmProjects'
                '/python-education/hangman'
                '/guessed_words.txt')
    guessed_words = [x.strip() for x in file]
    if guessed_words:
        print(guessed_words)
    else:
        print("Not much here for now")
    file.close()


def write_guessed_word(*args):
    """Writes guessed words in file"""
    file = open('/home/gerrhorr/PycharmProjects'
                '/python-education/hangman'
                '/guessed_words.txt')
    guessed_words = [x.strip() for x in file]
    file.close()
    if args not in guessed_words:
        guessed_words.append(args)
    else:
        pass
    file = open('/home/gerrhorr/PycharmProjects'
                '/python-education/hangman'
                '/guessed_words.txt', 'w')
    for x in guessed_words:
        file.write(f'{x}\n')
    file.close()


def game_manu():
    """Game menu logic"""
    print("########################"
          "\n# Hangman by Plotnikov #"
          "\n########################"
          "\n_______________________"
          "\n* S - start the game"
          "\n* L - watch guessed words"
          "\n* Q - quit the game")
    choice = input('\nType your choice: ').upper()
    if choice == "S":
        play()
    elif choice == "L":
        check_guessed_words()
        while input('Type "Q" to return to menu!').upper() == "Q":
            game_manu()
    else:
        quit()


def win_statement(word, stuffing):
    """Resolution of win"""
    write_guessed_word(word)
    print(stuffing)
    a = input("You win!"
              "\nWanna play again? (Y/N)").upper()
    if a == "Y":
        play()
    else:
        game_manu()


def lost_statement(word):
    """Resolution of lost"""
    b = input(f'Oh no, you lost!'
              f'\n The word was {word.upper()}'
              f'\nWanna play again? (Y/N)').upper()
    if b == "Y":
        play()
    else:
        game_manu()


def print_visuals(stuffing, tries, mentioned_letters, mentioned_words):
    """Function for printing visual part of a game"""
    print(f"\nWhat is {stuffing}?"
          f"\n"
          f"\nTries: {tries}"
          f"\n Letters: {mentioned_letters}"
          f"\n Words: {mentioned_words}")


def stuffing_the_word(stuffing, guess, word):
    """Function for filling the empty spaces
    and checking for victory"""
    buffer = [x for x, letters in enumerate(word) if letters == guess]
    for x in buffer:
        stuffing[x] = guess
    if "_" not in stuffing:
        win = True
        win_statement(word, stuffing)


def verify_letter(guess, stuffing, tries, word, mentioned_letters, win):
    """Checking in for letter in a word
    or in a mentioned pool"""
    if guess in mentioned_letters:
        print(f'Letter "{guess}" were mentioned before!')
    elif guess not in word:
        print(f'There is no "{guess}" in there!')
        tries -= 1
        mentioned_letters.append(guess)
    else:
        print(f'{guess} is in the word!')
        mentioned_letters.append(guess)
        stuffing_the_word(stuffing, guess, word)
    return tries


def verify_word(guess, stuffing, tries, word, mentioned_words, win):
    """Checking in for guess is a word
        or in a mentioned pool"""
    if guess in mentioned_words:
        print(f'{guess} were mentioned before!')
    elif guess != word:
        print(f'{guess} not the word!')
        mentioned_words.append(guess)
        tries -= 1
    else:
        stuffing = list(word.upper())
        win = True
        win_statement(word, stuffing)
    return tries


def game_cycle(stuffing, tries, word, mentioned_letters,
               mentioned_words, win):
    """Function of game cycle"""
    while not win and tries > 0:
        guess = input("Enter your guess: ").upper()
        if len(guess) == 1:
            tries = verify_letter(guess, stuffing, tries,
                                  word, mentioned_letters,
                                  win)
        elif len(guess) == len(word):
            tries = verify_word(guess, stuffing, tries,
                                word, mentioned_words,
                                win)
        else:
            print("Invalid guess")
        print_visuals(stuffing, tries, mentioned_letters, mentioned_words)
    return win


def header_print():
    """Prints opening titles"""
    print("######################"
          "\n# It`s Hangman time #"
          "\n######################"
          "\nyou may guess a letter"
          "\nor a whole word")


def win_ro_lost(win, word, stuffing):
    """Deciding function"""
    if win:
        win_statement(word, stuffing)
    else:
        lost_statement(word)


def play():
    """Game logic function"""
    word = chose_word().upper()
    stuffing = list("_" * len(word))
    tries, win = 6, False
    mentioned_letters = []
    mentioned_words = []
    header_print()
    print_visuals(stuffing, tries, mentioned_letters, mentioned_words)
    win = game_cycle(stuffing, tries, word, mentioned_letters,
                     mentioned_words, win)
    win_ro_lost(win, word, stuffing)


if __name__ == "__main__":
    game_manu()
