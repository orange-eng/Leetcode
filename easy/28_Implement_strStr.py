
# Leetcode practice
# author: orange
# date: 2021/5/27


# 使用index()函数可以直接找到下标。
# 注意try: except函数用于处理异常事件
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except:
            return -1

example = Solution()
haystack = 'hello'
needle = 'll'
output = example.strStr(haystack,needle)
print(output)