def fast_select(arr, k):
    """
    :param arr: the length of the original array
    :param k:  is an index
    :return:
    """
    n = len(arr)

    if 0 < k <= n:  # k should be a valid index

        # Helper variables
        set_of_medians = []
        arr_less_pivot = []
        arr_equal_pivot = []
        arr_greater_pivot = []
        i = 0

        # Step 1 - Break Arr into groups of sizes 5
        # Step 2 - For each group, sort and find median (middle). Add the median to set_of_medians.

        while i < n // 5:  # n / 5 gives the integer quotient of the division
            median = find_median(arr, 5 * i, 5)  # find the median of each group sizes 5
            set_of_medians.append(median)
            i += 1

        # if n is not a multiple of 5, then a last group with size = n % 5 will be formed
        if 5 * i < n:
            median = find_median(arr, 5 * i, n % 5)
            set_of_medians.append(median)

        # Step 3 - Find the median of set_of_medians
        if len(set_of_medians) == 1:  # base case for this task
            pivot = set_of_medians[0]
        elif len(set_of_medians) > 1:
            size = len(set_of_medians) // 2
            pivot = fast_select(set_of_medians, size)

        # Step 4 - Partition the original arr into three sub-arrays
        for element in arr:
            if element < pivot:
                arr_less_pivot.append(element)
            elif element > pivot:
                arr_greater_pivot.append(element)
            else:
                arr_equal_pivot.append(element)

        # Step 5 - Recurse based on the sizes of the three sub-arrays
        if k <= len(arr_less_pivot):
            return fast_select(arr_less_pivot, k)
        elif k > (len(arr_less_pivot) + len(arr_equal_pivot)):
            return fast_select(arr_greater_pivot, (k - len(arr_less_pivot) - len(arr_equal_pivot)))
        else:
            return pivot


def find_median(arr, start, size):
    my_list = []
    for i in range(start, start + size):
        my_list.append(arr[i])

    # sort the array
    my_list.sort()

    # return the middle 
    return my_list[size // 2]


if __name__ == '__main__':
    arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
    k = 5
    print(fast_select(arr, k))  # outputs = 12

    arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
    k = 5
    print(fast_select(arr, k))  # outputs = 11

    arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
    k = 10
    print(fast_select(arr, k))  # outputs = 99
