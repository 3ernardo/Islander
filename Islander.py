from random import randint

# Definition of the Height and Width of the matrix;
w, h = 10, 8;

k, t = 0,0

matrix = [[randint(0, 1) for x in range(w)] for y in range(h)]
islands = []

k, t = 0,2

x = 65;
y = 65;
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

iCounter = 0
iReference = 0

for iHCoord in range (h):
    for iWCoord in range (w):
        if matrix[iHCoord][iWCoord] == 1:
            print ('Coordenadas: h', chr(iHCoord+65), ' w', chr(iWCoord+65))
            iCounter += 1
            islands.append([iCounter, iHCoord, iWCoord, iReference])
print (islands)