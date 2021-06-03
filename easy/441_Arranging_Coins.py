

# Leetcode practice
# author: orange
# date: 2021/6/3



# 方法1
# 迭代法
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        i = 1
        while n >= i:
            n = n - i
            i = i + 1
        return i -1


# 方法2
# 求解方程组
'''
其实就是初中数学，解一元二次方程。
1+2+...+k=n，转换成高斯公式就变成了 k×(k+1)/2=n，
求出未知数 k 以后，返回不超过 k 的最大整数就 OK 了。
'''

example = Solution()

output = example.arrangeCoins(3)
print(output)