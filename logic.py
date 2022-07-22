import random

def start_game():
    
    matrix = [[0 for i in range(4)] for j in range(4)]
    return matrix

def add_new_2(matrix):
    
    row = random.randint(0,3)
    col = random.randint(0,3)
    while(matrix[row][col] != 0):
        row = random.randint(0,3)
        col = random.randint(0,3)
    matrix[row][col] = 2
    
def get_current_state(matrix):
    
    # checking if 2048 is formed or not
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 2048:
                return 'GAME WON'
    
    # checking if 0 is present anywhere 
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return 'GAME NOT OVER'
    
    # checking if same numbers are there in board except the last row and last col
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == matrix[i+1][j] or matrix[i][j] == matrix[i][j+1]:
                return 'GAME NOT OVER'
    
    #checking last row
    for j in range(3):
        if matrix[3][j] == matrix[3][j+1]:
            return 'GAME NOT OVER'
    
    #checking last column
    for i in range(3):
        if matrix[i][3] == matrix[i+1][3]:
            return 'GAME NOT OVER'
    return 'GAME LOST'
    

def compress(matrix):
    # for left move
    changed = False
    new_matrix = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if matrix[i][j] != 0:
                new_matrix[i][pos] = matrix[i][j]
                if j != pos:
                    changed = True
                pos += 1
                
    return new_matrix,changed
    
def merge(matrix):
    # for left move
    changed = False
    for i in range(4):
        for j in range(3):
            if matrix[i][j] == matrix[i][j+1] and matrix[i][j] != 0:
                matrix[i][j] = 2*matrix[i][j]
                matrix[i][j+1] = 0
                changed = True
    return matrix, changed

def reverse(matrix):
    new_matrix = []
    for i in range(4):
        new_matrix.append([])
        for j in range(4):
            new_matrix[i].append(matrix[i][3-j])
    
    return new_matrix

def transpose(matrix):
    new_matrix = []
    for i in range(4):
        new_matrix.append([])
        for j in range(4):
            new_matrix[i].append(matrix[j][i])
            
    return new_matrix

def move_left(grid):
    
    new_grid,change1 = compress(grid)
    new_grid,change2 = merge(new_grid)
    new_grid,temp  = compress(new_grid)
    changed = change1 or change2
    
    return new_grid, changed
    
def move_right(grid):
    
    new_grid = reverse(grid)
    new_grid,changed = move_left(new_grid)
    new_grid = reverse(new_grid)
    
    return new_grid,changed

def move_up(grid):
    
    new_grid = transpose(grid)
    new_grid,changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    
    return new_grid,changed

def move_down(grid):
    
    new_grid = transpose(grid)
    new_grid,changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    
    return new_grid,changed

