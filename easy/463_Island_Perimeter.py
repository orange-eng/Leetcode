# Leetcode practice
# author: orange
# date: 2021/6/17

# 双遍历即可
# 遇到1，则+4
# 如果左边相邻，-2
# 如果上面相邻，-2


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans += 4
                    if i > 0:
                        ans -= 2*grid[i-1][j]
                    if j > 0:
                        ans -= 2*grid[i][j-1]
        return ans

example = Solution()
#grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
grid = [[1,0]]
output = example.islandPerimeter(grid)
print(output)
