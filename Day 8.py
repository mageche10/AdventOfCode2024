def hasAntenna(x, y, table):
    return not table[y][x] == "."


# Pot haver un antinode de varies antenes en una mateixa posicio -> llavors ja no es unica

table = []
with open("input8.txt") as file:
    for line in file:
        table.append(line[:-1])

antennas = []
for yy in range(len(table)):
    for xx in range(len(table[yy])):
        if hasAntenna(xx, yy, table):
            antennas.append((table[yy][xx], xx, yy))

antennas.sort()
antennasSaved = antennas

nodes = []
for aType in antennas:
    same = list(filter(lambda x: x[0] == aType[0], antennas))

    for ii in range(len(same)):
        for jj in (list(range(ii + 1, len(same)))):
            deltaX = same[jj][2] - same[ii][2]
            deltaY = same[jj][1] - same[ii][1]

            nX = same[ii][2] - deltaX
            nX2 = same[ii][2] + 2 * deltaX
            nY = same[ii][1] - deltaY
            nY2 = same[ii][1] + 2 * deltaY

            if ((0 <= nX <= len(table[0]) - 1 and 0 <= nY <= len(table) - 1)
                    and ((nX, nY) not in nodes)):
                nodes.append((nX, nY))

            if ((0 <= nX2 <= len(table[0]) - 1 and 0 <= nY2 <= len(table) - 1)
                    and ((nX2, nY2) not in nodes)):
                nodes.append((nX2, nY2))

    antennas = antennas[len(same):]
print(len(nodes))

antennas = antennasSaved
nodesP2 = []
for aType in antennas:
    same = list(filter(lambda x: x[0] == aType[0], antennas))

    for ii in range(len(same)):
        for jj in (list(range(ii + 1, len(same)))):
            deltaX = same[jj][2] - same[ii][2]
            deltaY = same[jj][1] - same[ii][1]

            n = 0
            nX = same[ii][2] + n*deltaX
            nY = same[ii][1] + n*deltaY
            while 0 <= nX <= len(table[0]) - 1 and 0 <= nY <= len(table) - 1:
                if (nX, nY) not in nodesP2:
                    nodesP2.append((nX, nY))
                n += 1

                nX = same[ii][2] + n*deltaX
                nY = same[ii][1] + n*deltaY

            n = 1
            nX = same[ii][2] - n * deltaX
            nY = same[ii][1] - n * deltaY
            while 0 <= nX <= len(table[0])-1 and 0 <= nY <= len(table) - 1:
                if (nX, nY) not in nodesP2:
                    nodesP2.append((nX, nY))
                n += 1

                nX = same[ii][2] - n * deltaX
                nY = same[ii][1] - n * deltaY

    antennas = antennas[len(same):]

print(len(nodesP2))
