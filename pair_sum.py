def pair_sum(arr, target):
    # Sort the list
    arr.sort()

    # Initial two pointers - one from the start of the array and the other from the end
    front_idx = 0
    back_idx = len(arr) - 1

    # Shift the pointers
    while front_idx < back_idx:
        front = arr[front_idx]
        back = arr[back_idx]

        if front + back == target:
            return [front, back]

        elif front + back < target:  # sum < target ==> shift front pointer forward
            front_idx += 1
        else:
            back_idx += 1  # sum > target ==> shift back pointer backward

    return [None, None]


def test_function(test_case):
    input_list = test_case[0]
    target = test_case[1]

    solution = test_case[2]
    output = pair_sum(input_list, target)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    input_list = [2, 7, 11, 15]
    target = 9
    solution = [2, 7]
    test_case = [input_list, target, solution]
    test_function(test_case)

    input_list = [0, 8, 5, 7, 9]
    target = 9
    solution = [0, 9]
    test_case = [input_list, target, solution]
    test_function(test_case)

    input_list = [110, 9, 89]
    target = 9
    solution = [None, None]
    test_case = [input_list, target, solution]
    test_function(test_case)
