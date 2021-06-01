
# Leetcode practice
# author: orange
# date: 2021/5/31



from typing import Hashable


# 方法1 Hash map
# class Solution(object):
#     def titleToNumber(self, columnTitle):
#         """
#         :type columnTitle: str
#         :rtype: int
#         """
#         output=0
#         Hash_map = {}
#         for i in range(26):
#            Hash_map[chr(ord('A')+i)] = i+1
#         print(Hash_map)
#         for i in range(len(columnTitle)):
#             output = output + Hash_map[columnTitle[len(columnTitle)-1-i]] * pow(26,i)
#         return output


# 方法2 直接算
class Solution(object):
    def titleToNumber(self, s):
        #26进制转10进制
        ans = 0
        for x in s:
            ans *= 26
            ans += ord(x)-ord('A')+1
        return ans

example = Solution()

column = 'FXSHRXW'
output = example.titleToNumber(column)
print(output)
        