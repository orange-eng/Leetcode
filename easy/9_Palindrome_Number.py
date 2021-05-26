# Leetcode practice
# author: orange
# date: 2021/5/26


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        if str_x[0] == '-':
            return False
        flag = 0
        for i in range(len(str_x)):
            if str_x[i] != str_x[len(str_x) - 1 - i]:
                flag = 1
                return False
        return True

example = Solution()
output = example.isPalindrome(121)
print(output)