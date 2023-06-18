def count_inversion(arr):
    start_idx = 0
    end_idx = len(arr) - 1
    output = inversion_count_func(arr, start_idx, end_idx)
    return output


def inversion_count_func(arr, start_idx, end_idx):
    if start_idx >= end_idx:
        return 0

    mid_idx = start_idx + (end_idx - start_idx) // 2

    # find number of inversions in left-half
    left_answer = inversion_count_func(arr, start_idx, mid_idx)

    # find number of inversions in right-half
    right_answer = inversion_count_func(arr, mid_idx + 1, end_idx)

    output = left_answer + right_answer

    # merge two sorted halves and count inversion while merging

    output += merge_two_sorted_halves(arr, start_idx, mid_idx, mid_idx + 1, end_idx)
    return output


def merge_two_sorted_halves(arr, start_one, end_one, start_two, end_two):
    count = 0
    left_idx = start_one
    right_idx = start_two

    output_length = (end_two - start_two + 1) + (end_one - start_one + 1)
    output_list = [0 for _ in range(output_length)]
    index = 0

    while index < output_length:
        # if left <= right, it's not an inversion
        if arr[left_idx] <= arr[right_idx]:
            output_list[index] = arr[left_idx]
            left_idx += 1
        else:
            count = count + (end_one - left_idx + 1)  # left > right hence it's an inversion
            output_list[index] = arr[right_idx]
            right_idx += 1

        index = index + 1

        if left_idx > end_one:
            for i in range(right_idx, end_two + 1):
                output_list[index] = arr[i]
                index += 1
            break

        elif right_idx > end_two:
            for i in range(left_idx, end_one + 1):
                output_list[index] = arr[i]
                index += 1
            break

    index = start_one
    for i in range(output_length):
        arr[index] = output_list[i]
        index += 1
    return count


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    if count_inversion(arr) == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    arr = [2, 5, 1, 3, 4]
    solution = 4
    test_case = [arr, solution]
    test_function(test_case)

    arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
    solution = 26
    test_case = [arr, solution]
    test_function(test_case)

    arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
    solution = 2
    test_case = [arr, solution]
    test_function(test_case)
