import os, platform

def draw_board(board):
    print(board[5][0],"|",board[5][1],"|",board[5][2],"|",board[5][3],"|",board[5][4],"|",board[5][5],"|",board[5][6])
    print("--------------------------")
    print(board[4][0],"|",board[4][1],"|",board[4][2],"|",board[4][3],"|",board[4][4],"|",board[4][5],"|",board[4][6])
    print("--------------------------")
    print(board[3][0],"|",board[3][1],"|",board[3][2],"|",board[3][3],"|",board[3][4],"|",board[3][5],"|",board[3][6])
    print("--------------------------")
    print(board[2][0],"|",board[2][1],"|",board[2][2],"|",board[2][3],"|",board[2][4],"|",board[2][5],"|",board[2][6])
    print("--------------------------")
    print(board[1][0],"|",board[1][1],"|",board[1][2],"|",board[1][3],"|",board[1][4],"|",board[1][5],"|",board[1][6])
    print("--------------------------")
    print(board[0][0],"|",board[0][1],"|",board[0][2],"|",board[0][3],"|",board[0][4],"|",board[0][5],"|",board[0][6])

def newboard(board):
  for i in range(0,6): #for loop that goes through all of that checks all of the columns in the board 
    for j in range(0,5): #for loop that goes through all of that checks all of the rows in the board 
      board[i][j] = 0 #resets all of the values bak to 0, therefore clearing the board
  return board #returns the new board with all of the values at 0

def player1_turn(board):
    row=0;
    while (True): #while statement that executes player 1's turn 
        row=0 
        choice=int(input("Player 1, enter (0-6):")) #asks player one to enter a number form (0-6)
            
        if (choice>=0 and choice<=6): 
            for row in range(0,6):
                
                if (board[row][choice]==0):
                    
                    board[row][choice]=1  #if the value of the slot is 0 it chnges the value to 1 since it is player 1's turn
                    return
                    
                    
                
            print("The row is full!")
            
        else:
            print("This is not the proper input") #else condition, if the user enters a number that is not within the rows index (0-6), this will be printed
            


def player2_turn(board):
    row=0;
    while (True):
        row=0
        choice=int(input("Player 2, enter (0-6):"))
            
        if (choice>=0 and choice<=6):
            for row in range(0,6):
                
                if (board[row][choice]==0):
                    
                    board[row][choice]=1  #if the value of the slot is 0 it chnges the value to 2 since it is player 2's turn
                    board[row][choice]=2 
                    return
                    
                    
                
            print("The row is full!") #if all of the values in the column are changed, this will be printed
            
        else:
            print("This is not the proper input") #else condition, if the user enters a number that is not within the rows index (0-6), this will be printed
   


def clear(): #cleaning output. (taken from https://stackoverflowcom/questions/37071230/clear-overwrite-standard-output-in-python)
   if platform.system() == ("Windows"):
      os.system('cls')
   else:
      os.system('clear')



def check_winning(board):
#if 4 pieces are connected together, return True.     

    #horizontal
    for row in range(0,6): #for loop the rows in the list index, therefore 0 is technically 1
      
      for column in range(0,4):
        if (board[row][column]==board[row][column+1] and board[row][column]==board[row][column+2] and board[row][column]==board[row][column+3] and board[row][column]!=0): #column + number checks the next column over.
          return True

  #vertical
    for row in range (0,3): 
 #In the index this is the highest row your match of 4 can start from
      for column in range(0,7):

        if (board[row][column]==board[row+1][column] and board[row][column]==board[row+2][column] and board[row][column]==board[row+3][column] and board[row][column]!=0): #row + number checks the row on top to see if there is a piece there.
          return True


    for row in range (0,3): 
      
      for column in range (0,4):
        if (board[row][column]==board[row+1][column+1] and board[row][column]==board[row+2][column+2] and board[row][column]==board[row+3][column+3] and board[row][column]!=0): #row + number and column + number checks the next row and next column over
          return True


#diagonal facing right
    for row in range (3,6):
     #It stars checking from row index 3 (the 4th row ---> 0,1,2,3) because that is the lowest that any of the players can win from. 
      
      for column in range (0,4):
      #checks diagonals that are facing right. 
        if (board[row][column]==board[row-1][column+1] and board[row][column]==board[row-2][column+2] and board[row][column]==board[row-3][column+3] and board[row][column]!=0): #checks the next column over and the row below, column + number checks the next column over in the index, and row - number checks the row below.
          return True