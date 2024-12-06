with open('input4.txt') as file:
    table = []
    for line in file:
        table.append(line)

    count = 0
    for ii in range(len(table)):
        for jj in range(len(table[ii])):
            c = table[ii][jj]
            if c == 'X':
                # RIGHT
                if jj <= len(table[ii]) - 3 and table[ii][jj + 1] == 'M' and table[ii][jj + 2] == 'A' and table[ii][jj + 3] == 'S':
                    count = count + 1
                # LEFT
                if table[ii][jj - 1] == 'M' and table[ii][jj - 2] == 'A' and table[ii][jj - 3] == 'S':
                    count = count + 1
                # UP
                if ii >= 3 and table[ii - 1][jj] == 'M' and table[ii - 2][jj] == 'A' and table[ii - 3][jj] == 'S':
                    count = count + 1
                # DOWN
                if ii <= len(table) - 3 and table[ii + 1][jj] == 'M' and table[ii + 2][jj] == 'A' and table[ii + 3][jj] == 'S':
                    count = count + 1

                # DIAGONAL U-R
                if ii >= 3 and table[ii - 1][jj + 1] == 'M' and table[ii - 2][jj + 2] == 'A' and table[ii - 3][
                    jj + 3] == 'S':
                    count = count + 1
                # DIAGONAL U-L
                if ii >= 3 and table[ii - 1][jj - 1] == 'M' and table[ii - 2][jj - 2] == 'A' and table[ii - 3][
                    jj - 3] == 'S':
                    count = count + 1
                # DIAGONAL D-L
                if ii <= len(table) - 3 and table[ii + 1][jj - 1] == 'M' and table[ii + 2][jj - 2] == 'A' and \
                        table[ii + 3][jj - 3] == 'S':
                    count = count + 1
                # DIAGONAL D-R
                if ii <= len(table) - 3 and table[ii + 1][jj + 1] == 'M' and table[ii + 2][jj + 2] == 'A' and \
                        table[ii + 3][jj + 3] == 'S':
                    count = count + 1
print(count)

# PART 2

with open('input4.txt') as file:
    table = []
    for line in file:
        table.append(line)

    count = 0
    for ii in range(1, len(table) - 1):
        for jj in range(1, len(table[ii]) - 1):
            c = table[ii][jj]
            if c == 'A':
                if (((table[ii - 1][jj - 1] == 'S' and table[ii + 1][jj + 1] == 'M') or
                     (table[ii - 1][jj - 1] == 'M' and table[ii + 1][jj + 1] == 'S')) and
                        ((table[ii + 1][jj - 1] == 'S' and table[ii - 1][jj + 1] == 'M') or
                         (table[ii + 1][jj - 1] == 'M' and table[ii - 1][jj + 1] == 'S'))):

                    count = count + 1

print(count)
