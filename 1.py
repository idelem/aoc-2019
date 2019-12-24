def part_one():
    fuel = 0
    with open('1.txt', 'r') as f:
        lst = f.readlines()
    for line in lst:
        mass = int(line)
        fuel += mass // 3 - 2
    return fuel

def part_two():
    total = 0
    with open('1.txt', 'r') as f:
        lst = f.readlines()
    for line in lst:
        mass = int(line)
        fuel = mass // 3 - 2
        fuels = [fuel]
        while fuels[-1] > 0:
            fuels.append(fuels[-1] // 3 - 2)
        fuels[-1] = 0
        total += sum(fuels)
    print(total)

part_two()