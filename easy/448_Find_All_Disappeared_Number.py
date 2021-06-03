
# Leetcode practice
# author: orange
# date: 2021/6/3





# 技巧
# 【笔记】将所有正数作为数组下标，置对应数组值为负值。
# 那么，仍为正数的位置即为（未出现过）消失的数字。

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        nums_copy = []
        for i in nums:
            nums_copy.append(i)
        print(nums_copy)
        for i in range(len(nums_copy)):
                nums[nums_copy[i]-1] = -1
        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i+1)
        return output

nums = [4,3,2,7,8,2,3,1]

example = Solution()
output = example.findDisappearedNumbers(nums)

print(output)