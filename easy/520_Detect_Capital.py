# Leetcode practice
# author: orange
# date: 2021/6/4



# 传统方法

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        if len(word) == 2:
            if 'a'<= word[0] <= 'z' and 'A'<= word[1] <= 'Z':
                return False
            else:
                return True

        for i in range(1,len(word)):
            if 'A' <= word[0] <= 'Z':
                if  'a'<= word[1] <= 'z':
                    if 'a' > word[i] or  word[i]> 'z':
                        return False
                if 'A' <= word[1] <= 'Z':
                    if 'A' > word[i] or word[i] > 'Z':
                        return False
            if 'a' <= word[0] <= 'z':
                if 'a' > word[i] or  word[i]> 'z':
                    return False
        
        return True

# 也可以先统计大小写字母的个数，然后分类讨论

example = Solution()
word = 'aAG'
output = example.detectCapitalUse(word)
print(output)
