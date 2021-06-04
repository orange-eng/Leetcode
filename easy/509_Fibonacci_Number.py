



# Leetcode practice
# author: orange
# date: 2021/6/4


# 常规方法
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        output = [0,1]
        for i in range(2,n+1):
            output.append(output[i-1]+output[i-2])
        
        return output[-1]

example = Solution()
output = example.fib(1)
print(output)

