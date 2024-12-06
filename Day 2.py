def checkDiff(a, b):
    if 1 <= abs(a - b) <= 3:
        return True
    else:
        return False


def checkDecreasing(elements):
    for jj in range(len(elements) - 1):
        if elements[jj + 1] < elements[jj]:
            continue
        else:
            return False
    return True


def checkIncreasing(elements):
    for jj in range(len(elements) - 1):
        if elements[jj + 1] > elements[jj]:
            continue
        else:
            return False
    return True


with open('input2.txt') as file:
    count = 0

    for line in file:
        values = line.split(' ')
        values = list(map(int, values))

        valid = False
        if checkDecreasing(values) or checkIncreasing(values):
            valid = True

            for n in range(len(values) - 1):
                if not checkDiff(values[n], values[n + 1]):
                    valid = False

            if valid:
                count += 1

        if not valid:
            checked = False
            while not checked:
                for ii in range(len(values)):
                    valuesP = values[0:ii] + values[ii + 1:]

                    if checkDecreasing(valuesP) or checkIncreasing(valuesP):
                        valid = True

                        for nn in range(len(valuesP) - 1):
                            if not checkDiff(valuesP[nn], valuesP[nn + 1]):
                                valid = False

                        if valid:
                            count += 1
                            checked = True
                            break

                if ii == len(values) - 1:
                    checked = True

print(count)
