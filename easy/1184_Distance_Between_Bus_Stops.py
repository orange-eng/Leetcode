

# Leetcode practice
# author: orange
# date: 2021/6/16

# 遍历法即可


class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        
        total_distance = sum(distance)
        if start == destination:
            return 0
        elif start < destination:
            print("")
        else:
            temp = start
            start = destination
            destination = temp
        output_shun = 0
        for i in range(start,destination):
            output_shun += distance[i]

        output_ni = total_distance - output_shun
        if output_shun >= output_ni:
            return output_ni
        else:
            return output_shun


example = Solution()
distance = [1,2,3,4]
start = 0
destination = 2
output = example.distanceBetweenBusStops(distance,start,destination)
print(output)