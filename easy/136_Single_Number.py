# Leetcode practice
# author: orange
# date: 2021/5/31



# 方法一： 常规方法
# 使用栈的思想和remove（）函数即可

# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         stack = []
#         for i in range(len(nums)):
#             if nums[i] not in stack:
#                 stack.append(nums[i])
#             else:
#                 stack.remove(nums[i])
#         if stack == []:
#             return 
#         else:
#             return stack[0]


# 方法2 异或操作解题
# 将其与0进行异或，两个相同的数字对0进行异或，依然得到0
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a

example = Solution()
nums = [1,2,1,2,3]
output = example.singleNumber(nums)
print(output)