# Leetcode practice
# author: orange
# date: 2021/6/1


# //返回某个字母第一次出现的下标

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if len(s) == None and len(t) == None:
            return True
        if len(s) == None or len(t) == None:
            return False
        
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        
        return True

example = Solution()
s = 'asd'
t = 'qwe'
output = example.isIsomorphic(s,t)
print(output)


