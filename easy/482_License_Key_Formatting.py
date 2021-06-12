

# Leetcode practice
# author: orange
# date: 2021/6/12




# 反方向一个一个插入即可

class Solution:
    def licenseKeyFormatting(self, s: str, k: int):
        s =s.upper()
        parts =  s.split("-")
        
        sum_str = ''
        for i in range(len(parts)):
            for j in range(len(parts[i])):
                sum_str = sum_str + parts[i][j]

        sum_letter = len(sum_str)

        output = ''
        for i in range(sum_letter):
            if i % k == 0 and i != 0:
                output = '-' + output
            output = sum_str[sum_letter - 1 - i] + output
        return output

example = Solution()

#s = "5F3Z-2e-9-w78"
s = "2-5g-3-J"
output =  example.licenseKeyFormatting(s,2)
print(output)