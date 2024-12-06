with open('input.txt') as file:
    l1 = list()
    l2 = list()

    for line in file:
        l1.append(int(line.split('   ')[0]))
        l2.append(int(line.split('   ')[1]))

    l1.sort()
    l2.sort()

    maxDist = 0
    for n in range(len(l1)):
        maxDist = maxDist + abs(l1[n] - l2[n])

    print(maxDist)

    similarity = 0

    for number in l1:
        count = 0
        for n2 in l2:
            if number == n2:
                count += 1

        similarity += count * number

    print(similarity)
