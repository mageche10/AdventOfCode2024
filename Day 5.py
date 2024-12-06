import random


def checkOrder(a, b, llista):
    # Checks if a is before b in a given list
    if b in llista:
        posA = llista.index(a)
        posB = llista.index(b)
        return posA < posB
    else:
        return True


def checkUpdate(pages):
    valid = True
    fail = 0
    for page in pages:
        if valid:
            for rule in workedRules:
                if rule[0] == page:
                    if not checkOrder(rule[0], rule[1], pages):
                        valid = False
                        fail = pages.index(page)

    return valid, fail


with open("input5.txt") as file:
    rules = []
    updates = []
    inRules = True

    for line in file:
        if line.isspace():
            inRules = False
        else:
            rules.append(line) if inRules else updates.append(line)

    workedRules = list()
    for rule in rules:
        workedRules.append((int(rule.split("|")[0]), int(rule.split("|")[1])))

    count = 0
    for update in updates:
        pages = list(map(int, update.split(",")))
        valid, fail = checkUpdate(pages)

        if valid:
            count = count + pages[int((len(pages) - 1) / 2)]

print(count)

# PART 2

with open("input5.txt") as file:
    rules = []
    updas = []
    inRules = True

    for line in file:
        if line.isspace():
            inRules = False
        else:
            rules.append(line) if inRules else updas.append(line)

    workedRules = list()
    for rule in rules:
        workedRules.append((int(rule.split("|")[0]), int(rule.split("|")[1])))

    count = 0
    for update in updas:
        pages = list(map(int, update.split(",")))
        valid, fail = checkUpdate(pages)

        if not valid:
            while not valid:
                i = fail
                p = pages.pop(i)
                pages.insert(i - 1, p)
                valid, fail = checkUpdate(pages)

            count = count + pages[int((len(pages) - 1) / 2)]


print(count)
