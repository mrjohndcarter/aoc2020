from day1.p1 import find_x_y_for_sum


def main():
    result_tuple = None
    input_data = None;

    with open('input.p1', 'r') as f:
        input_data = sorted([int(x) for x in f])

    while input_data:
        current_x = input_data.pop(0)
        result_tuple = None
        current_yzsum = 2020 - current_x

        if current_yzsum > 0:
            result_tuple = find_x_y_for_sum(input_data, current_yzsum)

        if result_tuple:
            print(f'{current_x} + {result_tuple[0]} + {result_tuple[1]} == 2020; {current_x} * {result_tuple[0]} * {result_tuple[1]} = {current_x * result_tuple[0] * result_tuple[1]}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
