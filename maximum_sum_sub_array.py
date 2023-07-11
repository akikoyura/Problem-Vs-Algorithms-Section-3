# Helper Function - Find the max crossing sum
def max_crossing_sum(arr, start, mid, stop):
    # LEFT PHASE - Traverse the left part starting from the mid-element
    left_sum = arr[mid]  # Denotes the sum of the left part from mid-element to the current element
    left_max_sum = arr[mid]  # Keep track of maximum-sum

    # Traverse in reverse direction from (mid - 1) to start
    for i in range(mid - 1, start - 1, -1):  # The second argument of range is not inclusive.
        # The third argument is the step size.
        left_sum = left_sum + arr[i]
        if left_sum > left_max_sum:
            left_max_sum = left_sum  # update left_max_sum

    # RIGHT PHASE - Traverse the Right part, starting from (mid + 1)
    right_sum = arr[mid + 1]  # Denotes the sum of right part from (mid + 1) element to the current element
    right_max_sum = arr[mid + 1]  # Keep track of the maximum sum

    # Traverse in forward direction from (mid + 2) to stop
    for j in range(mid + 2, stop + 1):  # The second argument of range is not inclusive
        right_sum = right_sum + arr[j]
        if right_sum > right_max_sum:
            right_max_sum = right_sum  # Update right_max_sum

    # Both right_max_sum and left_max_sum each would contain value of at least one element from the arr
    return right_max_sum + left_max_sum


# Recursive function
def max_sub_array_recursive(arr, start, stop):  # start and stop are the indices
    # base case
    if start == stop:
        return arr[start]

    if start < stop:
        mid = (start + stop) // 2
        left = max_sub_array_recursive(arr, start, mid)
        right = max_sub_array_recursive(arr, mid + 1, stop)
        crossing_sum = max_crossing_sum(arr, start, mid, stop)
        return max(crossing_sum, max(left, right))
    else:  # If ever start > stop. Not feasible
        return arr[start]


def max_sub_array(arr):
    start = 0  # starting index of the original array
    stop = len(arr) - 1  # ending index of the original array
    return max_sub_array_recursive(arr, start, stop)


if __name__ == '__main__':
    # Test your code
    arr = [-2, 7, -6, 3, 1, -4, 5, 7]
    print("Maximum Sum = ", max_sub_array(arr))  # Outputs 13

    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Outputs 6
    print("Maximum Sum = ", max_sub_array(arr))

    arr = [-4, 14, -6, 7]
    print("Maximum Sum = ", max_sub_array(arr))  # Outputs 15

    arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
    print("Maximum Sum = ", max_sub_array(arr))  # Outputs 10a

    arr = [-2, -5, 6, -2, -3, 1, 5, -6]
    print("Maximum Sum = ", max_sub_array(arr))  # Outputs 7
