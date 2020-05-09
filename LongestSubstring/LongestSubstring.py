def longestSubstring(input):
    longestSubstring = [0, 1]

    for i in range(1, len(input)):
        odd = getLongestSubstringAt(input, i-1, i+1)
        even = getLongestSubstringAt(input, i-1, i )
        longest = max(odd, even, key= lambda x: x[1]-x[0])
        longestSubstring = max(longest, longestSubstring, key= lambda x: x[1]-x[0])

    return input[longestSubstring[0]: longestSubstring[1]]


def getLongestSubstringAt(input , left, right):

    while left >= 0 and right < len(input):
        if input[left] != input[right]:
            break
        left -= 1
        right += 1

    return [left + 1, right]


print(longestSubstring('paavaanabcdcba'))