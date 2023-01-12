# Given an array, find the average of all contiguous subarrays of size 'K' in it.
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

# time complexity N*k
def find_averages_of_subarray(k, arr):
    result = []

    for i in range(0,len(arr)):

        for i in range(len(arr)-k+1):
            _sum = 0
            for j in range(i,i+k):
                _sum += arr[j]

            result.append(_sum/k)

    return result

# time complexity O(N)
def find_averages_of_subarray_new(k, arr):
    result = []

    window_sum = 0.0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            result .append(window_sum/k)
            window_sum -= arr[window_end-k+1]

    return result


def main():
    result = find_averages_of_subarray_new(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print(result)

main()
