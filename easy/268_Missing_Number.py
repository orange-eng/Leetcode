
# Leetcode practice
# author: orange
# date: 2021/6/1



# 方法1
# 求和再相减运算
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number_list = []
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
        all_sum = 0
        for i in range(len(nums) + 1):
            all_sum = all_sum + i
        
        return all_sum - sum



# 方法2
# 使用异或操作来求解缺少项也可以
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            ans = ans ^ ((i+1)^nums[i])
        return ans

example = Solution()
nums = [1]
output = example.missingNumber(nums)
print(output)