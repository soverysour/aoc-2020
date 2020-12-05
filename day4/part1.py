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

requiredForValid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
areValid = 0

for p in passports:
    good = True

    for f in requiredForValid:
        if f not in p:
            good = False
            break

    if good:
        areValid += 1

print(areValid)
