
# Leetcode practice
# author: orange
# date: 2021/6/14


# 栈方法
# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         stack = []
#         for e in s:
#             if stack and stack[-1]==e:
#                 stack.pop()
#             else:
#                 stack.append(e)
#         return "".join(stack)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            #print(stack)
            if stack != [] and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        s = "".join(stack)
        return s

example = Solution()
s = "aababaab"
output = example.removeDuplicates(s)
print("output=",output)