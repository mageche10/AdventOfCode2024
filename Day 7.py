def isValid(target, numbers):
    if len(numbers) == 0:
        return target == 0
    if target == 0:
        return False
    return isValid(target - numbers[-1], numbers[:-1]) or (
                target % numbers[-1] == 0 and isValid(target // numbers[-1], numbers[:-1]))


with open("input7.txt") as file:
    count = 0
    for line in file:
        target = int(line.split(":")[0])
        numbers = list(map(int, line.split(":")[1][1:-1].split(" ")))

        if isValid(target, numbers):
            count += target

    print(count)


# PART 2
def isValid2(target, numbers):
    if len(numbers) == 1:
        return numbers[0] == target
    if isValid2(target, [numbers[0] + numbers[1]] + numbers[2:]):
        return True
    if isValid2(target, [numbers[0] * numbers[1]] + numbers[2:]):
        return True
    if isValid2(target, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:]):
        return True
    return False


with open("input7.txt") as file:
    count = 0
    for line in file:
        target = int(line.split(":")[0])
        numbers = list(map(int, line.split(":")[1][1:-1].split(" ")))

        if isValid2(target, numbers):
            count += target

    print(count)
