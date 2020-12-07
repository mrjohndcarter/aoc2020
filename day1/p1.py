import math
import unittest


def binary_search(sorted_list, search_value, start_index=0, end_index=None) -> int:
    if len(sorted_list) is 0:
        return -1;

    if end_index is None:
        end_index = len(sorted_list) - 1

    pivot_index = math.ceil((end_index - start_index) / 2) + start_index;

    if sorted_list[pivot_index] == search_value:
        return pivot_index

    if pivot_index != end_index:
        if search_value < sorted_list[pivot_index]:
            return binary_search(sorted_list, search_value, start_index, pivot_index - 1)

        return binary_search(sorted_list, search_value, pivot_index + 1, end_index)

    return -1;


def find_x_y_for_sum(input_data, search_sum):
    while input_data:
        current_x = input_data.pop()
        search_y = search_sum - current_x

        if binary_search(input_data, search_y) != -1:
            return current_x, search_y

    return None


def main():
    input_data = None;

    with open('input.p1', 'r') as f:
        input_data = [int(x) for x in f]

    result_tuple = find_x_y_for_sum(sorted(input_data), 2020)

    if result_tuple:
        print(
            f'{result_tuple[0]} + {result_tuple[1]} == 2020; {result_tuple[0]} * {result_tuple[1]} = {result_tuple[0] * result_tuple[1]}')
    else:
        print('not found')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


class TestBinarySearch(unittest.TestCase):

    def test_single(self):
        self.assertEqual(binary_search([2], 2), 0)

    def test_empty(self):
        self.assertEqual(binary_search([], 2), -1)

    def test_midpoint(self):
        self.assertEqual(binary_search([1, 2, 3], 2), 1)

    def test_midpoint_missing(self):
        self.assertEqual(binary_search([1, 2, 3], 4), -1)

    def test_atend(self):
        self.assertEqual(binary_search([1, 2, 3, 5, 7], 7), 4)

    def test_atstart(self):
        self.assertEqual(binary_search([1, 2, 5, 6, 7, 8], 1), 0)

    def test_beforestart(self):
        self.assertEqual(binary_search([11, 12, 15, 16, 17, 18], 10), -1)

    def test_afterend(self):
        self.assertEqual(binary_search([11, 12, 15, 16, 17, 18], 190), -1)