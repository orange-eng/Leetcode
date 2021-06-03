
# Leetcode practice
# author: orange
# date: 2021/6/2




# 使用index()函数解题比较方便

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pi = []
        si = []
        for v in pattern:
            pi.append(pattern.index(v)) # 第一次出现的下标
            
        ss = s.split(' ')
        for v in ss:
            si.append(ss.index(v))
        print(si)
        print(pi)
        if si == pi:
            return True
        else:
            return False

example = Solution()

mask = 'abba'
s = 'dog cat cat do'

output = example.wordPattern(mask,s)
print(output)