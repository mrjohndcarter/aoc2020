def main():

    all_groups = []

    with open('input.p1', 'r') as f:
        all_declarations = f.readlines()
        group = {
            "size": 0,
            "yes": set()
        }
        for line in all_declarations:

            group['size'] += 1
            group['yes'].update([c for c in line.strip()])

            if line == '\n':
                # that's the end of group
                all_groups.append(group)
                group = {
                    "size": 0,
                    "yes": set()
                }

        # add the last one
        all_groups.append(group)

    sum = 0
    for group in all_groups:
        sum += len(group['yes'])

    print(f'Sum is: {sum}')

if __name__ == '__main__':
    main()