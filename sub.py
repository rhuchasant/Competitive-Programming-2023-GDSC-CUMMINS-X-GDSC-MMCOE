def length_of_longest_substring(s):
    # Initialize a dictionary to store the last seen index of each character
    char_index = {}
    max_length = 0  # Initialize the maximum length
    start = 0  # Initialize the starting index of the substring

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            # If the character is seen again within the current substring, update the start index
            start = char_index[s[end]] + 1

        char_index[s[end]] = end  # Update the last seen index of the character
        max_length = max(max_length, end - start + 1)  # Update the maximum length

    return max_length

# Example usage:
s1 = "abcabcbb"
print(length_of_longest_substring(s1))  # Output: 3

s2 = "bbbbb"
print(length_of_longest_substring(s2))  # Output: 1

s3 = "pwwkew"
print(length_of_longest_substring(s3))  # Output: 3


