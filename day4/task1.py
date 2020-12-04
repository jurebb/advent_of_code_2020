import sys


REQIURED_KEYS = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
}


def count_valid_passports(passports):
    count = 0

    for passport in passports:
        passport_keys = dict(field.split(':') for field in passport).keys()

        if not REQIURED_KEYS - set(passport_keys):
            count += 1

    return count


def extract_passports_from_stdin(passports):
    current_passport = list()
    for line in sys.stdin:
        line = line.strip()

        if line == '':

            if current_passport:
                passports.append(current_passport)

                current_passport = list()

        else:
            current_passport.extend(line.split(' '))

    if current_passport:
        passports.append(current_passport)


def main():
    passports = list()

    extract_passports_from_stdin(passports)

    valid_count = count_valid_passports(passports)

    print(valid_count)


if __name__ == '__main__':
    main()
