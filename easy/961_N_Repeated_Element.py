# Leetcode practice
# author: orange
# date: 2021/6/19



class Solution:
    def repeatedNTimes(self, nums) -> int:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]


example = Solution()
nums = [1,2,3,3]

output = example.repeatedNTimes(nums)
print(output)