


# Leetcode practice
# author: orange
# date: 2021/6/3


# 传统思路即可
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_1 = []
        nums = nums + [0]
        number_1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                number_1 += 1
            else:
                nums_1.append(number_1)
                number_1 = 0
        return (max(nums_1))


example = Solution()

nums = [0]

output = example.findMaxConsecutiveOnes(nums)
print(output)
