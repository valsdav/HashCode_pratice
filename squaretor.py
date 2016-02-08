
from Block import Block


commands = []

def find_squares(matrix, num_rows, num_col):
    s_max = find_max_s(matrix, num_rows, num_col)
    for S in range(s_max,0,-1):
        find_square(matrix, num_rows,num_col,S)
    return ('\n'.join(commands), len(commands))

def find_square(matrix, num_rows, num_col, S):
    for i in range(S, num_rows-S):
        for j in range(S, num_col-S):
            block = matrix[i][j]
            if block.is_good():
                if is_square(matrix, block, S):
                    paint(matrix, block,S)
                    commands.append("PAINT_SQUARE {} {} {}".format(block.x, block.y, S))

def is_square(matrix, block, S):
    ok = True 
    for i in range(-S,S+1):
        for j in range(-S,S+1):
            if ok:
                bl_tocheck = matrix[block.x+ i][ block.y + j]
                ok = ok and bl_tocheck.is_good_l()
            else:
                return False
    return ok

def paint(matrix,block, S):
    for i in range(-S,S+1):
        for j in range(-S,S+1):
            bl = matrix[block.x+ i][ block.y + j]
            bl.fill()


def find_max_s(matrix, num_rows, num_col):
    s = 0
    if (min(num_rows,num_col) % 2 == 0):
        s = min(num_rows,num_col)/2
    else:
        s = (min(num_rows,num_col) - 1) / 2
    return s
