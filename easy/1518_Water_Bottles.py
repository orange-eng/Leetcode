
# Leetcode practice
# author: orange
# date: 2021/6/19

# 设置一个空瓶数量
# 一直迭代总数量和空瓶子数量即可

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emptyBottle = numBottles
        while(emptyBottle >= numExchange):  # 设置一个空瓶子数量，然后之一直迭代即可
            numBottles = numBottles + emptyBottle//numExchange
            emptyBottle = emptyBottle//numExchange + emptyBottle%numExchange
        return numBottles

example = Solution()
numBottles = 15
numExchange = 4

output = example.numWaterBottles(numBottles,numExchange)
print(output)