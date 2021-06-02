
# Leetcode practice
# author: orange
# date: 2021/6/1


# 递归法
# 先一直除2，再一直除3，再一直除5
# 最后结果为0就为false，结果为1就为true

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return self.isUgly(n//2)
        elif n % 3 == 0:
            return self.isUgly(n//3)
        elif n % 5 == 0:
            return self.isUgly(n//5)
        return False

example = Solution()

output = example.isUgly(14)
print(output)
        
