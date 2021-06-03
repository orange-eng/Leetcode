
# Leetcode practice
# author: orange
# date: 2021/6/2



# 方法1
# 迭代法
# class Solution(object):
#     def isPowerOfThree(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n <= 0:
#             return False
#         if n == 1:
#             return True
#         while(n % 3 == 0):
#             n = n // 3
#             if n == 1 or n == -1:
#                 return True
#         return False



# 方法2
# 递归法
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            return self.isPowerOfThree(n//3)
        return False

example = Solution()
output = example.isPowerOfThree(27)
print(output)