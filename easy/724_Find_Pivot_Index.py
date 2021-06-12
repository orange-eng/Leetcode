
# Leetcode practice
# author: orange
# date: 2021/6/12


# 设置一个分界线，每次移动一个即可

class Solution:
    def pivotIndex(self, nums):
        a = 0
        b = sum(nums[1:])
        i=0
        while i != len(nums)-1:
            if a == b:
                return i

            a += nums[i]
            b -= nums[i+1]
            i = i + 1
        if a == b:
            return len(nums)-1
        else:
            return -1

example = Solution()
nums = [1,7,3,6,5,6]

output = example.pivotIndex(nums)
print(output)
