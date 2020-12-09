def trees_for_slope(pattern, slope) -> int:
    horizontal_size = len(pattern[0]);
    vertical_size = len(pattern);

    x, y = 0, 0
    tree_count = 0

    # remember that we access x,y as input_data[y][x]

    while y < vertical_size:
        if pattern[y][x] == '#':
            tree_count += 1
        y += slope['down']
        x = (x + slope['right']) % horizontal_size

    return tree_count


def main():
    input_data = None;

    with open('input.p1', 'r') as f:
        input_data = [[c for c in x.strip()] for x in f]

    slope = {
        'right': 3,
        'down': 1
    }

    print(f'Tree count: {trees_for_slope(input_data, slope)}')

    print(
        f'P2 value: {trees_for_slope(input_data, {"right": 1, "down": 1}) * trees_for_slope(input_data, {"right": 3, "down": 1}) * trees_for_slope(input_data, {"right": 5, "down": 1}) * trees_for_slope(input_data, {"right": 7, "down": 1}) * trees_for_slope(input_data, {"right": 1, "down": 2})}')


if __name__ == '__main__':
    main()
