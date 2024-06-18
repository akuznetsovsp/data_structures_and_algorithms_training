# https://leetcode.com/problems/valid-anagram/description/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def generate_hashmap(string):
            hash = {}

            for letter in string:
                if letter not in hash:
                    hash[letter] = 1
                else:
                    hash[letter] += 1

            return hash

        return generate_hashmap(s) == generate_hashmap(t)
