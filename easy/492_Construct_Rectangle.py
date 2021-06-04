
# Leetcode practice
# author: orange
# date: 2021/6/4


# 从sqrt(area)向下找即可

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if area == 1:
            return [1,1]
        if area == 2:
            return [2,1]
        
        i = 1
        output = []
        while i * i <= area:
            if area % i == 0:
                output.append([area//i,i])
            i = i + 1
        return output[-1]
        # left = 1
        # right = area
        # if area == 1:
        #     return [1,1]
        # if area == 2:
        #     return [2,1]
        # output = []
        # for i in range(1,area):
        #     #print("right,left:",right,left)
        #     if left * right == area:
        #         output.append([right,left])
        #         if left == right:
        #             return output[-1]
        #         left += 1
        #         right -= 1
        #     elif left * right < area:
                
        #         right = area // left + 1
        #         left += 1
        #     else:
        #         left = area // right - 1
        #         right -= 1
        # return output[-1]

example = Solution()
output = example.constructRectangle(4)
print(output)
