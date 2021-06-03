# Leetcode practice
# author: orange
# date: 2021/6/2







# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         output = []
#         for i,val in enumerate(nums):
#             if val != 0:
#                 output.append(val)
#         for i in range(len(nums) - len(output)):
#             output.append(0)
#         for i in range(len(nums)):
#             nums[i] = output[i]
#         return nums


# 方法2
# 使用count() remove() append()
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        return nums

example = Solution()

nums = [0,1,0,3,12]
output = example.moveZeroes(nums)
print(output)