# Leetcode practice
# author: orange
# date: 2021/5/26

# 先转换为字符串，再进行交换，更快一些
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        str_x = str(x)
        x = ''
        if str_x[0] == '-':
            x += '-'
        print("x:",x)
        x += str_x[len(str_x)-1::-1].lstrip("0").rstrip("-")
        x = int(x)
        if -2**31<x<2**31-1:
            return x
        return 0


example = Solution()
output = example.reverse(123)
print(output) 