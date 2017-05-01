from random import randint

def dimensionDefiner(minSide, maxSide): # Returns the random sizes for the height and width of the matrix within given boundaries.
    height = randint(minSide, maxSide)
    width = randint(minSide, maxSide)
    return height, width

def testFileRandomizer(h, w): # Creates a matrix of 0 and 1 based on the previously randomized size limits.
    header = str(w), ' ', str(h), '\n'
    matrix = [[randint(0, 1) for x in range(w)] for y in range(h)]
    with open('TestFile.txt', 'w') as inputFile:
        inputFile.writelines(header)
        for y in range(h):
            for x in range(w):
                inputFile.write(str(matrix[y][x]))
            inputFile.write('\n')
    return matrix

def testFilePrinter(toPrint, h, w): # Just for testing. Prints the matrix dimensions and the matrix itself with spaces.
    print('Map dimensions:\n Width %s\n Height %s\n' % (w, h))
    for x in range (h):
        for y in range (w):
            print(toPrint[x][y], end=' ')
        print()

h, w = dimensionDefiner(8, 12) # Optional size randomizer.
matrix = testFileRandomizer(h, w) # Alternatively the height and width can be directly defined here though parameters.
testFilePrinter(matrix, h, w) # Optional console print.