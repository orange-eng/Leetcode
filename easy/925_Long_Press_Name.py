
# Leetcode practice
# author: orange
# date: 2021/6/13


# 双指针方法

# class Solution:
#     def isLongPressedName(self, name: str, typed: str) -> bool:
#         name = list(name)
#         typed = list(typed)
#         i = 0
#         j = 0
#         if name[i] != typed[j]:
#             return False

#         while i != len(name):
#             if name[i] == typed[j]:
#                 i += 1
#                 j += 1
#             else:
#                 if typed[j] == typed[j-1]:
#                     j += 1
#                 else:
#                     return False
#             if j == len(typed) and i != len(name):
#                 return False
#         while j != len(typed):
#             if typed[j] == typed[j-1]:
#                 j += 1
#             else:
#                 return False
#         return True


# 栈方法
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name = list(name)
        typed = list(typed)
        while name:
            c = name.pop()
            if not typed or typed.pop() != c:
                return False
            if not name or name[-1] != c:
                while typed and typed[-1] == c:
                    typed.pop()
        return not typed

example = Solution()
name = "zlexya"

typed = "aazlllllllllllllleexxxxxxxxxxxxxxxya"
output = example.isLongPressedName(name,typed)

print(output)
