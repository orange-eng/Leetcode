# Leetcode practice
# author: orange
# date: 2021/6/3

# 常规计算即可

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x == y:
            return 0
        res = x ^ y
        number = 0
        while res >= 2:
            if res % 2 == 1:
                number += 1
            res = res // 2
        
        return number+1

example = Solution()

output = example.hammingDistance(1,0)
print(output)