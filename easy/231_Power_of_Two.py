
# Leetcode practice
# author: orange
# date: 2021/6/1





# 方法1：常规方法
# class Solution(object):
#     def isPowerOfTwo(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n == 1:
#             return True
#         if n == 0:
#             return False
#         while n % 2 == 0:
#             n = n // 2
#             if n == 1:
#                 return True
#         return False


# 方法2
# 使用位运算即可。(n & (n-1)) = 0代表是2的幂次方
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & (n - 1))


example = Solution()

n = 3
output = example.isPowerOfTwo(n)
print(output)