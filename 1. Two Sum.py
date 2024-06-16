# https://leetcode.com/problems/two-sum/description/


# Brute force - O(n2):
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_idx, first_num in enumerate(nums[:-1]):
            # print(f'first_num = {first_num}, idx = {first_idx}')
            for second_idx, second_num in enumerate(
                nums[first_idx + 1 :], start=first_idx + 1
            ):
                # print(f'second_num = {second_num}, idx = {second_idx}')
                if first_num + second_num == target:
                    return [first_idx, second_idx]


# Hash map - O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for idx, num in enumerate(nums):
            if num not in hashmap:
                hashmap[target - num] = idx
                # print(print(target - num, hashmap[target - num]))
            else:
                # print(idx)
                return [hashmap[num], idx]
