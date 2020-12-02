import re

good = 0
bad = 0

with open('./day2/input.txt') as f:
    for _line in f.readlines():
        line = _line.strip()
        lowest, highest, char, pwd = re.search(
            '([0-9]+)-([0-9]+)\\s+([a-z]): ([a-z]*)', line).groups()

        c = list(pwd).count(char)
        if c >= int(lowest) and c <= int(highest):
            good += 1
        else:
            bad += 1

print(good)
print(bad)
