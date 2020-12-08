import re


def parse_line(line) -> dict:
    # min-max letter: string
    # rem = re.match(r'[0-9]+-[0-9]+\w.:\w$', line)
    rem = re.match(r'(\d+)\-(\d+)\s(.):\s(.+)', line)
    return {
        'min': int(rem[1]),
        'max': int(rem[2]),
        'char': rem[3],
        'string': rem[4]
    }


def valid_password_p2(password) -> bool:
    return (password['string'][password['min'] - 1] == password['char']) ^ (
            password['string'][password['max'] - 1] == password['char'])


def main():
    with open('input.p1', 'r') as f:
        input_data = [parse_line(r) for r in f]

    valid_passwords = [p for p in input_data if (p['min'] <= p['string'].count(p['char']) <= p['max'])]

    valid_passwords_p2 = list(filter(valid_password_p2, input_data))

    print(f'p1 valid passwords: {len(valid_passwords)}')
    print(f'p2 valid passwords: {len(valid_passwords_p2)}')


if __name__ == '__main__':
    main()
