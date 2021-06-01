
# Leetcode practice
# author: orange
# date: 2021/5/31




# 方法1： 强行计算

# class Solution(object):
#     def trailingZeroes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 0:
#             return 0
#         sum = 1
#         for i in range(n):
#             sum = sum *(i+1)
#         number_zero = 0
#         while sum % 10 == 0:
#             sum = sum // 10
#             number_zero += 1
#         return number_zero


# 方法2
'''
不断除以 5, 是因为每间隔 5 个数有一个数可以被 5 整除, 
然后在这些可被 5 整除的数中, 每间隔 5 个数又有一个可以被 25 整除, 
故要再除一次, ... 直到结果为 0, 表示没有能继续被 5 整除的数了.
'''
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        while(n//5 != 0):
            count = count + n//5
            n = n //5
        return count



example = Solution()
output = example.trailingZeroes(125)
print(output)