# Leetcode practice
# author: orange
# date: 2021/5/30



# 动态规划
 
#  要考虑第爬到第n阶楼梯时候可能是一步，也可能是两步。 
#  1.计算爬上n-1阶楼梯的方法数量。因为再爬1阶就到第n阶 
#  2.计算爬上n-2阶楼梯体方法数量。因为再爬2阶就到第n阶 那么f(n)=f(n-1)+f(n-2);

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        if (n==1): return 1
        if (n==2): return 2
        a = 1
        b = 2
        temp = 0
        i = 3
        while i <= n:
            temp = a
            a = b
            b = temp + b
            i = i + 1
        return b

example = Solution()
output = example.climbStairs(10)
print(output)