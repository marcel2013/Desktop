import sys
import random


def quess_number(name= 'PlayerOne'):
    game_count = 0
    player_wins = 0
    
    def play_quess_number():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(
            f"\n{name}, quess wich number I'm thinking of ....1, 2, or 3.\n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3")
            return play_quess_number()
        
        computerchoice = random.choice("123")

        print(f"\n{name}, you chose {playerchoice}.")
        print(f"I was thinking about the number {computerchoice}.\n")

        player = int(playerchoice)

        computer = int(computerchoice)

        def decide_winer(player, computer):
            nonlocal name
            nonlocal player_wins
            
            if player == computer :
                player_wins += 1
                return f"🎉 🎉 {name}, you win!"
            else:
                return f"🐍 Sorry, {name}. Better luck next time..😢😢"
            


        game_result = decide_winer(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count:  {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")
        

        print(f"\nPlay again, {name}?")


        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in  ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_quess_number()
        else:
            print("\n🎉🙌🎉🙌🥂")
            print("Thank you for playng!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 🙋‍♂️")
            else:
                return

    return play_quess_number

if __name__ =="__main__":
    import argparse


    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", '--name', metavar='name', 
        required=True, help="The name of the person playng the game."
    )

    args = parser.parse_args()

    quess_my_number = quess_number(args.name)
    quess_my_number()

            




    