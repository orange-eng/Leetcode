

# insert函数用于插入
# pop 函数用于删除

class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        sum = len(arr)
        i = 0
        while i < sum:
            if arr[i] == 0:
                arr.insert(i+1,0)
                i = i + 1
                arr.pop()
            i = i+1
        return arr

exmaple = Solution()
arr = [1,0,1]
output = exmaple.duplicateZeros(arr)
print(output)
