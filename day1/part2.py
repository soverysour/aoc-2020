l = []

with open("./day1/input.txt") as f:
    for line in f.readlines():
        l.append(int(line))

length = len(l)

for i in range(length):
    for j in range(length):
        for k in range(length):
            if i != j and j != k and i != k:
                e1 = l[i]
                e2 = l[j]
                e3 = l[k]

                if e1 + e2 + e3 == 2020:
                    print(e1 * e2 * e3)
                    exit(0)
