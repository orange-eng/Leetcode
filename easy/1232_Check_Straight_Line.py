

from typing import Coroutine


class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        if len(coordinates) == 2:
            return True
        flag = 1
        constant = coordinates[0][0]
        for i in range(1,len(coordinates)):
            if coordinates[i][0] != constant:
                continue
            else:
                flag = 0
                break
        if flag == 0:
            for i in range(len(coordinates)):
                if coordinates[i][0] != constant:
                    return False
            return True
        else:
            k = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
            for i in range(2,len(coordinates)):
                if coordinates[i][1] - coordinates[0][1] != k*(coordinates[i][0] - coordinates[0][0]):
                    return False
            return True


example = Solution()
#coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,6]]
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
output = example.checkStraightLine(coordinates)
print(output)
