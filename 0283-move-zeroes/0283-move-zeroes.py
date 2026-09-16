class Solution:
    def moveZeroes(self, nums):
        i = 0

        for number in nums:
            if number != 0:
                nums[i] = number
                i += 1

        while i < len(nums):
            nums[i] = 0
            i += 1