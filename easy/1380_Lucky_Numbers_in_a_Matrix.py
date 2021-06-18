
# Leetcode practice
# author: orange
# date: 2021/6/18


# 求转置操作
# T_matrix = zip(*matrix)
# 分别求出每一行的最小值和每一列的最大值
# 然后如果有交集，那么就是该数

class Solution:
    def luckyNumbers (self, matrix):
        m2 = zip(*matrix)
        row_min = [min(i) for i in matrix]  # 每行的最小值
        col_max = [max(i) for i in m2]      # 每列的最大值


        res = [i for i in row_min if i in col_max]
        # 如果同时存在最小值和最大值
        return res

matrix = [[3,7,8],[9,11,13],[15,16,17]]
m2 = zip(*matrix)


for j in m2:
    print(j)

for j in matrix:
    print(j)

# example = Solution()
# output = example.luckyNumbers(matrix)
# print(output)

girl_list= ["美女", "好看的美女", "特别好看的美女"]
girl_set = set(girl_list) #嘿嘿，把list转成set，set就接受一个参数