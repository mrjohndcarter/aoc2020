def main():

    highest_pass_number = 0
    seat_ids = []

    with open('input.p1', 'r') as f:
        for boarding_pass_string in f:

            start = 0
            end = window_size = 2 ** 7

            for i in range(len(boarding_pass_string) - 4):
                current = boarding_pass_string[i]

                window_size = int(window_size / 2)

                # go lower
                if (boarding_pass_string[i] == 'F'):
                    end = start + window_size
                # go upper
                elif (boarding_pass_string[i] == 'B'):
                    start = start + window_size


            region = start

            start = 0
            end = window_size = 2 ** 3
            for i in range(7,10):
                window_size = int(window_size / 2)

                # go lower
                if (boarding_pass_string[i] == 'L'):
                    end = start + window_size
                # go upper
                elif (boarding_pass_string[i] == 'R'):
                    start = start + window_size

            col = start

            seat_id = (region * 8) + col

            print(f'Code: {boarding_pass_string} Id: {seat_id}')

            seat_ids.append(seat_id)

            if seat_id > highest_pass_number:
                highest_pass_number = seat_id

    seat_ids = sorted(seat_ids)
    print(f'Highest Pass Number is: {highest_pass_number}')

    # this is sketchy, not sure how to determine if seat is at the front
    while seat_ids:
        current = seat_ids.pop(0)
        if seat_ids and seat_ids[0] - current >= 2:
            print(f'Missing: {current+1}')


if __name__ == '__main__':
    main()