def find_sum(target_sum, window_list):
    search_set = set(window_list)

    for value in search_set:
        if target_sum - value in search_set:
            return True

    return False


def find_longest_sequence_not_exceeding(a_list, value):
    sum = 0
    for i in range(len(a_list)):
        sum += a_list[i]
        if sum > value:
            return a_list[slice(0, i - 1)], sum - a_list[i]
    return None, 0


def main():
    transmission = []
    window_size = 25
    not_found = None

    with open('input.p1', 'r') as f:
        transmission = list(map(int, f))

    for i in range(window_size, len(transmission)):
        if not find_sum(transmission[i], transmission[slice(i - window_size, i)]):
            print(f'Could not find: {transmission[i]}')
            not_found = transmission[i]
            break

    for i in range(len(transmission)):
        sequence, value = find_longest_sequence_not_exceeding(transmission[slice(i, len(transmission))], not_found)

        if value == not_found:
            print(f'Found Sequence: {sequence}')
            sequence = sorted(sequence)
            print(f'Adding smallest and largest of found sequence: {sequence[0] + sequence[-1]}')
            return


if __name__ == '__main__':
    main()
