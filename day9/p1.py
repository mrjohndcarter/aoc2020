import itertools


def find_sum(target_sum, window_list):
    search_set = set(window_list)

    for value in search_set:
        if target_sum - value in search_set:
            return True

    return False


def main():
    transmission = []
    window_size = 25

    with open('input.p1', 'r') as f:
        transmission = list(map(int, f))

    for i in range(window_size, len(transmission)):
        if not find_sum(transmission[i], transmission[slice(i - window_size, i)]):
            print(f'Could not find: {transmission[i]}')
            break




if __name__ == '__main__':
    main()
