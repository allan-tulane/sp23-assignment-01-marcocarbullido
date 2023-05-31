"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""


# no imports needed.

def foo(x):
    if x == 1:
        return 1
    else:
        return foo(x - 2) + foo(x - 1)


def longest_run(mylist, key):
    current_run_length = 0
    longest_run_length = 0
    for a, b in enumerate(mylist):
        if b == key:
            current_run_length += 1
        else:
            current_run_length = 0
        if current_run_length > longest_run_length:
            longest_run_length = current_run_length
    return longest_run_length


class Result:
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size  # run on left side of input
        self.right_size = right_size  # run on right side of input
        self.longest_size = longest_size  # longest run in input
        self.is_entire_range = is_entire_range  # True if the entire input matches the key

    def __repr__(self):
        return ('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
                (self.longest_size, self.left_size, self.right_size, self.is_entire_range))


def longest_run_recursive(mylist, key):
    def divide_and_conquer(left, right):
        if left == right:
            if mylist[left] == key:
                return Result(1, 1, 1, True)
            else:
                return Result(0, 0, 1, False)

        mid = (left + right) // 2
        left_result = divide_and_conquer(left, mid)
        right_result = divide_and_conquer(mid+1, right)

        # Combine results
        combined_left_size = left_result.left_size
        if left_result.is_entire_range:
            combined_left_size += right_result.left_size

        combined_right_size = right_result.right_size
        if right_result.is_entire_range:
            combined_right_size += left_result.right_size

        combined_longest_size = max(left_result.longest_size, right_result.longest_size, left_result.right_size + right_result.left_size)
        combined_is_entire_range = left_result.is_entire_range and right_result.is_entire_range

        return Result(combined_left_size, combined_right_size, combined_longest_size, combined_is_entire_range)

    if len(mylist) == 0:
        return 0
    return divide_and_conquer(0, len(mylist) - 1).longest_size


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2, 12, 12, 8, 12, 12, 12, 0, 12, 1], 12) == 3
