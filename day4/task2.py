import sys


class TwoSplitOperation:
    def __init__(self, split_on, pre_rule=None, post_rule=None):
        self.split_on = split_on
        self.pre_rule = pre_rule
        self.post_rule = post_rule

    def validate(self, value):
        validity = True

        if self.pre_rule:
            validity = validity and self.pre_rule.validate(value.split(self.split_on)[0])

        if self.post_rule:
            validity = validity and self.post_rule.validate(value.split(self.split_on)[1])

        return validity


class PrefSuffRule:
    def __init__(self, valid_prefixes=None, valid_suffixes=None):
        self.valid_prefixes = valid_prefixes
        self.valid_suffixes = valid_suffixes

    def validate(self, value):
        if self.valid_prefixes:
            for pref in self.valid_prefixes:

                if not value.startswith(pref):
                    return False

        if self.valid_suffixes:
            for suff in self.valid_suffixes:

                if not value.endswith(suff):
                    return False

        return True


class NumberRule:
    def __init__(self, num_of_digits=None, upper_value_bound=None, lower_value_bound=None, leading_zeros=False):
        self.num_of_digits = num_of_digits
        self.upper_value_bound = upper_value_bound
        self.lower_value_bound = lower_value_bound
        self.leading_zeros = leading_zeros

    def validate(self, value):
        assert type(value) == str

        if not value.startswith('0'):
            return False

        value = int(value)  # TODO what if float

        if self.num_of_digits:
            if not len(str(value)) == self.num_of_digits:
                return False

        if self.upper_value_bound:
            if value > self.upper_value_bound:
                return False

        if self.lower_value_bound:
            if value < self.lower_value_bound:
                return False

        return True


class CharRule:
    def __init__(self, valid_chars=None, char_count=None, exact_match_one_of=None):
        self.valid_chars = valid_chars
        self.char_count = char_count
        self.exact_match_one_of = exact_match_one_of

    def validate(self, value):
        assert type(value) == str

        if self.valid_chars:
            for char in value:
                if not char in self.valid_chars:
                    return False

        if self.char_count:
            if not len(str(value)) == self.char_count:
                return False

        if self.exact_match_one_of:
            matches = 0
            for exact_match_chars in self.exact_match_one_of:
                if value == exact_match_chars:
                    matches += 1

            if not matches == 1:
                return False

        return True


REQIURED_KEYS = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
}


REQIURED_VALUES = {
    'byr': [NumberRule(num_of_digits=4, upper_value_bound=2002, lower_value_bound=1920)],
    'iyr': [NumberRule(num_of_digits=4, upper_value_bound=2020, lower_value_bound=2010)],
    'eyr': [NumberRule(num_of_digits=4, upper_value_bound=2030, lower_value_bound=2020)],
    'hgt': [PrefSuffRule(valid_suffixes=['cm', 'in']),
            TwoSplitOperation(split_on='cm', pre_rule=NumberRule(upper_value_bound=193, lower_value_bound=150)),
            TwoSplitOperation(split_on='in', pre_rule=NumberRule(upper_value_bound=76, lower_value_bound=59))],
    'hcl': [PrefSuffRule(valid_prefixes=['#']),
            TwoSplitOperation(split_on='#', post_rule=CharRule(valid_chars=list(map(str, range(10))),
                                                               char_count=6)),
            TwoSplitOperation(split_on='#', post_rule=CharRule(valid_chars=['a', 'b', 'c', 'd', 'e', 'f'],
                                                               char_count=6))
            ],
    'ecl': [CharRule(exact_match_one_of=['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])],
    'pid': [NumberRule(num_of_digits=9, leading_zeros=True)]
}


def count_valid_passports(passports):
    count = 0

    for passport in passports:
        passport_dict = dict(field.split(':') for field in passport)

        required_fields_validity = not REQIURED_KEYS - set(passport_dict.keys())

        validity = True

        for key, val in passport_dict.items():
            if key != 'cid':
                for rule in REQIURED_VALUES[key]:
                    validity = validity and rule.validate(val)

        required_values_validity = validity

        if required_fields_validity and required_values_validity:
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
