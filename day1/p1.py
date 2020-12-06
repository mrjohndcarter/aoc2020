
def main():

    input_data = None;

    with open('input.p1', 'r') as f:
        input_data = [int(x) for x in f]

    # find x + y == 2020

    while input_data:
        current_x = input_data.pop()
        search_y = 2020 - current_x
        if search_y in input_data:
            print(f'{current_x} + {search_y} = 2020, {current_x} * {search_y} = {current_x * search_y}')
            exit(0)

    print('Not found')
    exit(0)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
