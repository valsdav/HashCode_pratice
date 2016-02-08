from Block import Block

f = open('right_angle.commands','r')

matrix = {}
row = 40
col= 200
for i in range(row):
    matrix[i] = []
    for k in range(col):
        matrix[i].append(Block(i,k,False))

for l in f:
    t = l.split(' ')
    cmd = t[0]
    if cmd=='PAINT_LINE':
        r1 = int(t[1])
        c1 = int(t[2])
        r2 = int(t[3])
        c2 = int(t[4])
        if r1==r2:
            for j in range(c1, c2+1):
                matrix[r1][j].drawn= True
        if c1==c2:
            for j in range(r1, r2+1):
                matrix[j][c1].drawn = True
    if cmd =='PAINT_SQUARE':
        x = int(t[1])
        y = int(t[2])
        S = int(t[3])
        for i in range(-S,S+1):
            for k in range(-S,S+1):
                matrix[x+i][y+k].drawn=True
                
    
out =''
for i in range(row):
    for k in range(col):
        if matrix[i][k].drawn:
           out = out+'#'
        else: 
           out= out+'.'
    out = out+ '\n'
print out
    

