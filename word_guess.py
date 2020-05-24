"""
File: word_guess.py
-------------------
Fill in this comment.
"""

import random

LEXICON_FILE = "Lexicon.txt"  # File to read word list from
INITIAL_GUESSES = 8  # Initial number of guesses player starts with


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)
    desire_to_play_again = play_another_game()
    while desire_to_play_again == "YES":
        play_another_game()


def play_another_game():
    """
    Summary:
    Parameters:
    Returns:
    """
    desire_to_play_again = input("Do you want to play again? Type YES or NO: ")
    desire_to_play_again = desire_to_play_again.upper()
    while (desire_to_play_again != "YES") and (desire_to_play_again != "NO"):
        desire_to_play_again = input("Please enter YES or NO:")
        desire_to_play_again = desire_to_play_again.upper()
    if desire_to_play_again == "YES":
        secret_word = get_word()
        play_game(secret_word)
    else:
        print("Goodbye!")
    return desire_to_play_again


def play_game(secret_word):
    """
    Summary:
    Parameters:
    Returns:
    """
    guess_list, remaining_guesses, concealed_word, original_concealed_word, \
    concealed_word_list = prepare_for_game(secret_word)
    while (concealed_word != secret_word) and (remaining_guesses > 0):
        print("You have " + str(remaining_guesses) + " guesses left")
        user_guess = ask_for_input()
        while (len(user_guess) > 1) or (user_guess.isalpha() is False):
            user_guess = request_correct_type_guess(concealed_word, user_guess,
                                                    guess_list)
        user_guess = user_guess.upper()
        if user_guess not in concealed_word:
            guess_list.append(user_guess)
        concealed_word_list = check_for_correct_guess(secret_word, user_guess,
                                                      concealed_word_list)
        concealed_word = ""
        concealed_word = update_concealed_word(concealed_word_list,
                                               concealed_word)
        remaining_guesses, original_concealed_word = check_for_progress(
            concealed_word, original_concealed_word, remaining_guesses,
            user_guess, guess_list, secret_word)


def prepare_for_game(secret_word):
    """
    Summary:
    Parameters:
    Returns:
    """
    guess_list = []
    remaining_guesses = INITIAL_GUESSES
    concealed_word = create_concealed_word(secret_word)
    original_concealed_word = concealed_word
    concealed_word_list = create_concealed_word_list(concealed_word)
    print("The word now looks like this: " + concealed_word)
    return guess_list, remaining_guesses, concealed_word, \
           original_concealed_word, concealed_word_list


def check_for_progress(concealed_word, original_concealed_word,
                       remaining_guesses, user_guess, guess_list, secret_word):
    """
    Summary:
    Parameters:
    Returns:
    """
    if (concealed_word == original_concealed_word) and (user_guess not in
                                                        concealed_word):
        if remaining_guesses > 1:
            remaining_guesses = declare_incorrect_guess(user_guess,
                                                        remaining_guesses,
                                                        concealed_word,
                                                        guess_list)
        else:
            remaining_guesses = declare_lost_game(remaining_guesses,
                                                  secret_word)
    else:
        print("That guess is correct.")
        if concealed_word != secret_word:
            original_concealed_word = declare_correct_guess(concealed_word,
                                                            secret_word,
                                                            guess_list,
                                                       original_concealed_word)
        else:
            print("Congratulations, the word is: " + secret_word)
    return remaining_guesses, original_concealed_word


def update_concealed_word(concealed_word_list, concealed_word):
    """
    Summary:
    Parameters:
    Returns:
    """
    for elem in concealed_word_list:
        concealed_word += elem
    return concealed_word


def show_word_and_guesses(concealed_word, guess_list):
    """
    Summary:
    Parameters:
    Returns:
    """
    print("The word now looks like this: " + concealed_word)
    print("You have guessed: " + str(guess_list))


def ask_for_input():
    """
    Summary:
    Parameters:
    Returns:
    """
    user_guess = input("Type a single letter here, then press enter: ")
    return user_guess


def declare_correct_guess(concealed_word, secret_word, guess_list,
                          original_concealed_word):
    """
    Summary:
    Parameters:
    Returns:
    """
    show_word_and_guesses(concealed_word, guess_list)
    original_concealed_word = concealed_word
    return original_concealed_word


def declare_lost_game(remaining_guesses, secret_word):
    """
    Summary:
    Parameters:
    Returns:
    """
    remaining_guesses -= 1
    print("Sorry, you lost. The secret word was: " + secret_word)
    return remaining_guesses


def declare_incorrect_guess(user_guess, remaining_guesses, concealed_word,
                            guess_list):
    """
    Summary:
    Parameters:
    Returns:
    """
    print("There are no " + user_guess + "'s in the word")
    remaining_guesses -= 1
    show_word_and_guesses(concealed_word, guess_list)
    return remaining_guesses


def check_for_correct_guess(secret_word, user_guess, concealed_word_list):
    """
    Summary: This loops through secret_word, checking user_guess by
      each character. If user_guess is in secret_word, the element
      in concealed_word_list at the correct index (determined by
      position in secret_word) is re-assigned to user_guess.
    Parameters: secret_word {string}
                user_guess {string}
                concealed_word_list {list}
    Returns: concealed_word_list {list} -- updated with new correct
      character from user_guess
    """
    for i in range(len(secret_word)):
        ch = secret_word[i]
        if ch == user_guess:
            concealed_word_list[i] = user_guess
    return concealed_word_list


def request_correct_type_guess(concealed_word, guess_list, user_guess):
    """
    Summary: If user enters a number, symbol, or multiple alphabetic
      characters, this function asks user for correct type of guess
      (a single alphabetic character). The user enters a new guess,
      and user_guess is re-assigned.
    Parameters: concealed_word {string}
                guess_list {list}
                user_guess {string} -- either a number, symbol, or
                  multiple alphabetic characters
    Returns: user_guess {string} -- a single alphabetic character
    """
    print("Guess should only be a single, alphabetic character.")
    show_word_and_guesses(concealed_word, guess_list)
    user_guess = ask_for_input()
    return user_guess


def create_concealed_word_list(concealed_word):
    """
    Summary: Appends each character in concealed_word to a list
      concealed_word_list.
    Parameters: concealed_word {string}
    Returns: concealed_word_list {list}
    """
    concealed_word_list = []
    for ch in concealed_word:
        concealed_word_list.append(ch)
    return concealed_word_list


def create_concealed_word(secret_word):
    """
    Summary: Takes in secret_word and uses its length to create
      concealed_word, a string of the same length but comprised of
      dashes instead of letters.
    Parameters: secret_word {string}
    Returns: concealed_word {string}
    """
    word_length = len(secret_word)
    concealed_word = ""
    for i in range(word_length):
        ch = secret_word[i]
        concealed_word += "-"
    return concealed_word


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function selects a word from a list
    by reading a list of words from the file specified by the
    constant LEXICON_FILE.
    """
    word_list = []
    for line in open(LEXICON_FILE):
        line = line.strip()
        word_list.append(line)
    random_index = random.randint(0, len(word_list))
    secret_word = word_list[random_index]
    return secret_word


if __name__ == "__main__":
    main()
