"""
Problem Statement
Writes a function that takes an input array (or Python list) consisting of only 0s, 1s, and 2s, and sorts that array in a single traversal.

Note that if you can get the function to put the 0s and 2s in the correct positions,
 this will automatically cause the 1s to be in the correct positions as well.
"""


def sort_012(input_list):
    next_position_0 = 0
    next_position_2 = len(input_list) - 1

    front_idx = 0

    while front_idx <= next_position_2:
        if input_list[front_idx] == 0:
            input_list[front_idx] = input_list[next_position_0]
            input_list[next_position_0] = 0
            next_position_0 += 1
            front_idx += 1

        elif input_list[front_idx] == 2:
            input_list[front_idx] = input_list[next_position_2]
            input_list[next_position_2] = 2
            next_position_2 -= 1
        else:
            front_idx += 1


def test_function(test_case):
    sort_012(test_case)
    print(test_case)

    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_case = [0, 0, 2, 2, 2, 1, 1, 1, 1, 2, 0, 2]
    test_function(test_case)

    test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
    test_function(test_case)

    test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
    test_function(test_case)
