def makeList(lst, num):
    for i in range(0, 6):
        base = pow(10, 5-i)
        lst.append(num // base)
        num -= lst[i] * base

def isAscending(lst):
    digit = lst[0]
    for i in range(1, 6):
        if lst[i] < digit:
            return False
        digit = lst[i]
    return True

def hasPair(lst):
    flag = False
    for i in range(0, 5):
        if lst[i] == lst[i+1]:
            flag = True
    return flag

def hasTriplet(lst):
    flag = False
    for i in range(0, 4):
        if lst[i] == lst[i+1] == lst[i+2]:
            flag = True
    return flag

def hasPurePair(lst):
    for i in range(1, 4):
        if lst[i-1] != lst[i] == lst[i+1] != lst[i+2]:
            return True
    if lst[0] == lst[1] != lst[2]:
        return True
    if lst[3] != lst[4] == lst[5]:
        return True
    return False

def part_one():
    count = 0
    for num in range(171309, 643604):
        lst = []
        makeList(lst, num)
        if isAscending(lst) and hasPair(lst):
            count += 1
    print(count)

def part_two():
    count = 0
    for num in range(171309, 643604):
        lst = []
        makeList(lst, num)
        if isAscending(lst) and hasPurePair(lst):
            count += 1
            print(num)
    print(count)

part_two()