
# Leetcode practice
# author: orange
# date: 2021/6/13

class Solution:
    def isBoomerang(self, points) -> bool:
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        y1 = (points[0][1] - points[1][1])
        x1 = (points[0][0] - points[1][0])
        y2 = (points[0][1] - points[2][1])
        x2 = (points[0][0] - points[2][0])
        if x1 == 0 and x2 == 0:
            return False
        elif x1 == 0 and x2 != 0:
            return True
        elif x1 != 0 and x2 == 0:
            return True
        

        if y1/x1 == y2/x2:
            return False
        else:
            return True

example = Solution()
points = [[0,1],[0,1],[2,1]]
output = example.isBoomerang(points)
print(output)
