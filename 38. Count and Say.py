class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(n)

        def recursive_call(num, start="1"):

            if num == 0:
                return start

            cur = start[0]
            cntr = 1
            i = 0
            res = ""

            while i < len(start) - 1:
                i += 1

                if start[i] == cur:
                    cntr += 1
                else:
                    res += str(cntr) + cur
                    cur = start[i]

                    cntr = 1

            # add last value's encoding
            res += str(cntr) + cur

            return recursive_call(num - 1, res)

        return recursive_call(n - 1, "1")
