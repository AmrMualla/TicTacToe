#Amr Mualla, Tic Tac Toe, (text based version)
#The code is not meant to be optimal, it was simply practice with conditional statements, aswell dictionary use.

def TicTacToe():
    print("Welcome to Amr's two player Tic Tac Toe game.")


    d = {"row1_1": "☐", "row1_2": "☐", "row1_3": "☐", "row2_1": "☐", "row2_2": "☐", "row2_3":"☐", "row3_1":"☐", "row3_2":"☐", "row3_3":"☐"}
    diagram = f"{d['row1_1']} |{d['row1_2']} |{d['row1_3']}  \n--------\n{d['row2_1']} |{d['row2_2']} |{d['row2_3']} \n--------\n{d['row3_1']} |{d['row3_2']} |{d['row3_3']} "
    player_one_win = "★ Player One (X) has won the game! Good game. ★"
    player_two_win = "✪ Player Two (O) has won the game! Good game. ✪"


    game_on = True
    turn = True
    spotstaken = []
    while game_on:
        if d["row1_1"] == "X" and d["row1_2"] == "X" and d["row1_3"] == "X":
            print(player_one_win)
            game_on = False
        elif d["row2_1"] == "X" and d["row2_2"] == "X" and d["row2_3"] == "X":
            print(player_one_win)
            game_on = False
        elif d["row3_1"] == "X" and d["row3_2"] == "X" and d["row3_3"] == "X":
            print(player_one_win)
            game_on = False
        elif d["row1_1"] == "X" and d["row2_1"] == "X" and d["row3_1"] == "X":
            print(player_one_win)
            game_on = False
        elif d["row1_2"] == "X" and d["row2_2"] == "X" and d["row3_2"] == "X":
            print(player_one_win)
            game_on = False
        elif d["row1_3"] == "X" and d["row2_3"] == "X" and d["row3_3"] == "X":
            print(player_one_win)
            game_on = False
        elif d["row1_1"] == "X" and d["row2_2"] == "X" and d["row3_3"] == "X":
            print(player_one_win)
            game_on = False
        elif d["row1_3"] == "X" and d["row2_2"] == "X" and d["row3_1"] == "X":
            print(player_one_win)
            game_on = False
        elif d["row1_1"] == "O" and d["row1_2"] == "O" and d["row1_3"] == "O":
            print(player_two_win)
            game_on = False
        elif d["row2_1"] == "O" and d["row2_2"] == "O" and d["row2_3"] == "O":
            print(player_two_win)
            game_on = False
        elif d["row3_1"] == "O" and d["row3_2"] == "O" and d["row3_3"] == "O":
            print(player_two_win)
            game_on = False
        elif d["row1_1"] == "O" and d["row2_1"] == "O" and d["row3_1"] == "O":
            print(player_two_win)
            game_on = False
        elif d["row1_2"] == "O" and d["row2_2"] == "O" and d["row3_2"] == "O":
            print(player_two_win)
            game_on = False
        elif d["row1_3"] == "O" and d["row2_3"] == "O" and d["row3_3"] == "O":
            print(player_two_win)
            game_on = False
        elif d["row1_1"] == "O" and d["row2_2"] == "O" and d["row3_3"] == "O":
            print(player_two_win)
            game_on = False
        elif d["row1_3"] == "O" and d["row2_2"] == "O" and d["row3_1"] == "O":
            print(player_two_win)
            game_on = False
        elif len(spotstaken) >= 8:
            print("Tie game")
            game_on = False
    

        elif turn == True:
            choice = input("Player one (X), What location do you choose? ex: row1_1")
            if choice not in spotstaken:
                d[choice] = "X"
                diagram = f"{d['row1_1']} |{d['row1_2']} |{d['row1_3']}  \n--------\n{d['row2_1']} |{d['row2_2']} |{d['row2_3']} \n--------\n{d['row3_1']} |{d['row3_2']} |{d['row3_3']} "
                print(diagram)
                spotstaken.append(choice)
                turn = False
            else:
                print("Sorry, that spot is either unavailable or artificial. Pick another spot that you see is available, example input: row1_1. This is your last attempt.")
                choice = input("What location do you now choose? ex: row1_1")
            if choice not in spotstaken:
                d[choice] = "X"
                diagram = f"{d['row1_1']} |{d['row1_2']} |{d['row1_3']}  \n--------\n{d['row2_1']} |{d['row2_2']} |{d['row2_3']} \n--------\n{d['row3_1']} |{d['row3_2']} |{d['row3_3']} "
                print(diagram)
                spotstaken.append(choice)
                turn = False
        
        elif turn == False:
            choice = input("Player two (O), What location do you choose? ex: row1_1")
            if choice not in spotstaken:
                d[choice] = "O"
                diagram = f"{d['row1_1']} |{d['row1_2']} |{d['row1_3']}  \n--------\n{d['row2_1']} |{d['row2_2']} |{d['row2_3']} \n--------\n{d['row3_1']} |{d['row3_2']} |{d['row3_3']} "
                print(diagram)
                spotstaken.append(choice)
                turn = True
            else:
                print("Sorry, that spot is either unavailable or artificial. Pick another spot that you see is available, example input: row1_1. This is your last attempt.")
                choice = input("What location do you now choose? ex: row1_1")
            if choice not in spotstaken:
                d[choice] = "O"
                diagram = f"{d['row1_1']} |{d['row1_2']} |{d['row1_3']}  \n--------\n{d['row2_1']} |{d['row2_2']} |{d['row2_3']} \n--------\n{d['row3_1']} |{d['row3_2']} |{d['row3_3']} "
                print(diagram)
                spotstaken.append(choice)
                turn = True

TicTacToe()
again = input("Would you like to play again? Type Y for Yes and N for no")
if again == "Y":
    TicTacToe()
else:
    exit()

        
