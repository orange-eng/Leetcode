
# Leetcode practice
# author: orange
# date: 2021/6/12


class Solution:
    def missingNumber(self, nums):

        if nums == [0]:
            return 1
        if nums[0] != 0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] != 1:
                return nums[i-1] + 1
        return nums[len(nums)-1] + 1
example = Solution()
nums = [1,2]
output = example.missingNumber(nums)
print(output)