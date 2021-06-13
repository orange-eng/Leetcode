# Leetcode practice
# author: orange
# date: 2021/6/13

# 先计算左边，再计算右边，最后排除特殊情况即可

class Solution:
    def validMountainArray(self, arr) -> bool:
        l,r=0,len(arr)-1
        while l<r and arr[l]<arr[l+1]: l+=1 # 先算左边的

        while r>l and arr[r]<arr[r-1]: r-=1 # 再算右边的
        return l==r and l!=0 and r!=len(arr)-1  # 排除特殊情况即可

example = Solution()
arr = [3,5,5]
output = example.validMountainArray(arr)
print(output)
         