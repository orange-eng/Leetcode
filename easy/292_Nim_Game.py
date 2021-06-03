
# Leetcode practice
# author: orange
# date: 2021/6/2

# 是4的倍数就一定就会输



class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 3:
            return True
        if n % 4 == 0:
            return False
        return True

example = Solution()
output = example.canWinNim(5)
print(output)