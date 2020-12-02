import re

good = 0
bad = 0

with open('./day2/input.txt') as f:
    for _line in f.readlines():
        line = _line.strip()
        lowest, highest, char, pwd = re.search(
            '([0-9]+)-([0-9]+)\\s+([a-z]): ([a-z]*)', line).groups()

        f1 = pwd[int(lowest) - 1]
        f2 = pwd[int(highest) - 1]
        if f1 != f2 and (f1 == char or f2 == char):
            good += 1
        else:
            bad += 1

print(good)
print(bad)
