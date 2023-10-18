from connect4_functions import *

count = 0  #variable that decides who's turn it is

board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

while (True):
    while (True):
        draw_board(board) #runs the draw board function and creates the board

        if (count % 2 == 0):  #if condition that checks whos turn it is, if count is even this means it is player ones turn
            player1_turn(board)
            clear()  #stops the program from printing a new table after every turn

        else:  #else condition, if count is odd it is player 2's turn
            player2_turn(board)
            clear()

        count += 1  #after a player does their turn it adds 1 to the count variable. If the count is odd it is player 2's turn and if it is even it player ones turn

        if (count == 42):  #if condition, if the variable count is equal to 42, this means that all the slots on the board are filled
            draw_board(board)  #keeps the board printed with all of the slots filled.
            print("Draw!")  #prints "Draw!", meaning there is no winner.
            break  #exits the nested while loop
        
        
        if check_winning(board): #runs the check_winning function
            if count % 2 == 0: 
                draw_board(board)  #keeps the final board printed
                print("Player 2 wins! ")
                break  #exits the nested while loop
            else:
                draw_board(board) #keeps the board printed with the final 4 match
                print("Player 1 wins! ") #if odd player one wins
                break  #exits the nested while loop

    choice = input("One more game? Press 1 for yes and other key to exit: ")  #Asks players if they want to play another game (if one is entered --> yes if any other key is entered ---> no)

    if (choice == "1"):  #if condition. If users enter 1, when asked if they want to play another game, the prograpm check this if condition and runs another game
        count = 0  #resets turn to player 1
        board = newboard(board)  #prints a new table that is cleared
        clear()  #removes the old table

    else:
        break
#else condition, if the players enter a different key (not 1), this means that they don't want to play another one and it exits the while loop.

print ("Thanks for playing the game! ")  #After the players are done playing and exit the while loop, this is what will be printed.
