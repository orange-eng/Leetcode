# Leetcode practice
# author: orange
# date: 2021/6/1


# 方法1
# 神技
# X = 100*a + 10*b + c = 99*a + 9*b + (a+b+c)；所以对9取余即可。

# class Solution(object):
#     def addDigits(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         if num == 0:
#             return 0
#         return (num - 1) % 9 + 1


# 方法2
# 迭代法
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num = num // 10 + num % 10
        return num


example = Solution()

output = example.addDigits(11138)
print(output)