# (x, y) elems
forest = set([])

height = 0
wrappingAt = 0
with open('./day3/input.txt') as f:
    for line in f.readlines():
        wrappingAt = len(line)

        for i in range(len(line)):
            if line[i] == '#':
                forest.add((i, height))

        height += 1


def getEncounter(xIncrement: int, yIncrement: int) -> int:
    encountered = 0
    x = 0
    y = 0

    while y < height:
        if (x % wrappingAt, y) in forest:
            encountered += 1

        x += xIncrement
        y += yIncrement

    return encountered


s11 = getEncounter(1, 1)
s31 = getEncounter(3, 1)
s51 = getEncounter(5, 1)
s71 = getEncounter(7, 1)
s12 = getEncounter(1, 2)

print(s11)
print(s31)
print(s51)
print(s71)
print(s12)

print()
print(s11 * s31 * s51 * s71 * s12)
