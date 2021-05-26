# Leetcode practice
# author: orange
# date: 2021/5/26

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)-i - 1):
                if nums[i] + nums[i+j+1] == target:
                    return [i,i+j+1]
                else:
                    j = j +1
            i = i + 1


nums = [2,7,11,15]
target = 26

a = Solution()
result = a.twoSum(nums,target)
print(result)