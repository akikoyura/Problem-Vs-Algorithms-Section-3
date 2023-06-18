def design_quicksort(arr):
    # select the last element as the pivot
    pivot_idx = len(items) - 1

    pivot_value = items[pivot_idx]

    left_idx = 0
    while pivot_value != left_idx:
        item = items[left_idx]

        if item <= pivot_value:
            left_idx += 1
            continue

        # Place the item before the pivot at left_idx
        items[left_idx] = items[pivot_idx - 1]

        # Shift pivot one to the left
        items[pivot_idx - 1] = pivot_value

        # Place item at pivot's previous location
        items[pivot_idx] = item

        # Update pivot_idx
        pivot_idx -= 1

    print(items)  # [0,1,2,7,3,10,8]


def sort_a_little_bit(items):
    left_idx = 0
    pivot_idx = len(items) - 1
    pivot_value = items[pivot_idx]

    while pivot_idx != left_idx:

        item = items[left_idx]
        if item <= pivot_value:
            left_idx += 1
            continue

        items[left_idx] = items[pivot_idx - 1]
        items[pivot_idx - 1] = pivot_value
        items[pivot_idx] = item

        pivot_idx -= 1


def sort_a_little_bit_v1(items, start_idx, end_idx):
    left_idx = 0
    pivot_idx = end_idx
    pivot_value = items[pivot_idx]

    while pivot_idx != left_idx:
        item = items[left_idx]
        if item <= pivot_value:
            left_idx += 1
            continue
        items[left_idx] = items[pivot_idx - 1]
        items[pivot_idx - 1] = pivot_value
        items[pivot_idx] = item

        pivot_idx -= 1
    return pivot_idx


def sort_all(items, begin_idx, end_idx):
    if begin_idx >= end_idx:
        return

    pivot_idx = sort_a_little_bit_v1(items, begin_idx, end_idx)
    sort_all(items, begin_idx, pivot_idx - 1)
    sort_all(items, pivot_idx + 1, end_idx)


def quick_sort(items):
    sort_all(items, 0, len(items) - 1)


if __name__ == '__main__':
    items = [8, 3, 1, 7, 0, 10, 2]
    design_quicksort(items)

    items_1 = [8, 3, 1, 7, 0, 10, 2]
    sort_a_little_bit(items_1)
    print(items_1)

    items_2 = [8, 3, 1, 7, 0, 10, 2]
    pivot_idx = sort_a_little_bit_v1(items_2, 0, len(items_2) - 1)
    print(items_2)
    print('pivot index %d' % pivot_idx)

    items_3 = [8, 3, 1, 7, 0, 10, 2]
    quick_sort(items_3)
    print(items_3)

    items = [1, 0]
    quick_sort(items)
    print(items)
