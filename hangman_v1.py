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

def take_word():
    """ Takes a random word from the list and hides it """

    pair =[]                                                    # Empty list to use it later
    words = ("dom", "kot", "las", "java", "auto", "lawa", "python", "karoca", "zabawa", "komputer", "wisielec", "latawiec")
    word = r.choice(words)  # Random word from the list
    pair.append(word)       # Add the word to the list 'pair'
    hidden_word = ["_" for i in word]                       # List comprehension -> is beautiful !!!! -> change all characters with '_'
    # It was before list comprehension -> bleeee ;)
    # for i in range(len(word)):
    #      hidden_word = hidden_word.replace(hidden_word[i],"_")
    pair.append(hidden_word)  # Add the hidden_word to the list 'pair'
    return pair               # Function can return only one parametr, so it return the list 'pair'
    
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


def number_of_players():
    pass


def game_board(choosen_letters, hidden_word, wrong_answer):
    """ Function shows the game board with all necessary elements """

    clear_screen()
    f = Figlet(font ="standard")
    print(colored(f.renderText("HANGMAN"), "green"))
    f = Figlet(font ="digital")
    print(colored(f.renderText("       Don't get hunged"), "red"))
    f = Figlet(font ="standard")
    print (colored(f.renderText(hidden_word), "yellow"))  
    print_gallows_and_hangman(wrong_answer)
    print(" The letters You have already selected: ", choosen_letters[:])
    
def main_game():
    clear_screen()    
    start_screen()
    taken_word = take_word()
    drawn_word = list(taken_word[0])
    hidden_word = taken_word[1]
    choosen_letters = []
    wrong_answer = 0

    # The while loop works as long as the hidden word differs from the drawn word and as long as the number of invalid letters is below 7.
    while wrong_answer != 7 and hidden_word != drawn_word:          
            
        game_board(choosen_letters,hidden_word,wrong_answer)
        letter = get_letter()
        choosen_letters.append(letter)

        if letter not in drawn_word:
            wrong_answer += 1
            print("\a")
        else:
            for i in range (len(drawn_word)):
                if letter == drawn_word[i]:
                    hidden_word[i] = letter
                
        game_board(choosen_letters, hidden_word, wrong_answer)
    time.sleep(2)
    end_game(wrong_answer)


main_game()
time.sleep(2)
