
# Leetcode practice
# author: orange
# date: 2021/6/2


# 方法1
# 迭代法
# class Solution(object):
#     def reverseString(self, s):
#         """
#         :type s: List[str]
#         :rtype: None Do not return anything, modify s in-place instead.
#         """
#         output = []
#         for i in range(len(s)//2):
#             temp = s[i]
#             s[i] = s[len(s)-1-i]
#             print("s[i]=",s[i])
#             s[len(s)-1-i] = temp
            
#         return s

# 方法2
#双指针法
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return s

example = Solution()

s = ['h','e','l','l']
output = example.reverseString(s)
print(output)