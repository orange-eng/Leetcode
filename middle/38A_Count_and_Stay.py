
# Leetcode practice
# author: orange
# date: 2021/6/8





# class Solution:
#     def countAndSay(self, n: int) -> str:
#         output = ''
#         # 返回初始值
#         if n == 1:
#             return '1'
#         elif n > 1:
#             s = self.countAndSay(n-1)
#             t = ""
#             i,j = 0,len(s)
#             count = 1
#             while i <j - 1:
#                 if s[i] == s[j+1]:
#                     count += 1
#                     i += 1
#                 else:
#                     t = t + str(count) + s[i]
#                     count = 1
#                     i += 1
#             t = t + str(count) + s[i]
#             return t

class Solution:
    def countAndSay(self, n: int) -> str:
        """
        迭代方法
        :param n:
        :return:
        执行用时：52 ms, 在所有 Python3 提交中击败了75.93%的用户
        内存消耗：15 MB, 在所有 Python3 提交中击败了5.18%的用户
        """
        s = "1"
        for i in range(n - 1):
            t = ""
            i, j, count = 0, len(s), 1
            while i < j - 1:
                if s[i] == s[i + 1]:
                    count += 1
                    i += 1
                else:
                    t = t + str(count) + s[i]
                    count = 1
                    i += 1
            s = t + str(count) + s[i]
        return s

example = Solution()

output = example.countAndSay(4)
print(output)