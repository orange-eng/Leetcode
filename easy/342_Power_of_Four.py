
# Leetcode practice
# author: orange
# date: 2021/6/2





# 递归法
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n <= 0:
            return False
        
        if n % 4 == 0:
            return self.isPowerOfFour(n//4)
        return False

example = Solution()

output = example.isPowerOfFour(9)
print(output)