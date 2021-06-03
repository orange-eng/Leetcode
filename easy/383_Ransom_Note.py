

# Leetcode practice
# author: orange
# date: 2021/6/3


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom = list(ransomNote)
        maga = list(magazine)
        try:
            for i in ransom:
                maga.remove(i)
            return True
        except:
            return False

example = Solution()
ransomNote = 'aa'
magazine = 'aab'
output = example.canConstruct(ransomNote,magazine)
print(output)
