

class Solution:
    def maxPower(self, s: str) -> int:
        output = []
        i = 0
        number = 1
        while i != len(s)-1:
            if s[i] == s[i+1]:
                number += 1
            else:
                output.append(number)
                number = 1
            i += 1
        output.append(number)       # 最后一次的计算结果也要算进来
        #print(output)
        return max(output)

example = Solution()

s = 'lll'
output = example.maxPower(s)
print(output)
