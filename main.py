import numpy as np
import copy

def is_valid(board, row, col, num):
    # Verificar se o número já está presente na linha
    if num in board[row, :]:
        return False

    # Verificar se o número já está presente na coluna
    if num in board[:, col]:
        return False

    # Verificar se o número já está presente no bloco 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    if num in board[start_row:start_row + 3, start_col:start_col + 3]:
        return False
    
    return True
    
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row,col] == 0: #verificar célula vazia
                for num in range(1,10): #Tentar números de 1 a 9
                    if is_valid(board,row,col,num):
                        board[row,col] = num #Preencher a célula
                        if solve_sudoku(board): #chamada recursiva
                            return True
                        else:
                            board[row,col] = 0 #Retroceder se a solução não for encontrada
                return False
    return True

sudoku_board = np.array([
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
])

solve_sudoku(sudoku_board)
print(sudoku_board)