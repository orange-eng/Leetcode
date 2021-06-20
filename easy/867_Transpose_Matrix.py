# Leetcode practice
# author: orange
# date: 2021/6/20




class Solution:
    def transpose(self, matrix):
        transpose = zip(*matrix)
        transpose = list(transpose)
        output = []
        for i in range(len(transpose)):
            output.append(list(transpose[i]))
        return output

matrix = [[1]]
example = Solution()
output = example.transpose(matrix)
print(output)