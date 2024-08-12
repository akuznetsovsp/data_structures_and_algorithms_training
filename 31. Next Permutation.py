class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return

        r = len(nums) - 1
        found = 0

        while r > 0:
            if nums[r - 1] >= nums[r]:
                r -= 1
            else:
                found = 1
                break

        if not found:
            nums.reverse()
            return

        l = r - 1
        r = len(nums) - 1
        while nums[r] <= nums[l]:
            r -= 1

        nums[r], nums[l] = nums[l], nums[r]

        nums[l + 1 :] = sorted(nums[l + 1 :])

        return
