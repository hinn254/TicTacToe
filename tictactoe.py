'''
# BennyWorld
Tic Tac Toe
 |X|0|0|
 |0|X|0|
 |0|0|X|

WIN - LOSS - DRAW
TWO PLAYER - TURNS
Take turns
'''

# Dict
my_board = {
    "One": "",
    "Two": "",
    "Three": "",
    "Four": "",
    "Five": "",
    "Six": "",
    "Seven": "",
    "Eight": "",
    "Nine": "",
}


def board():
    print(f'| {my_board["One"]} | {my_board["Two"]} | {my_board["Three"]} |')
    print('-  -  -')
    print(f'| {my_board["Four"]} | {my_board["Five"]} | {my_board["Six"]} |')
    print('-  -  -')

    print(
        f'| {my_board["Seven"]} | {my_board["Eight"]} | {my_board["Nine"]} |')


counter = 10


def selectedOption():
    player1 = input("Do you want X or O").upper()
    # while player1 != "X" or "O":
    #     player1 = input("Do you want X or O").upper()

    if player1 == "O":
        player2 = "X"
        print("Player 1 is O and Player 2 is X")
    else:
        player2 = "O"
        print("Player 1 is X and Player 2 is O")

    return player1


def checkWinnerDraw():
    if my_board["One"] == my_board["Two"] == my_board["Three"] != "":
        print("Won")
        return True
    if my_board["Four"] == my_board["Five"] == my_board["Six"] != "":
        print("Won")
        return True
    if my_board["Seven"] == my_board["Eight"] == my_board["Nine"] != "":
        print("Won")
        return True
    # Diagonals
    if my_board["One"] == my_board["Five"] == my_board["Nine"] != "":
        print("Won")
        return True
    if my_board["Three"] == my_board["Five"] == my_board["Seven"] != "":
        print("Won")
        return True
    # vertical
    if my_board["One"] == my_board["Four"] == my_board["Seven"] != "":
        print("Won")
        return True
    if my_board["Two"] == my_board["Five"] == my_board["Eight"] != "":
        print("Won")
        return True
    if my_board["Three"] == my_board["Six"] == my_board["Nine"] != "":
        print("Won")
        return True


def selection():
    i = 1
    val = selectedOption()  # X- O
    while i < counter:
        my_chosen_index = int(
            input("Where do you want to place your item"))

        if my_chosen_index == 1:
            my_board["One"] = val
        if my_chosen_index == 2:
            my_board["Two"] = val
        if my_chosen_index == 3:
            my_board["Three"] = val
        if my_chosen_index == 4:
            my_board["Four"] = val
        if my_chosen_index == 5:
            my_board["Five"] = val
        if my_chosen_index == 6:
            my_board["Six"] = val
        if my_chosen_index == 7:
            my_board["Seven"] = val
        if my_chosen_index == 8:
            my_board["Eight"] = val
        if my_chosen_index == 9:
            my_board["Nine"] = val
        board()

        win = checkWinnerDraw()
        if win:
            print(f"{val} has won!!!")
            break
        i += 1
        # X - player1
        if val == "X":
            val = "O"
        else:
            val = "X"
        print(f"You have {counter - i} trials left")

        print("It is the other players turn")
        if i == 9:
            print("IT'S A DRAW...")


board()
selection()
