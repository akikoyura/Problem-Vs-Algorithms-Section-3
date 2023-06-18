def first_and_last_index(arr, number):
    first_idx = find_first_index(arr, number, 0, len(arr) - 1)
    last_idx = find_last_index(arr, number, 0, len(arr) - 1)
    return [first_idx, last_idx]


def find_first_index(arr, number, start_index, end_index):
    if start_index > end_index:
        return -1

    middle_idx = start_index + (end_index - start_index) // 2
    if arr[middle_idx] == number:
        current_position = find_first_index(arr, number, start_index, middle_idx - 1)
        if current_position != -1:
            first_idx = current_position
        else:
            first_idx = middle_idx
        return first_idx

    elif arr[middle_idx] < number:
        return find_first_index(arr, number, middle_idx + 1, end_index)
    else:
        return find_first_index(arr, number, start_index, middle_idx - 1)


def find_last_index(arr, number, start_idx, end_idx):
    if start_idx > end_idx:
        return -1

    middle_idx = start_idx + (end_idx - start_idx) // 2
    if arr[middle_idx] == number:
        current_position = find_last_index(arr, number, middle_idx + 1, end_idx)
        if current_position != -1:
            last_idx = current_position
        else:
            last_idx = middle_idx
        return last_idx

    elif arr[middle_idx] < number:
        return find_last_index(arr, number, middle_idx + 1, end_idx)
    else:
        return find_last_index(arr, number, start_idx, middle_idx - 1)


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    # input_list = [1]
    # number = 1
    # solution = [0, 0]
    # test_case_1 = [input_list, number, solution]
    # test_function(test_case_1)

    input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
    number = 3
    solution = [3, 6]
    test_case_2 = [input_list, number, solution]
    test_function(test_case_2)

    input_list = [0, 1, 2, 3, 4, 5]
    number = 5
    solution = [5, 5]
    test_case_3 = [input_list, number, solution]
    test_function(test_case_3)

    input_list = [0, 1, 2, 3, 4, 5]
    number = 6
    solution = [-1, -1]
    test_case_4 = [input_list, number, solution]
    test_function(test_case_4)
