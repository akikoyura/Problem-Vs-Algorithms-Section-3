def merge_sort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # Call mergesort recursively with the left and right half
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge our two halves and return
    return merge(left, right)


def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0

    # Move through the lists until we have exhausted one
    while left_idx < len(left) and right_idx < len(right):
        # If left's item is larger, append right's item
        # and increment the index
        if left[left_idx] > right[right_idx]:
            merged.append(right[right_idx])
            right_idx += 1

        # otherwise, append left's item and increment
        else:
            merged.append(left[left_idx])
            left_idx += 1

    # Append any leftovers. Because we've broken from our while loop,
    # We know at least one is empty, and the remaining:
    # a) is already sorted
    # b) all sorts past our last element in merged
    merged += left[left_idx:]
    merged += right[right_idx:]

    # return the ordered, merged list
    return merged


if __name__ == '__main__':
    list1 = [0, 1, 2, 3]
    midpoint1 = len(list1) // 2
    print('List 1 midpoint: {}'.format(midpoint1))

    list2 = [4, 5, 6]
    midpoint2 = len(list2) // 2
    print('List 2 midpoint: {}'.format(midpoint2))

    left1 = list1[:midpoint1]
    right1 = list1[midpoint1:]

    print('List 1 left side: {}'.format(left1))
    print('List 1 right side: {}'.format(right1))

    left2 = list2[:midpoint2]
    right2 = list2[midpoint2:]

    print('List 2 left side: {}'.format(left2))
    print('List 2 right side: {}'.format(right2))

    # Test this out
    merged = merge([1, 3, 7], [2, 5, 6])
    print(merged)

    test_list_1 = [8, 3, 1, 7, 0, 10, 2]
    test_list_2 = [1, 0]
    test_list_3 = [97, 98, 99]
    print('{} to {}'.format(test_list_1, merge_sort(test_list_1)))
    print('{} to {}'.format(test_list_2, merge_sort(test_list_2)))
    print('{} to {}'.format(test_list_3, merge_sort(test_list_3)))
