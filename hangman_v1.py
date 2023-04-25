import random as r
import time
import sys
from termcolor import colored, cprint
from pyfiglet import Figlet
from os import system, name


def clear_screen():
    """ Clear the screen in depends of operation system (Windows, Linux or iOS). 
        It was copied from internet,  I will find out how it works in future (_=system is unknow for me) :)"""

    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


def start_screen():
    """ Show start screen. Use pyfigled and termcolor modules"""

    f = Figlet(font ="standard")
    print(colored(f.renderText("HANGMAN"), "green"))
    time.sleep(1)                                                   # Used time module for program delay
    f = Figlet(font ="digital")
    print(colored(f.renderText("       Don't get hunged"), "red"))
    time.sleep(2)


def get_letter():
    """ Get a letter from Player """

    user_letter = input(colored(" Enter the letter You are guessing: ", "yellow"))
    while (user_letter.isalpha()) != True or len(user_letter) !=1:                  # While loop checks if a letter is not a digits and it is only one
        sys.stdout.write("\033[F")                                                  # Clear to the end of line
        sys.stdout.write('\033[2K\033[1G')                                          # Erase and go to beginning of line
        print("\a")                                                                 # Plays sound from system buzzer
        # If a letter is not character form alphabet or it is not only one get it again
        user_letter = input(colored(" IT MUST BE ONE LETTER! Enter the letter You are guessing: ", "yellow")) 
    else:
        return user_letter.lower()


def get_word():
    """ Get a word from Player 2 """

    word = input(colored("Enter the word for the other player to guess: ", "yellow"))
    while not word.isalpha() or len(word) < 3:
        sys.stdout.write("\033[F")
        sys.stdout.write('\033[2K\033[1G')
        print("\a")
        word = input(colored(
            "Invalid input! The word should only contain letters and be at least 3 characters long. Try again: ",
            "yellow"))
    else:
        return word.lower()


def take_word(num_of_players):
    """ Takes a random word from the list and hides it """

    pair = []                                                    # Empty list to use it later
    words = ("dom", "kot", "las", "java", "auto", "lawa", "python", "karoca", "zabawa", "komputer", "wisielec", "latawiec")
    word = r.choice(words)  # Random word from the list
    pair.append(word)  # Add the word to the list 'pair'
    hidden_word = ["_" for i in word]        # List comprehension -> is beautiful !!!! -> change all characters with '_'
    # It was before list comprehension -> bleeee ;)
    # for i in range(len(word)):
    #      hidden_word = hidden_word.replace(hidden_word[i],"_")
    pair.append(hidden_word)  # Add the hidden_word to the list 'pair'
    return pair               # Function can return only one parameter, so it return the list 'pair'


def print_gallows_and_hangman(counter):
    """ Prints gallows and hangman in ASCI code """

    gallows = (
        """
           _____________
           |            |
           |
           |
           |
           |
           |
           |
           |
           |
         -----
      """
      ,
      """
           _____________
           |            |
           |            O
           |
           |
           |
           |
           |
           |
           |
         -----
      """
      ,
      """
           _____________
           |            |
           |            O
           |           -+- 
           |
           |
           |
           |
           |
           |
         -----
      """
      ,
      """
           _____________
           |            |
           |            O
           |           -+- 
           |          /   
           |          |
           |
           |
           |
           |
         -----
      """
      ,
      """
           _____________
           |            |
           |            O
           |           -+- 
           |          /   \ 
           |          |   |     
           |             
           |
           |
           |
         -----
      """
      ,
      """
           _____________
           |            |
           |            O
           |           -+- 
           |          / | \ 
           |          | | |
           |            |
           |           
           |
           |
         -----
      """
      ,
      """
           _____________
           |            |
           |            O
           |           -+- 
           |          / | \ 
           |          | | |
           |            |
           |           |
           |           |
           |           
         -----
      """
      ,
      """
           _____________
           |            |
           |            O
           |           -+- 
           |          / | \ 
           |          | | |
           |            |
           |           | |
           |           | |
           |           
         -----
      """
      ,
      )
    print(colored(gallows[counter], "magenta"))


def hanged(counter):
    """This is not a happy end, the game is over and Player is dead """

    dangle = (
      """
           _____________
           |            |
           |            O
           |           -+- 
           |          / | \ 
           |          | | |
           |            |
           |           | |
           |           | |
           |           
         -----
      """
      ,
      """
           _____________
           |            /
           |           O
           |         -+- 
           |       / / \ 
           |      / /   |
           |       /    
           |     / /
           |    / /
           |           
         -----
      """
      ,
      """
           _____________
           |            |
           |            O
           |           -+- 
           |          / | \ 
           |          | | |
           |            |
           |           | |
           |           | |
           |           
         -----
      """
      ,
      """
           _____________
           |            \\
           |             O
           |             -+- 
           |            / \ \ 
           |           |   \ \\
           |                \\
           |                \ \\
           |                 \ \\
           |           
         -----
      """
      ,
      """
           _____________
           |            |
           |            O
           |         \ -+- /
           |          \ | / 
           |            | 
           |            |
           |          |\ /|
           |          |   |
           |           
         -----
      """
    )
    print(colored(dangle[counter], "magenta"))


def live(counter):
    """The Player is  alive and can play again :))) """

    happy = (
      """
   
                 O
                -+- 
               / | \ 
               | | |
                 |
                | |
                | |
 
      """
      ,
      """
                 O
              \ -+- /
               \ | / 
                 | 
                 |
               |\ /|
               |   |
   

      """
    )
    print(colored(happy[counter], "magenta"))


def get_player_names():
    """Get player names from users"""

    player1_name = input(colored("Enter the name of the first player: ", "yellow"))
    player2_name = input(colored("Enter the name of the second player: ", "yellow"))

    return player1_name, player2_name

def get_word(player_name):
    """Get word from player"""

    return input(colored(f"{player_name}, enter a word to guess: ", "yellow"))


def goodbye():
    """Shows goodbye screen"""

    clear_screen()
    start_screen()
    f = Figlet(font ="standard")
    print(colored(f.renderText('GOODBYE'), "magenta"))
    time.sleep(3)
    return


def end_game(wrong_answer):
    """The function shows the end screen and allows to choose whether the Player will play again or not """
    
    if wrong_answer == 7:
        for i in range(10):
            for i in range (0,5):
                clear_screen()
                f = Figlet(font ="standard")
                print(colored(f.renderText("HANGMAN"), "green"))
                f = Figlet(font ="digital")
                print(colored(f.renderText("     YOU HAVE LOST"), "red"))
                print(colored(f.renderText("     AND YOU DANGLE"), "red"))
                hanged(i)                                                   
                time.sleep(0.15)
    else:
        for i in range(10):
            for i in range (0,2):
                clear_screen()
                f = Figlet(font ="standard")
                print(colored(f.renderText("HANGMAN"), "green"))
                print(colored(f.renderText("     YOU ARE"), "red"))
                print(colored(f.renderText("STILL ALIVE"), "red"))
                live(i)                                                     
                print(colored(f.renderText("GERONIMO !"), "blue"))
                time.sleep(0.15)
    time.sleep(2)
    clear_screen()
    answer = ''
    # print(answer)
    while answer.lower != "n" or answer.lower() != "y":
        clear_screen()
        start_screen()
        answer = input(colored("       Do You want play again [Y]es/[N]o ? ", "green"))
        if answer.lower() == "n":
            goodbye()
            return

        elif answer.lower() == "y":
            main_game()


# def num_of_players_screen():
#     """Shows screen with question about numer of players"""
#
#     clear_screen()
#     start_screen()
#     f = Figlet(font ="digital")
#     print(colored(f.renderText('Choose number of players:'), "magenta"))
#     print(colored(f.renderText('1. Player'), "green"))
#     print(colored(f.renderText('2. Players'), "green"))
#     time.sleep(3)
#     return
#
#
def game_board(choosen_letters, hidden_word, wrong_answer, player_names):
    """ Function shows the game board with all necessary elements """

    clear_screen()
    f = Figlet(font ="standard")
    print(colored(f.renderText("HANGMAN"), "green"))
    f = Figlet(font ="digital")
    if player_names is None:
        print(colored(f.renderText("       Don't get hunged"), "red"))
    else:
        print(colored(f.renderText(f"       {player_names[1]}, guess the word"), "red"))
    print (colored(f.renderText(hidden_word), "yellow"))
    print_gallows_and_hangman(wrong_answer)
    print(" The letters You have already selected: ", choosen_letters[:])


def main_game():
    clear_screen()    
    start_screen()
    player_names = None
    player_mode = input(colored("Choose the game mode: [1] - one player, [2] - two players: ", "yellow"))
    if player_mode == "2":
        player_names = get_player_names()

    taken_word = []
    if player_names is not None:
        taken_word.append(get_word(player_names[0]).lower())
    else:
        words = ("dom", "kot", "las", "java", "auto", "lawa", "python", "karoca", "zabawa", "komputer", "wisielec", "latawiec")
        taken_word.append(r.choice(words))
    drawn_word = list(taken_word[0])
    hidden_word = ["_" for i in drawn_word]
    choosen_letters = []
    wrong_answer = 0

    # The while loop works as long as the hidden word differs from the drawn word and as long as the number of invalid letters is below 7.
    while wrong_answer != 7 and hidden_word != drawn_word:          
            
        game_board(choosen_letters,hidden_word,wrong_answer, player_names)
        letter = get_letter()
        choosen_letters.append(letter)

        if letter not in drawn_word:
            wrong_answer += 1
            print("\a")
        else:
            for i in range(len(drawn_word)):
                if letter == drawn_word[i]:
                    hidden_word[i] = letter
                
        game_board(choosen_letters, hidden_word, wrong_answer, player_names)
    time.sleep(2)
    end_game(wrong_answer)


main_game()
time.sleep(2)
