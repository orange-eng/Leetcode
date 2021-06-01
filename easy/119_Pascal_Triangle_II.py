
# Leetcode practice
# author: orange
# date: 2021/5/31


# 嵌套两个循环即可

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        if rowIndex == 0 :
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            rowIndex = rowIndex + 1
            num_list = [[1],[1,1]]
            for i in range(2,rowIndex):
                num_line = [1]
                for j in range(1,i):
                    num_line.append(num_list[i-1][j-1]+num_list[i-1][j])
                num_line.append(1)
                num_list.append(num_line)
            return num_list[-1]

example = Solution()
rowIndex = 2

output = example.getRow(rowIndex)
print(output)
