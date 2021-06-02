

# Leetcode practice
# author: orange
# date: 2021/6/1


# 方法1
# 传统方法（超时了）

# class Solution(object):
#     def nthUglyNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 1:
#             return 1
#         digit_sum = [1]
#         i = 1
#         while len(digit_sum) <= n-1:
#             i = i + 1
#             if self.UglyNumber(i):
#                 digit_sum.append(i)
                
#         print(digit_sum)
#         return digit_sum[-1]
#     def UglyNumber(self,num):
#         if num == 1:
#             return True
#         if num % 2 == 0:
#             return self.UglyNumber(num // 2)
#         if num % 3 == 0:
#             return self.UglyNumber(num // 3)
#         if num % 5 == 0:
#             return self.UglyNumber(num // 5)
#         return False


# 方法2
# 三指针方法（学到了）
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        idx2 = 0
        idx3 = 0
        idx5 = 0
        for i in range(n-1):
            res.append(min(res[idx2]*2,res[idx3]*3,res[idx5]*5))
            if res[-1] == res[idx2]*2:
                idx2 += 1
            if res[-1] == res[idx3]*3:
                idx3 += 1
            if res[-1] == res[idx5]*5:
                idx5 += 1
        return res[-1]

example = Solution()
output = example.nthUglyNumber(10)
print(output)