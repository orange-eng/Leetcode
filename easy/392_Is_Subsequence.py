
# Leetcode practice
# author: orange
# date: 2021/6/3


'''
#查找
find() 方法检测字符串中是否包含子字符串
inf0 = 'abca'
info.find('a',1)#从1开始查找第一个出现的子串。如果找不到，返回-1
'''
# 使用find函数轻松解题

# class Solution(object):
#     def isSubsequence(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         loc = -1
#         for i in range(len(s)):
#             loc = t.find(s[i],loc+1)
#             if loc == -1:
#                 return False
#         return True



# 双指针方法
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        while(i<len(s) and j<len(t)):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)

example = Solution()

s = 'abc'
t = 'ahbgdc'

output = example.isSubsequence(s,t)
print(output)
