from Block import Block


commands = []
num_rows = 0
num_cols = 0

def find_lines(matrix,num_row, num_col):
    global num_rows
    num_rows = num_row
    global num_cols
    num_cols = num_col
    for i in range(0,num_row):
        for j in range(0, num_col):
            block = matrix[i][j]
            #controlla anche se non e gia disegna
            if block.is_good():
                r = find_row(matrix, block)
                c = find_column(matrix, block)
                if r > c:
                    (i,j_min,j_max) = fill_row(matrix,block)
                    commands.append("PAINT_LINE {} {} {} {}".format(i,j_min,i, j_max))
                else:
                    (j,i_min,i_max) = fill_column(matrix, block)
                    commands.append("PAINT_LINE {} {} {} {}".format(i_min,j,i_max, j))
    return ('\n'.join(commands), len(commands))

def check_j(j):
    if j<= 0:
        return False
    if j == num_cols:
        return False
    return True

def check_i(i):
    if i<= 0:
        return False
    if i == num_rows:
        return False
    return True
                        
                        
def fill_row(matrix, block):
    block.fill()
    cell_right = 0
    cell_left = 0 
    i  = block.x
    j = block.y
    while True:
        if not check_j(j+1): 
            break
        bl = matrix[i][j+1]
        if bl.is_good_l():
            bl.fill()
            j += 1
        else:
            break
    j_max = j
    j = block.y
    while True:
        if not check_j(j-1): 
            break
        bl = matrix[i][j-1]
        if bl.is_good_l():
            bl.fill()
            j -= 1
        else:
            break
    j_min = j 
    return (i, j_min,j_max)
    
def fill_column(matrix,block):
    block.fill()
    cell_up = 0
    cell_down = 0 
    i  = block.x
    j = block.y
    while True:
        if not check_i(i+1): 
            break
        bl = matrix[i+1][j]
        if bl.is_good_l():
            bl.fill()
            i += 1
        else:
            break
    i_max = i
    i = block.x
    while True:
        if not check_i(i-1): 
            break
        bl = matrix[i-1][j]
        if bl.is_good_l():
            bl.fill()
            i -= 1
        else:
            break
    i_min = i 
    return (j, i_min,i_max)
                

def find_row(matrix, block):
    cell_right = 0
    cell_left = 0 
    i  = block.x
    j = block.y
    while True:
        if not check_j(j+1):
            break
        bl = matrix[i][j+1]
        if bl.is_good_l():
            cell_right +=1
            j += 1
        else:
            break
    j = block.y
    while True:
        if not check_j(j-1): 
            break
        bl = matrix[i][j-1]
        if bl.is_good_l():
            cell_left +=1
            j -= 1
        else:
            break
    return cell_right + cell_left + 1 
        
            
def find_column(matrix, block):
    cell_up = 0
    cell_down = 0 
    i  = block.x
    j = block.y
    while True:
        if not check_i(i+1): 
            break
        bl = matrix[i+1][j]
        if bl.is_good():
            cell_up +=1
            i += 1
        else:
            break
    i = block.x
    while True:
        if not check_i(i): 
            break
        bl = matrix[i-1][j-1]
        if bl.is_good():
            cell_down +=1
            i -= 1
        else:
            break
    return cell_up + cell_down +1 