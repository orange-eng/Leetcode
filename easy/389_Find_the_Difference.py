
# Leetcode practice
# author: orange
# date: 2021/6/3



# 位操作更加简洁
# 凡是找多出来的一个元素，都可以使用位操作来超导
# 因为相同数字的位操作等于0

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = s + ' '
        print(s)
        ans = 0
        if s == '':
            return t[0]
        for i in range(len(s)):
            ans = ans ^ (ord(s[i]) ^ ord(t[i]))
        # if ans == 0:
        #     return t[-1]
        print(chr(ans))
        return (chr(ans + 32))



# 方法2
# 迭代法
# class Solution(object):
#     def findTheDifference(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         t = list(t)
#         if s == '':
#             return t[0]
#         for i in range(len(s)):
#             t.remove(s[i])
#         return t[0]
s = 'ab'
t = 'abc'

example = Solution()
output = example.findTheDifference(s,t)
print(output)