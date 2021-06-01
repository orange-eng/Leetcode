
# Leetcode practice
# author: orange
# date: 2021/5/31



# 使用双指针
# 数组本身就是有顺序的，以此可以两个指针从两边移动

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while(left != right):
            if numbers[left] + numbers[right] == target:
                return [left+1,right + 1]
            elif numbers[left] + numbers[right] < target:
                left = left +1
            else:
                right = right - 1

numbers = [2,7,11,15]
target = 13

example = Solution()
output = example.twoSum(numbers,target)
print(output)
