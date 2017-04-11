from random import randint

h = 8 # Map height
w = 10 # Map width
map = [[randint(0, 1) for x in range(w)] for y in range(h)]
counter = 1

def printMap():
    for x in range (h):
        for y in range (w):
            print(map[x][y], end='  ')
        print()

def printIslands():
    for x in range(h):
        for y in range(w):
            print("%02d" %(map[x][y]), end=' ')
        print()

def landInSight(m, h, w, c):
    if m[h][w] == 1:
        m[h][w] = c
        if w < len(m[0]) - 1: landInSight(m, h, w + 1, c)
        if h < len(m) - 1: landInSight(m, h + 1, w, c)
        if w > 0: landInSight(m, h, w - 1, c)
        if h > 0: landInSight(m, h - 1, w, c)

def swipe(counter):
    for x in range(h):
        for y in range(w):
            counter += 1
            landInSight(map, x, y, counter)

printMap()
swipe(counter)
print('=============================')
printIslands()