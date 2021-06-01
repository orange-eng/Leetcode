# Leetcode practice
# author: orange
# date: 2021/5/31

# 找余数即可
#注意一开始,columnnumber-1
#然后创建hash表从0:A开始


class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        dict_my = {0:''}
        res_str = ''
        for i in range(0,26):
            dict_my[i] = chr(ord('A') + i)    #简历一个hash表
        while(columnNumber):
            columnNumber -= 1       #先减去1，再进行去余数计算
            y = columnNumber % 26
            columnNumber = columnNumber // 26
            res_str = dict_my[y] + res_str      #一直都是找余数
        
        return res_str


example = Solution()
column = 27

output = example.convertToTitle(column)
print(output)
