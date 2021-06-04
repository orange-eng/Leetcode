# Leetcode practice
# author: orange
# date: 2021/6/3


# 技巧题目


'''
n-1个数同时加一，就好比每次有一个数自身减一，因为只能做减法，
所以数组最后的数只能是最小值。
这样的话每个元素减去最小值求其和就是答案。
'''

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_number = min(nums)
        while min_number in nums:
            nums.remove(min_number)
        total_moves = 0
        for i in nums:
            total_moves = total_moves + i - min_number
        return total_moves

example = Solution()

nums = [1,1,1]

output = example.minMoves(nums)
print(output)