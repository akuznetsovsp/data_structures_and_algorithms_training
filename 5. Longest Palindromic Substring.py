class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s

        max_str = s[0]

        def expand(s, left, right):

            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left : right + 1]

        for idx, l in enumerate(s):

            even = expand(s, idx, idx + 1)
            odd = expand(s, idx, idx)

            if len(even) > len(max_str):
                max_str = even
            if len(odd) > len(max_str):
                max_str = odd

            # print(max_str)

        return max_str


test = "cbbd"
tester = Solution()
tester.longestPalindrome(test)


def expand(s, left, right):

    while left > 0 and right < len(s) - 1 and s[left] == s[right]:
        print(left, right)
        left -= 1
        right += 1

    print(left, right)
    return s[left + 1 : right]
