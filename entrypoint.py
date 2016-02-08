#hash code
from Block import Block
import squaretor, lineator
import sys


file_to_parse = sys.argv[1]
f = open('{}.in'.format(file_to_parse),'r')
filecontent = f.read()
f.close()
rows=filecontent.split('\n')

first_row=rows[0].split(' ')
row_count=int(first_row[0])
col_count=int(first_row[1])
print "Dimensione: {} x {}".format(row_count , col_count)

inputdata={}

for row in range(1,row_count+1):
    inputdata[row-1] = []
    for col in range(0,col_count):
        b = Block(row-1,col,rows[row][col]=='#')
        inputdata[row-1].append(b)

for i in range(0,row_count):
    for k in range(0,col_count):
        if inputdata[i][k].drawn:
            
            print '#',
        else:
            print '.',
    print

commands,num1 = squaretor.find_squares(inputdata, row_count, col_count)
#print(commands)


commands2,num2 = lineator.find_lines(inputdata, row_count, col_count)
#print(commands2)

print('after process')
for i in range(0,row_count):
    for k in range(0,col_count):
        if inputdata[i][k].filled:                
            print 'X',
        else:
            print '.',
    print

output="{} {}\n".format(row_count,col_count)
for i in range(0,row_count):
    for k in range(0,col_count):
        if inputdata[i][k].filled:
            output='{}#'.format(output)
            #print '#',
        elif inputdata[i][k].drawn:
            output='0#'.format(output)
            #print '0',
        else:
            output='{}.'.format(output)
            #print '.',

    output='{}\n'.format(output)
    #print

out = open('{}.out'.format(file_to_parse),'w')
out.write(output)
out.close()


outcmd = open('{}.commands'.format(file_to_parse),'w')
outcmd.write(str(num1+num2)+"\n")
outcmd.write(commands+"\n")
outcmd.write(commands2)
outcmd.close()

print('NUMERO TOTALE COMANDI '+ str(num1+num2))
