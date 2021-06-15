# Leetcode practice
# author: orange
# date: 2021/6/14



class Solution:
    def thousandSeparator(self, n: int) -> str:
        output = ''
        car = n % 10
        if n == 0:
            return '0'
        num_list = []
        while n != 0:
            num_list.append(n%10)
            n = n // 10
        for i in range(len(num_list)):
            if i != 0 and i%3==0:
                output = '.' + output
            output = '{}'.format(num_list[i]) + output
        
        return output

example = Solution()
n = 0
output = example.thousandSeparator(n)
print(output)