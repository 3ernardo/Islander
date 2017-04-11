from random import randint

# Definition of the Height and Width of the matrix;
w, h = 10, 8

matrix = [[randint(0, 1) for x in range(w)] for y in range(h)]
islands = []

### Printing the matrix and the top/left coordinates
print ('==================\n'
       ' MAPA\n'
       '==================\n')

x, y = 65, 65

print(end='  ')
for n in range (w):
    print (chr(x), end=' ')
    x += 1
print ()

for n in range (h):
    print(chr(y), end=' ')
    y += 1
    for m in range (w):
        print (matrix[n][m], end=' '),
    print ()

### Testing for ones and printing it's coordinates
print ('\n'
       '==================\n'
       ' COORDENADAS\n'
       '==================\n')

iCounter, iReference = 0, 0

for iHCoord in range (h):
    for iWCoord in range (w):
        if matrix[iHCoord][iWCoord] == 1:
            print ('Coordenadas: h %s w %s' %(chr(iHCoord+65), chr(iWCoord+65)))
            iCounter += 1
            islands.append([iCounter, iHCoord, iWCoord, iReference])

### Testing for neighbours and printing
print ('\n'
       '==================\n'
       ' VIZINHOS\n'
       '==================\n')

for n in range (iCounter):
    print('Quadrante de terra %s:' %(islands[n][0]))
    for m in range (iCounter):
        #fatherless = 0
        #print ('compara %s com %s' %(islands[n], islands[m]))
        if islands[n][1] == islands[m][1] and islands[n][2]-1 == islands[m][2]:
            print ('- tem vizinho a esquerda')
            if islands[n][3] == 0:
                islands[n][3] = islands[m][3]
        #else:
        #    fatherless = 1
        if islands[n][1] == islands[m][1] and islands[n][2]+1 == islands[m][2]:
            print ('- tem vizinho a direita')
            if islands[m][3] == 0:
                islands[m][3] = islands[n][3]
        if islands[n][2] == islands[m][2] and islands[n][1]-1 == islands[m][1]:
            print ('- tem vizinho a cima')
        #    fatherless = 0
            if islands[n][3] == 0:
                islands[n][3] = islands[m][3]
        #else:
        #    fatherless = 1
        if islands[n][2] == islands[m][2] and islands[n][1]+1 == islands[m][1]:
            print ('- tem vizinho a baixo')
            if islands[m][3] == 0:
                islands[m][3] = islands[n][3]
        #if fatherless == 1:
        #    iReference += 1
        #    islands[n][3] = iReference

### Finding islands
print ('\n'
       '==================\n'
       ' ILHAS\n'
       '==================\n')

landmass = []
for n in range (iCounter):
    island = []
    if islands[n][3] == 0:
        island.append([islands[n][0], 1])
        if islands[n][1] == islands[m][1] and islands[n][2]-1 == islands[m][2]:
            print ('- tem vizinho a esquerda')
        if islands[n][1] == islands[m][1] and islands[n][2]+1 == islands[m][2]:
            print ('- tem vizinho a direita')
        if islands[n][2] == islands[m][2] and islands[n][1]-1 == islands[m][1]:
            print ('- tem vizinho a cima')
        if islands[n][2] == islands[m][2] and islands[n][1]+1 == islands[m][1]:
            print ('- tem vizinho a baixo')
