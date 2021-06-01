

# Leetcode practice
# author: orange
# date: 2021/5/31


# 嵌套两个循环即可

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            num_list = [[1],[1,1]]
            for i in range(2,numRows):
                num_line = [1]
                for j in range(1,i):
                    num_line.append(num_list[i-1][j-1]+num_list[i-1][j])
                num_line.append(1)
                num_list.append(num_line)

            return num_list


example = Solution()

num = 5
output = example.generate(num)
print(output)