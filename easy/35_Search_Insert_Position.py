# Leetcode practice
# author: orange
# date: 2021/5/27


# 方法一
# 比较简单，设置一个number 用来记录移动的位置即可
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        number = 0
        i= 0
        while i < (len(nums)):
            if target > nums[i]:
                number = number + 1
            i = i + 1
        return number



# 方法二
# 先append然后再sort()，最后用Index()函数找到下标
# class Solution:
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if target in nums:
#             return nums.index(target)
#         else:
#             nums.append(target)
#             nums.sort()
#             return nums.index(target)

example = Solution()
nums = [1,3,5,6]
target = 0


output = example.searchInsert(nums,target)
print(output)
                
