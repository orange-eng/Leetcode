
# Leetcode practice
# author: orange
# date: 2021/6/14


# 注意，每增加一位，就是相当于左移一位，扩大二倍

class Solution:
    def prefixesDivBy5(self, nums):
        output = []
        sum  = 0
        for i in range(len(nums)):
            sum = sum*2 + nums[i]       # 每增加一位，相当于sum*2这个很重要
            
            if sum % 5 == 0:
                output.append(True)
            else:
                output.append(False)
        return output

example = Solution()
nums = [1,1,0,0,0,1,0,0,1]
output = example.prefixesDivBy5(nums)
print(output)

