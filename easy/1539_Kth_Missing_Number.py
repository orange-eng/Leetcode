# Leetcode practice
# author: orange
# date: 2021/6/17


# 迭代法即可
# 注意对特殊点的处理

class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        i = 0       # 数组编号
        j = 1       # 固定数
        output = []
        while i < len(arr) and k != 0:
            if arr[i] != j:
                output.append(j)
                j += 1
                k -= 1
            else:       # 如果相等，则都+1
                j += 1
                i += 1
        if k != 0:
            return arr[-1] + k
        else:
            return output[-1]

example = Solution()
arr = [2,3,4,7,11]
k = 2
output = example.findKthPositive(arr,k)
print(output)
        

example = Solution()
arr = [2,3,4,7,11]
k = 5
output = example.findKthPositive(arr,k)