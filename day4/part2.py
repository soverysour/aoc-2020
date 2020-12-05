import re

passports = []

with open('./day4/input.txt') as f:
    currentPassport = {}

    for line in f.readlines():
        if line.strip() == '':
            passports.append(currentPassport)
            currentPassport = {}
            continue

        for match in re.findall('([a-z]{3}):([^\\s]*)', line):
            key = match[0]
            value = match[1]

            if key in currentPassport:
                print('Duplicate key for passport.')

            currentPassport[key] = value

    passports.append(currentPassport)

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)


def numin(k: str, lower: int, upper: int) -> bool:
    if re.search('^[1-9][0-9]*$', k):
        v = int(k)

        return v >= lower and v <= upper

    return False


def valid(key: str, value: str) -> bool:
    if key == 'byr':
        numin(value, 1920, 2002)
    if key == 'iyr':
        numin(value, 2010, 2020)
    if key == 'eyr':
        numin(value, 2020, 2030)
    if key == 'hgt':
        s = re.search('^([1-9][0-9]*)(in|cm)$', value)
        if not s:
            return False

        raw, unit = s.groups()

        if unit == 'in':
            return numin(raw, 59, 76)
        if unit == 'cm':
            return numin(raw, 150, 193)

        return False

    if key == 'hcl':
        return re.match('^#([a-f0-9]{6})$', value)

    if key == 'ecl':
        return re.match('^(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$', value)

    if key == 'pid':
        return re.match('^([0-9]{9})$', value)

    return True


requiredForValid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
areValid = 0

for p in passports:
    good = True

    for f in requiredForValid:
        if f not in p or not valid(f, p[f]):
            good = False
            break

    if good:
        areValid += 1

print(areValid)
