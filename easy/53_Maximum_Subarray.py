# Leetcode practice
# author: orange
# date: 2021/5/28

# 直接替换数组的每一位即可。如果前一位大于0就加，如果小于0则不加。从该位置开始继续加

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #for i,val in enumerate(nums):
        for i in range(1,len(nums)):
            nums[i] = nums[i] + max(nums[i-1],0)
        return max(nums)

example = Solution()
nums = [5,4,-1,7,8]
output = example.maxSubArray(nums)
print(output)