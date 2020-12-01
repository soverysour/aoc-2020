obs = set([])

with open("./day1/input.txt") as f:
    for line in f.readlines():
        number = int(line)
        if 2020 - number in obs:
            print(number * (2020 - number))
            break

        obs.add(number)
