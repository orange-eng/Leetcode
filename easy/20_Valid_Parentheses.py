
# Leetcode practice
# author: orange
# date: 2021/5/27

# 寻找匹配项。如果有，则将其删除，并继续判断


class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}',"")
            s = s.replace("[]",'')
            s = s.replace('()','')
        return s == ''
example = Solution()
strs = '()[][]'
output = example.isValid(strs)
print(output)