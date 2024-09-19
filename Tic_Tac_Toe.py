#This is the TIC TAC TOE game for a Contestant vs Computer.

print('''





         ╔═══╗   ╔═══╗   ╔═══╗       
           ║       ║     ║
           ║       ║     ║
           ║       ║     ║
           ║       ║     ║
           ║       ║     ║
                 ╚═══╝   ╚═══╝
                 ╔═══╗ ╔═══╗  ╔═══╗
                   ║   ║   ║  ║
                   ║   ║   ║  ║
                   ║   ║═══║  ║
                   ║   ║   ║  ║
                   ║   ║   ║  ╚═══╝
                              ╔═══╗ ╔═══╗  ╔═══╗
                                ║   ║   ║  ║
                                ║   ║   ║  ║
                                ║   ║═══║  ║═══
                                ║   ║   ║  ║
                                ║   ╚═══╝  ╚═══╝
                                     

''')




#importing module
import random


# Game Board Setup
tic_tac_toe_setup = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]



contestant_score = 0
computer_score = 0
# Defining function
def tic_tac_toe():
    global tic_tac_toe_setup, contestant_score, computer_score
    # Creates a text file_handle and writes the header for the data
    file_handle = open('data.txt', 'w')
    file_handle.write('Move Count' + '\t' + 'Comp(C)/Contestant(CO)' + '\t' + 'Row' + '\t\t' + 'columnumn' + '\t\t' + 'Piece(O/X)')
    file_handle.write('\n')
    file_handle.close()


    
    #Contestant-X & computer-O
    player = ["X", "O"]
    data = []

    
    # Turn
    move = 0
    move_count = 0
    draw = True

    
    # If NOT DRAW..
    while check_draw(tic_tac_toe_setup) != draw:
        display_board(tic_tac_toe_setup)

        #Defining the if condition
        if move == 0:
            print("\nYOUR TURN!")
            row, column = user_move(tic_tac_toe_setup)
            tic_tac_toe_setup[row][column] = player[move]
            move_count += 1
            data_info(data, move_count, player, move, row, column)

        #Defining the else condition    
        else:
            print("\nCOMPUTER'S TURN!")
            row, column = comp_move(tic_tac_toe_setup)
            tic_tac_toe_setup[row][column] = player[move]
            move_count += 1 
            data_info(data, move_count, player, move, row, column)


            
        # Winning conditon
        if win_check(tic_tac_toe_setup):
            display_board(tic_tac_toe_setup)
            # If Contestant wins, Contestant gains 1 point
            if move == 0:
                print('\nYOU HAVE WON THIS GAME!')
                print('You gained 1 point!!!')
                contestant_score += 1
                break
            #If Computer wins, computer gains 1 point
            else:
                print('\nCOMPUTER HAS WON, YOU LOST THIS GAME..!')
                print('Computer gained 1 point!!!')
                computer_score += 1
                break
        # User switch
        move = 1 - move
    # If tie..
    else:
        display_board(tic_tac_toe_setup)
        print('\nGAME OVER')
        print("It's a tie!")
# Displays title and instructions
def tic_tac_toe_start():
    # Displays title
    print("------------------------")
    print("---WELCOME TO THE GAME OF TIC TAC TOE   ---")
    print('YOU USE (X) V/S COMPUTER USES (O)')
    print("------------------------")
    # Displays instructions
    print('\nRULES TO PLAY THE GAME..')
    print('1. You make the first move')
    print('2. You must type in the row number')
    print('2. Then you must type in the column number')
    print('3. Then computer will make the next move')
    print('4. Game ends when 3 of the same piece are placed in a ROW, COLUMN or DIAGONAL\n')
# Displaying of game board
def display_board(tic_tac_toe_setup):
    # The index of each item will be used as the row and columnumn values
    print("\n     1     2    3 \n")
    print('1   ' + tic_tac_toe_setup[0][0] + '  |  ' + tic_tac_toe_setup[0][1] + '  |  ' + tic_tac_toe_setup[0][2])
    print('    ---+-----+---')
    print('2   ' + tic_tac_toe_setup[1][0] + '  |  ' + tic_tac_toe_setup[1][1] + '  |  ' + tic_tac_toe_setup[1][2])
    print('    ---+-----+---')
    print('3   ' + tic_tac_toe_setup[2][0] + '  |  ' + tic_tac_toe_setup[2][1] + '  |  ' + tic_tac_toe_setup[2][2])



    
def user_move(tic_tac_toe_setup):
    posibble_inputs = [1, 2, 3]
    while True:
        row = input("\nEnter row number: ")
        while not row.isdigit() or int(row) not in posibble_inputs:
            row = input("Enter row number between 1-3: ")
        row = int(row)
        column = input("Enter column number: ")
        while not column.isdigit() or int(column) not in posibble_inputs:
            column = input("Enter column number between 1-3: ")
        column = int(column)
        if tic_tac_toe_setup[row-1][column-1] != " ":
            print("Pick an empty box!")
        else:
            return (row-1, column-1)
            



def comp_move(tic_tac_toe_setup):
    
    possible_moves = []
    for row in range(len(tic_tac_toe_setup)):
        for column in range(len(tic_tac_toe_setup[0])):
            if tic_tac_toe_setup[row][column] == " ":
                possible_moves.append((row, column))
    return possible_moves[random.randrange(len(possible_moves))]


# Checks each row of game board
def check_row(tic_tac_toe_setup, row):
    if tic_tac_toe_setup[row][0] == tic_tac_toe_setup[row][1] and tic_tac_toe_setup[row][1] == tic_tac_toe_setup[row][2] and tic_tac_toe_setup[row][0] != " ":
        return True
    else:
        return False


# Checks each columnumn of game board
def check_columnumn(tic_tac_toe_setup, column):
    # Checks if each row has similar pieces
    if tic_tac_toe_setup[0][column] == tic_tac_toe_setup[1][column] and tic_tac_toe_setup[1][column] == tic_tac_toe_setup[2][column] and tic_tac_toe_setup[0][column] != " ":
        return True
    else:
        return False



# Checks each diagonal of game board
def check_diagonals(tic_tac_toe_setup):
    # Checks if each row has similar pieces
    if tic_tac_toe_setup[0][0] == tic_tac_toe_setup[1][1] and tic_tac_toe_setup[1][1] == tic_tac_toe_setup[2][2] and tic_tac_toe_setup[0][0] != " ":
        return True
    elif tic_tac_toe_setup[2][0] == tic_tac_toe_setup[1][1] and tic_tac_toe_setup[1][1] == tic_tac_toe_setup[0][2] and tic_tac_toe_setup[2][0] != " ":
        return True
    else:
        return False



# Checks if any player won
def win_check(tic_tac_toe_setup):
    # Iterates 3 times to be able to go through every columnumn and row
    for i in range(3):
        if check_row(tic_tac_toe_setup, i):
            return True
        if check_columnumn(tic_tac_toe_setup, i):
            return True
    if check_diagonals(tic_tac_toe_setup):
        return True
    else:
        return False



# Checks if the game board is full
def check_draw(tic_tac_toe_setup):
    # Iterates through every item in the board, check if empty space exists
    for item in tic_tac_toe_setup:
        if " " in item:
            return False
    return True



# Records/datas all moves of the game
def data_info(data, move_count, player, move, row, column):
    file_handle = open('data.txt', 'a')
    data = []
    
    
    data.append(str(move_count))
    if move == 0:
        data.append('CO')
    else:
        data.append('C')
    data.append(str(row+1))
    data.append(str(column+1))
    data.append(str(player[move]))
    for i in range(len(data)):
        entry_1 = data[i] + '                    '
        file_handle.write(entry_1)
    
    file_handle.write('\n')
    file_handle.close()


    
# Prints the scores for computer and user
def score_board():
    print("\n\n--------------------------------")
    print("            SCOREBOARD       ")
    print("--------------------------------")
    print('      Contestant : ' + str(contestant_score) + ' points')
    print('      Computer : ' + str(computer_score) + ' points')
    print("--------------------------------\n")






# Asks Contestant if want to play again
def play_again():
    global tic_tac_toe_setup, computer_score, contestant_score
    while True:
        play_again = input("\nWOULD YOU LIKE TO PLAY AGAIN? Type 'y' for Yes or 'n' for No: ").lower()
        if  play_again == "y":
            reset_score =  input("\nWOULD YOU LIKE O RESET THE SCORE? (y/n): ").lower()
            if reset_score == 'y':
                contestant_score = 0
                computer_score = 0
                tic_tac_toe_setup = [ [" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
                return True
            elif reset_score == "n":
                tic_tac_toe_setup = [ [" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
                return True
            else:
                continue 
            
        elif play_again == 'n':
            print("Thank you for playing the game.")
            exit()
        else:
            print("You have entered wrong input.")
            exit()


        
    
# Runs all the tic_tac_toe user-defined functions
while True:
    tic_tac_toe_start()
    start_game = input('WOULD YOU LIKE TO START THE GAME? "y" for yes or "n" for no : ').lower()
    # If Contestant choice is y
    while start_game == 'y':
        tic_tac_toe()
        score_board()
        if play_again():
            pass
        else:
            break
    # If Contestant choice is n, the program breaks tic_tac_toe and ends.
    if start_game == 'n':
        break
    elif start_game != 'n' and 'y':
        continue
    break
    
        
