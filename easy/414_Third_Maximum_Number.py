
# Leetcode practice
# author: orange
# date: 2021/6/3



# 传统迭代法

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max = max(nums)
        if max(nums) == min(nums):
            return _max
        
        
        for _ in range(2):
            a = max(nums)
            while a in nums:
                nums.remove(a)
        if nums == []:
            return _max
        return max(nums)

example = Solution()

nums = [3,2,2,3,2]
output = example.thirdMax(nums)
print(output)