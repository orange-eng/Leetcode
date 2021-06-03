
# Leetcode practice
# author: orange
# date: 2021/6/2


# 常规方法即可

# class Solution(object):
#     def countBits(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """

#         def num2bit(number):
#             sum_2 = 0
#             while(number >= 2):
#                 if number % 2 == 1:
#                     sum_2 += 1
#                 number = number // 2
#             if number == 1:
#                 sum_2 += 1
#             return sum_2
#         output = []
#         for i in range(n+1):
#             output.append(num2bit(i))
        
#         return output



# 方法2
'''
        由上可见：
        1、如果 i 为偶数，那么f(i) = f(i/2) ,因为 i/2 本质上是i的二进制左移一位，低位补零，所以1的数量不变。
        2、如果 i 为奇数，那么f(i) = f(i - 1) + 1， 因为如果i为奇数，那么 i - 1必定为偶数，而偶数的二进制最低位一定是0，
        那么该偶数 +1 后最低位变为1且不会进位，所以奇数比它上一个偶数bit上多一个1，即 f(i) = f(i - 1) + 1。
        :type num: int

'''
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        output = [0,1]
        for i in range(2,n+1):
            if i % 2 == 0:
                output.append(output[i//2])
            else:
                output.append(output[i//2] + 1)
        
        return output

example = Solution()

outout = example.countBits(5)
print(outout)
