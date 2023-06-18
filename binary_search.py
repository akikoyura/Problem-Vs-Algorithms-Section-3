def binary_search(array, target):
    """
    Write a function that implements the binary search algorithm using iteration

    Args:
        array: a sorted array of items of the same type
        target: the element you're searching for

    Returns:
        int: the index of the target, if found, in the source
        -1: if the target is not found
    """
    left = array[0]
    right = len(array) - 1

    while left < right:
        middle = (left + right) // 2

        if array[middle] == target:
            return middle
        if array[middle] > target:
            right = middle - 1
        if array[middle] < target:
            left = middle + 1
    return -1


def binary_search_recursive(array, target):
    """
    This function will call `binary_search_recursive_soln` function.
    You don't need to change this function.

    Args:
      array: a sorted array of items of the same type
      target: the element you're searching for
    """
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    """
    Write a function that implements the binary search algorithm using recursion

    Args:
      array: a sorted array of items of the same type
      target: the element you're searching for
      start_index: beginning of the index of the sub-arrays
      end_index: end of the index of the sub-arrays

    Returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    """

    middle = (start_index + end_index) // 2

    if start_index > end_index:
        return -1

    if array[middle] == target:
        return middle
    elif array[middle] > target:
        return binary_search_recursive_soln(array[:middle], target, 0, middle)
    elif array[middle] < target:
        return binary_search_recursive_soln(array[middle + 1:], target, middle + 1, end_index)



def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


def test_function_recursive(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


if __name__ == '__main__':
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6
    index = 6
    test_case = [array, target, index]
    test_function(test_case)

    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 4
    index = 4
    test_case = [array, target, index]
    test_function_recursive(test_case)
