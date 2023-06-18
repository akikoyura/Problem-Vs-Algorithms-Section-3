def bubble_sort(lst):
    for iteration in range(len(lst)):
        for index in range(1, len(lst)):
            current = lst[index]
            prev = lst[index - 1]

            if prev <= current:
                continue

            lst[index] = prev
            lst[index - 1] = current


def bubble_sort_tuple(tuple):
    for iteration in range(len(tuple)):
        for index in range(1, len(tuple)):
            current = tuple[index]
            prev = tuple[index - 1]

            left_current, right_current = current
            left_prev, right_prev = prev

            if left_current == left_prev:
                if right_current > right_prev:
                    tuple[index] = prev
                    tuple[index - 1] = current
                else:
                    continue

            if left_current > left_prev:
                tuple[index] = prev
                tuple[index - 1] = current

            if left_current < left_prev:
                continue


if __name__ == '__main__':
    wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]
    bubble_sort(wakeup_times)

    print("Pass" if (wakeup_times[0] == 3) else "Fail")

    # Entries are (h, m) where h is the hour and m is the minute
    sleep_times = [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]

    bubble_sort_tuple(sleep_times)
    print(sleep_times)
    print("Pass" if (sleep_times == [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)]) else "Fail")
