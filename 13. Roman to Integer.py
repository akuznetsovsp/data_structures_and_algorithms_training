class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0
        i = 0

        while i < len(s):

            if i < len(s) - 1 and s[i] == "I" and (s[i + 1] in ("V", "X")):
                res -= d[s[i]]
            elif i < len(s) - 1 and s[i] == "X" and (s[i + 1] in ("L", "C")):
                res -= d[s[i]]
            elif i < len(s) - 1 and s[i] == "C" and (s[i + 1] in ("D", "M")):
                res -= d[s[i]]
            else:
                res += d[s[i]]

            i += 1

        return res
