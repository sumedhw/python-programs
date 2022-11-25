# Given an array of positive numbers and a positive number 'S', 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. 
# Return 0, if no such subarray exists.

import math

def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    min_len = math.inf
    window_start = 0

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_len = min(min_len, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    if min_len == math.inf:
        return 0

    return min_len

def main():
    print("Maximum sum of a subarray of size k: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2,3, 2])))
    print("Maximum sum of a subarray of size k: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8 ])))

main()
