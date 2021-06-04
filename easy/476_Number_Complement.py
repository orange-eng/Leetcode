

# Leetcode practice
# author: orange
# date: 2021/6/3


# 传统方法老老实实计算即可

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        total_bit = 0
        original_num = num
        while num >= 2:
            num = num // 2
            total_bit += 1
        total_bit += 1
        print("total_bit=",total_bit)
        total_num = 0
        for i in range(total_bit):
            total_num = total_num + pow(2,i)
        
        return total_num - original_num

example = Solution()
output = example.findComplement(1)
print(output)