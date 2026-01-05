function: finding the longest palindromic substring in a string

do from each center:
```python
def longestPalindromeNaive(s):

    """

    Naive O(n²) approach: expand around each center.

    Useful for comparison.

    """

    if not s:

        return ""

    def expand_around_center(left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]:

            left -= 1

            right += 1

        return right - left - 1

    start, max_len = 0, 0

    for i in range(len(s)):

        # Odd length palindromes (center is a character)

        len1 = expand_around_center(i, i)

        # Even length palindromes (center is between characters)

        len2 = expand_around_center(i, i + 1)

        current_len = max(len1, len2)

        if current_len > max_len:

            max_len = current_len

            start = i - (current_len - 1) // 2

    return s[start:start + max_len]
```