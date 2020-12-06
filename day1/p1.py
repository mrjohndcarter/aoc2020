def find_x_y_for_sum(input_data, search_sum):
    while input_data:
        current_x = input_data.pop()
        search_y = search_sum - current_x
        if search_y in input_data:
            return current_x, search_y
    return None


def main():

    input_data = None;

    with open('input.p1', 'r') as f:
        input_data = [int(x) for x in f]

    result_tuple = find_x_y_for_sum(input_data, 2020)

    if result_tuple:
        print(f'{result_tuple[0]} + {result_tuple[1]} == 2020; {result_tuple[0]} * {result_tuple[1]} = {result_tuple[0] * result_tuple[1]}')
    else:
        print('not found')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
