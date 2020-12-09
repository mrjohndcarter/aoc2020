import re

must_includes_keys = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']


def convert_to_int(string) -> int:
    return int(string, base=10)


def validate_byr(value):
    if len(value) != 4:
        return False
    try:
        v = convert_to_int(value)
        return 1920 <= v <= 2002
    except ValueError:
        pass
    return False


def validate_iyr(value):
    if len(value) != 4:
        return False
    try:
        v = convert_to_int(value)
        return 2010 <= v <= 2020
    except ValueError:
        pass
    return False


def validate_eyr(value):
    if len(value) != 4:
        return False
    try:
        v = convert_to_int(value)
        return 2020 <= v <= 2030
    except ValueError:
        pass
    return False


def validate_hgt(value):
    rem = re.match(r'(\d+)(cm|in)', value)
    if rem:
        try:
            v = convert_to_int(rem[1])
            if rem[2] == 'cm':
                return 150 <= v <= 193
            elif rem[2] == 'in':
                return 59 <= v <= 76
        except ValueError:
            pass
    return False


def validate_hcl(value):
    rem = re.match(r'#([0-9a-f]{6})$', value)
    if rem:
        return True
    return False


def validate_ecl(value):
    rem = re.match(r'(amb|blu|brn|gry|grn|hzl|oth)$', value)
    if rem:
        return True
    return False


def validate_pid(value):
    rem = re.match(r'(\d{9})$', value)
    if rem:
        return True
    return False


validators = {
    'byr': validate_byr,
    'iyr': validate_iyr,
    'eyr': validate_eyr,
    'hgt': validate_hgt,
    'hcl': validate_hcl,
    'ecl': validate_ecl,
    'pid': validate_pid
}


def is_valid_passport_or_northpole_cred(obj) -> bool:
    for key in must_includes_keys:
        if key not in obj:
            return False
        if not validators[key](obj[key]):
            return False

    return True


def main():
    potential_passports = []

    with open('input.p1', 'r') as f:
        input_data = f.readlines()
        passport = {}
        for line in input_data:

            if line is '\n':
                # new passport
                potential_passports.append(passport)
                passport = {}

            else:
                key_values = line.split()
                for kv in key_values:
                    key, value = kv.split(':')
                    passport[key] = value

        # add the last one
        potential_passports.append(passport)

        valid_passports = list(filter(is_valid_passport_or_northpole_cred, potential_passports))

        print(f'P1 Number of valid passports found: {len(valid_passports)}')


if __name__ == '__main__':
    main()

import unittest


class TestValidators(unittest.TestCase):

    def test_height(self):
        self.assertTrue(validate_hgt('151cm'))
        self.assertFalse(validate_hgt('19cm'))
        self.assertFalse(validate_hgt('12amc'))
        self.assertTrue(validate_hgt('59in'))
        self.assertTrue(validate_hgt('76in'))
        self.assertFalse(validate_hgt('77in'))

    def test_haircolor(self):
        self.assertTrue(validate_hcl('#cccc1b'))
        self.assertFalse(validate_hcl('#cccc1ba'))
        self.assertFalse(validate_hcl('#cc1ba'))

    def test_eyecolor(self):
        self.assertTrue(validate_ecl('amb'))
        self.assertFalse(validate_ecl('amb2'))
        self.assertTrue(validate_ecl('oth'))

    def test_passport_id(self):
        self.assertTrue(validate_pid('896056539'))
        self.assertFalse(validate_pid('89605653'))
        self.assertFalse(validate_pid('8960a5653'))
