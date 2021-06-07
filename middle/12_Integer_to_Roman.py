
# Leetcode practice
# author: orange
# date: 2021/6/4


# 从大到小，建立两个列表，设置明显的分割线
# 然后依次便利所有的13中特殊情况，如果大于该项，就减去
# 继续判断即可

class Solution:
    def intToRoman(self, num: int) -> str:
        values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]   # 明显的分割线
        reps=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        res = ''
        for i in range(13):
            while num >= values[i]:
                num -= values[i]
                res += reps[i]
        return res

example = Solution()

nums = 4

output = example.intToRoman(nums)
print(output)