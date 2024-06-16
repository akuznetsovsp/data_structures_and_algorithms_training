# https://leetcode.com/problems/valid-palindrome/description/


# First solution O(n):
class Solution:
    def isPalindrome(self, s: str) -> bool:

        string_list = []
        for letter in [let for let in s]:
            if letter.isalnum():
                string_list.append(letter)

        string = "".join(string_list).lower()

        len_string = len(string)

        stopping_idx = len_string // 2
        print(f"Stopping idx = {stopping_idx}")
        print(len_string)
        print(string)

        for idx, l in enumerate(string):
            print(f"")
            if idx > stopping_idx:
                return True
            if l != string[len_string - idx - 1]:
                return False

        return True
