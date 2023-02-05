def longest_substring_with_k_distinct(input_str, k):
    window_start = 0
    max_lenght = 0
    char_frequency = {}

    # in this following loop we will try extend the range [windows_start, window_end]
    for window_end in range(len(input_str)):
        right_char = input_str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct characters in the 
        # char_frequency

        while len(char_frequency) > k:
            left_char = input_str[window_start]

            char_frequency[left_char] -= 1

            if char_frequency[left_char] == 0:
                del char_frequency[left_char]

            window_start +=1 # shrink the window

        # remember the maximum length so far
        max_lenght = max(max_lenght, window_end-window_start + 1)

    return max_lenght



def main():
    print("Lenght of the longest substring : " + str(longest_substring_with_k_distinct("araaci",2)))
    print("Lenght of the longest substring : " + str(longest_substring_with_k_distinct("araaci",1)))
    print("Lenght of the longest substring : " + str(longest_substring_with_k_distinct("cbbebi",3)))

main()