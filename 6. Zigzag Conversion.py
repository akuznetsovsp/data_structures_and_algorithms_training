class Solution:
    def convert(self, s: str, numRows: int) -> str:

        i = 0
        rn = 1  # row number
        cond = 1

        m = {}
        for iter in range(1, numRows + 1):
            m[iter] = []

        res = []

        while i < len(s) - 1:

            if rn == numRows and cond == 1:
                m[rn].append(s[i])
                cond = -1
                rn += cond
                i += 1

            elif rn == 1 and cond == -1:
                m[rn].append(s[i])
                cond = 1
                rn += cond
                i += 1

            else:
                m[rn].append(s[i])
                rn += cond
                i += 1

        for row in m:
            res += m[row]

        return "".join(res)


m = {}
for iter in range(1, 3):
    m[iter] = []

m
