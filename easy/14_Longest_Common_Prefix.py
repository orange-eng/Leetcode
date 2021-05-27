# Leetcode practice
# author: orange
# date: 2021/5/27

# 使用字符串的ASCII值来进行比较，十分方便的方法

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str_max = max(strs)
        str_min = min(strs)
        for i,x in enumerate(str_min):      #要以最小的为基础，去匹配最大的
            if x != str_max[i]:
                return str_max[:i]
        return str_min



strs = ["flow","12flower"]
example = Solution()
output = example.longestCommonPrefix(strs)
print(output)

"""
    字符串的比较操作：
        运算符：>,>=,<,<=,==,!=
        比较规则:首先比较两个字符串中的第- -个字符，如果相等则继续比较下一个字符，依次比较下去，直到两个字符串中的字符不相等时，
        其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再被比较
        比较原理:两字符进行比较时，比较的是其ordinal value(原始值),调用内置函数ord可以得到指定字符的ordinal value（ASCII码）。
        与内置函数ord对应的是内置函数chr,调用内置函数chr时指定ordinal value可以得到其对应的字符
    == 与 is 的区别：
        == 比较的是value
        is 比较的是id

"""

# print("hello" > "hel")
# print("hello" > "interest")
# # 第二个，解释：
# print(ord("he"), ord("h"))  # 104<145

