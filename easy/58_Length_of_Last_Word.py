
# Leetcode practice
# author: orange
# date: 2021/5/28



# 方法1
# 使用split函数和remove函数
# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if s == '':
#             return 0
#         else:
#             s = s.split(' ')
#             while '' in s:
#                 s.remove('')
#             if s == []:
#                 return 0
#             else:
#                 return len(s[len(s)-1])
        


# 方法2

# 那么str.strip()就是把这个字符串头和尾的空格，以及位于头尾的\n \t之类给删掉
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip(' ')
        
        s = s.split(' ')
        return len(s[-1])
example = Solution()
s = ' 123'
output = example.lengthOfLastWord(s)
print(output)