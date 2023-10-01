import tkinter
import subprocess
import sys
from quess_number import quess_number
from rps import rps 




def play_game(name='PlayerOne'):
    welcome_back = True

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the arcade menu.")

            playerchoice = input(
                "\nPlease choose a game:\n1 = Rock Paper Scisors\n2 = Guess my number\n\nOr press \"x\" to exit the Arcade\n\n"
            )

        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}. please enter 1, 2, or x.")
            return play_game(name)
            
        welcome_back = True

        if playerchoice == "1":
            rock_papers_scissors =  rps(name)
            rock_papers_scissors()
        elif playerchoice == "2":
            quess_my_number = quess_number (name)
            quess_my_number()
        else:
            print(f"\nSee you next time!\n")
            sys.exit(f"Bye {name}! 🙋‍♂️🙋‍♂️🙋‍♂️")

if __name__ =="__main__":
    import argparse
    parser = argparse.ArgumentParser(
            description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", 
        required=True, help="The name of the person playng the game."
    )

    args = parser.parse_args()    

    print(f"\n{args.name}, welcome to the Arcade! 😎😎😎")  

    play_game(args.name)
        




