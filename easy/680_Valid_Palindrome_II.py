
# Leetcode practice
# author: orange
# date: 2021/6/13


# Loser

# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         if len(s) == 1:
#             return True

#         low = 0
#         flag = 0
#         high = len(s) - 1
#         while low != high:
#             if s[low] == s[high]:
#                 low += 1
#                 if low == high:
#                     return True
#                 high -= 1
#             else:
#                 if s[low+1] == s[high] and flag==0:
#                     low += 1
#                     flag = 1
#                 elif s[high-1] == s[low] and flag==0:
#                     high -= 1
#                     flag = 1
#                 else:
#                     return False
#         return True

# 双指针
# 当遇到不一样的位置时，应该如何处理，值得思考

class Solution:
    def validPalindrome(self, s):
        if s == s[::-1]:        # s[::-1]代表整个列表的相反列表
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                a = s[l + 1 : r + 1]    
                b = s[l:r]
                # 删除之后，再次观察a和b是否对称
                return a == a[::-1] or b==b[::-1]


example = Solution()
s = "abde"
output = example.validPalindrome(s)
print(output)

nums = [1,2,3,4]
print(nums[0:3])