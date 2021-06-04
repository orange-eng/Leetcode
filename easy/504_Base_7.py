
# Leetcode practice
# author: orange
# date: 2021/6/4



# 直接取余数，然后结合栈的思想即可

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        output = ''
        stack = []
        flag = 0
        if num < 0:
            num = - num 
            flag = 1

        while num >= 7:
            stack.append(num % 7)
            num = num // 7
        stack.append(num)
        print("stack=",stack)
        
        for i in range(len(stack)):
            output = output + '{}'.format(stack.pop())
        if flag == 1:
            return '-' + output
        else:
            return output

example = Solution()

output = example.convertToBase7(-8)
print(output)