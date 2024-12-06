def calculeNextPos(posX, posY, direction):
    nextPos = (0, 0)
    if direction == 0:
        nextPos = posX - 1, posY
    elif direction == 1:
        nextPos = posX, posY + 1
    elif direction == 2:
        nextPos = posX + 1, posY
    elif direction == 3:
        nextPos = posX, posY - 1
    return nextPos


with open("input6.txt") as file:
    table = []
    for line in file:
        table.append(line)

    initialPos = (0, 0)
    for ii in range(len(table)):
        for jj in range(len(table[ii])):
            if table[ii][jj] == "^":
                initialPos = (ii, jj)

    posX, posY = initialPos
    visitedPositions = [initialPos]
    # Directions: 0 -> UP; 1 -> RIGHT; 2 -> DOWN; 3 -> LEFT
    direction = 0
    count = 0
    while 0 <= posX <= len(table[0]) - 1 and 0 <= posY <= len(table) - 1:
        nextPos = calculeNextPos(posX, posY, direction)

        if table[nextPos[0]][nextPos[1]] == "." or table[nextPos[0]][nextPos[1]] == "^":
            posX, posY = nextPos
            if nextPos not in visitedPositions:
                count += 1
                visitedPositions.append(nextPos)
        elif table[nextPos[0]][nextPos[1]] == "#":
            validPos = False
            while not validPos:
                direction = (direction + 1) % 4
                nextPos = calculeNextPos(posX, posY, direction)
                if table[nextPos[0]][nextPos[1]] == ".":
                    posX, posY = nextPos
                    validPos = True
                    if nextPos not in visitedPositions:
                        count += 1
                        visitedPositions.append(nextPos)

        print(count + 1)
