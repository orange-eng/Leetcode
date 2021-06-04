
# Leetcode practice
# author: orange
# date: 2021/6/4


import math 

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        sum = 1
        for i in range(2,int(math.sqrt(num)+1)):
            if num % i == 0:
                sum += i
                sum += num//i
        
        return sum == num

example = Solution()

output = example.checkPerfectNumber(8128)
print(output)