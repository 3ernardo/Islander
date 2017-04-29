# Reads the file and creates the matrix map.
with open('testfile.txt') as f:
    w = int(f.read(1))
    f.read(1)
    h = int(f.read(1))
    f.read(1)
    map = [[2 for x in range(w)] for y in range(h)]
    for y in range(h):
        for x in range(w):
            map[y][x] = int(f.read(1))
        f.read(1)

# Swipes the matrix map after NEW land chunks.
def swipe():
    counter = 0
    for x in range(h):
        for y in range(w):
            if map[x][y] == 1:
                counter += 1
                landInSight(map, x, y, 99)
    print(counter)

# Recursive function to hide any land attached to a chunk already swiped.
def landInSight(m, h, w, c):
    if m[h][w] == 1:
        m[h][w] = c
        if w < len(m[0]) - 1: landInSight(m, h, w + 1, c)
        if h < len(m) - 1: landInSight(m, h + 1, w, c)
        if w > 0: landInSight(m, h, w - 1, c)
        if h > 0: landInSight(m, h - 1, w, c)

# Calls the swipe function.
swipe()