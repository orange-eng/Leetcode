


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()   # 字母变为小写
        output = []
        for i in range(len(s)):
            if (s[i] >= 'a' and s[i] <= 'z')or (s[i] >= '0' and s[i] <= '9'):
                output.append(s[i])
        print(output)
        if output == []:
            return True
        else:
            flag = 1
            for i in range(len(output)//2 + 1):
                if output[i] != output[len(output)-1-i]:
                    return False
                    
            return True

example = Solution()
#s = "A man, a plan, a canal: Panama"
s = "0p"
output = example.isPalindrome(s)
print(output)