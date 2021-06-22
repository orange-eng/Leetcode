# Leetcode practice
# author: orange
# date: 2021/6/22

# 使用set()集合，可以比大小的方式来判断包含关系
# 超级方便


class Solution:
    def findWords(self, words):
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        res = []
        for i in words:
            x = i.lower()
            setx = set(x)
            if setx<=set1 or setx<=set2 or setx<=set3:
                res.append(i)
               
        return res

example = Solution()
#words = ["Hello","Alaska","Dad","Peace"]
words = ["adsdf","sfd"]
output = example.findWords(words)
print(output)

set1 = set('qwertyuiop')
print("set1=",set1)

print({1, 2} >= {1,2})  # True