class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + "(")

            if right < left:
                dfs(left, right + 1, s + ")")

        res = []
        dfs(left=0, right=0, s="")
        return res


x = Solution()
print(x.generateParenthesis(2))


# class Solution:
#     def generateParenthesis(self, n: int) -> list[str]:
#         result = []
#         left = right = 0
#         q = [(left, right, "")]
#         while q:
#             left, right, s = q.pop()
#             if len(s) == 2 * n:
#                 result.append(s)
#             if left < n:
#                 q.append((left + 1, right, s + "("))
#             if right < left:
#                 q.append((left, right + 1, s + ")"))
#         return result
