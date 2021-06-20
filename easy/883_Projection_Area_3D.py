
# 迭代法

# class Solution:
#     def projectionArea(self, grid) -> int:
    
#         zero_appear = 0
#         down = len(grid)*len(grid[0])
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == 0:
#                     zero_appear += 1
        
#         left = 0
#         for i in range(len(grid)):
#             left += max(grid[i])
#         grid_T = list(zip(*grid))     # 求转置操作
#         right = 0
#         for i in range(len(grid_T)):
#             right += max(grid_T[i])
#         return down + left + right - zero_appear


# 一行代码
# map是python内置函数，会根据提供的函数对指定的序列做映射。
class Solution:
    def projectionArea(self, grid):
        return sum([sum(map(max, grid)), sum(map(max, zip(*grid))), sum(v > 0 for row in grid for v in row)])

example = Solution()
grid = [[2]]
output = example.projectionArea(grid)
print(output)
