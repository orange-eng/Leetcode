# Leetcode practice
# author: orange
# date: 2021/5/30

# class Solution(object):
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         a = 0
        
#         if x <= 1:
#             return x
#         for i in range(1,x//2+2):
#             if i <= x/i and (i+1) > x/(i+1):
#                 a = i
#         return a


# 牛顿迭代法
#y^2 = x
#迭代公式为yn+1 = yn -(yn^2 - x)/(2yn)

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        r = x
        while r > x / r:                # 设置好临界条件
            r = (r + x / r) // 2        # 根据牛顿迭代法求出递推公式
            # r = (2*r + x/(r*r))//3
        return int(r)


example = Solution()
output = example.mySqrt(27)
print(output) 