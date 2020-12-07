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


def main():
    with open('input.p1', 'r') as f:
        input_data = [parse_line(r) for r in f]

    valid_passwords = [p for p in input_data if (p['min'] <= p['string'].count(p['char']) <= p['max'])]

    print(len(valid_passwords))


if __name__ == '__main__':
    main()
