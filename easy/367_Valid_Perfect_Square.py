
# Leetcode practice
# author: orange
# date: 2021/6/3

# 牛顿迭代法,公式要记住了

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r > num/r:
            r = (r + num/r)//2
        
        if r*r == num:
            return True
        else:
            return False

example = Solution()

output = example.isPerfectSquare(1)
print(output)
