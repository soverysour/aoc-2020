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

x = 0
y = 0
encountered = 0

while y < height:
    if (x % wrappingAt, y) in forest:
        encountered += 1

    x += 3
    y += 1

print(encountered)
