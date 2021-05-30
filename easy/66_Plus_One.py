
# Leetcode practice
# author: orange
# date: 2021/5/28

# 从右到左边计算。设置一个进位标记carry，如果carry变成0，说明无需进位，输出结果
# 如果 carry=1一直持续到最后，那么必须要在开头增加[1]才行

class Solution:
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            re = (digits[i] + carry) % 10
            carry = (digits[i] +carry) // 10
            digits[i] = re
            if not carry: return digits
        return [1] + digits

example = Solution()
digits = [9]
output = example.plusOne(digits)
print(output)
                                                                                                                                                                                         