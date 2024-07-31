class Solution:
    def reverse(self, x: int) -> int:

        l = [n for n in str(x)]
        rl = []
        if l[0] == "-":
            rl.append(l[0])
            l = l[1:]

        if len(l) == 1:
            rl.append(l[0])
        else:
            while l[-1] == 0:
                l.pop()

            rl = rl + l[::-1]

        res = int("".join(rl))
        if res >= -(2**31) and res <= 2**31 - 1:
            return res
        else:
            return 0
