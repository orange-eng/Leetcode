# Leetcode practice
# author: orange
# date: 2021/6/17



# 一定是相连的三个数才能够组成最大值

class Solution:
    def largestPerimeter(self, nums) -> int:
        nums.sort()
        for i in range(len(nums)-2):
            a = nums[len(nums)-3-i]
            b = nums[len(nums)-2-i]
            c = nums[len(nums)-1-i]
            if a + b > c:
                return a+b+c
        return 0

example = Solution()
nums = [2,1,2]
output = example.largestPerimeter(nums)
print(output)
