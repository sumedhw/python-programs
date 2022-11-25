# Given an array of positive numbers and a positive number 'k',
#find the maximum sum of any contiguous subarray of size 'k'.

# brute force
# time complexity -> O(N * K)
'''def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0

    for i in range(len(arr) - k + 1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += arr[j]
        
        max_sum = max(window_sum, max_sum)
    
    return max_sum


def main():
    print("Maximum sum of a subarray of size k: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1,3, 2])))
    print("Maximum sum of a subarray of size k: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5 ])))

main()'''


# better approch
# time complexity

def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k -1:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum


def main():
    print("Maximum sum of a subarray of size k: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1,3, 2])))
    print("Maximum sum of a subarray of size k: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5 ])))

main()