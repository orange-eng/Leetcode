
# Leetcode practice
# author: orange
# date: 2021/6/16


# 三指针法，左中右三个位置卡好即可

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left,mid,right = 0,k,2*k    # 三指针方法
        output = ''
        while len(output) < len(s):
            output = output + s[left:mid][::-1] + s[mid:right]
            left,mid,right = left + 2*k,mid + 2*k, right + 2*k
        return output

example = Solution()

s = "abcdefg"
k = 2

output = example.reverseStr(s,k)
print(output)


exam_list = [1,2,3,4,5]
print(exam_list[1:10])