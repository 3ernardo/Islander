from random import randint

minSide, maxSide = 6, 12
h = randint(minSide, maxSide)
w = randint(minSide, maxSide)

def printMap():
    file = open('testfile.txt', 'w')
    header = str(w), ' ', str(h), '\n'
    file.writelines(header)

    matrix = [[randint(0, 1) for x in range(w)] for y in range(h)]

    for x in range (h):
        for y in range (w):
            file.write(str(matrix[x][y]))
            print(matrix[x][y], end='  ')
        file.write('\n')
        print()
    file.close()
printMap()