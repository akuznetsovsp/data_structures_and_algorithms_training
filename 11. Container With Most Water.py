# # brute force
# class Solution:
#     def maxArea(self, height: List[int]) -> int:

#         res = 0

#         for i, first in enumerate(height[:-1]):
#             for j, last in enumerate(height[i + 1 :]):

#                 h = min([first, last])
#                 w = j + 1
#                 if h * w > res:
#                     res = h * w

#                 # print(i, j, first, last, res)

#         return res


# optimized
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0

        while l <= r:
            if min([height[l], height[r]]) * (r - l) > res:
                res = min([height[l], height[r]]) * (r - l)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return res
