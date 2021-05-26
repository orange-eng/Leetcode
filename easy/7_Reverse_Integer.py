# Leetcode practice
# author: orange
# date: 2021/5/26

# 使用整除来求得每一位，存进数组，然后再相乘
# 这里注意，结果不可以超过31位
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = []
        if x < (-2**31) or x > (2**31-1):
            return 0 
        else:
            flag = 0
            if x < 0 :
                x = -x
                flag = 1
            while(x % 10 != x):
                num.append(x%10)
                x = x //10
            num.append(x)
            output = 0
            for i in range(len(num)):
                output = output + num[i] * pow(10,len(num)-i - 1)
            if output < (-2**31) or output > (2**31-1):
                return 0
            else:
                if flag == 0:
                    return output
                else:
                    return -output

example = Solution()
output = example.reverse(1534236469)
print(output) 