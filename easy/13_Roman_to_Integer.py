# Leetcode practice
# author: orange
# date: 2021/5/26


# 方法一
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = map[s[0]]
        for i in range(len(s)):
            if i != len(s)-1:
                if map[s[i]] >= map[s[i+1]]:
                    num = num + map[s[i+1]]
                else:
                    num = num + map[s[i+1]] - 2*map[s[i]]
            else:
                return num

# 方法二
# class Solution:
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}        
#         ans=0        
#         for i in range(len(s)):            
#             if i<len(s)-1 and a[s[i]]<a[s[i+1]]:                
#                 ans-=a[s[i]]
#             else:
#                 ans+=a[s[i]]
#         return ans


example = Solution()
output = example.romanToInt('MCMXCIV')
print(output)