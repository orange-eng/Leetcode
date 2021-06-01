
# Leetcode practice
# author: orange
# date: 2021/5/31

# 方法1
# 动态规划问题
# 注意，不可以使用双循环的方式，因为会超时

# 与上一个题目很相似，但是需要注意，一旦卖出股票之后，紧接着就要准备购买下一批
# 以此需要有一个判断，即卖出之后，立即更新min_Input=prices[i]和max_output = 0

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices) <=1:
#             return 0
#         prices = prices + [-1]
#         min_Input = prices[0]
#         max_Output = 0
#         output = 0
#         for p in range(1,len(prices)):
#             if prices[p] >= prices[p-1]:
#                 min_Input = min(prices[p],min_Input)
#                 max_Output = max(max_Output,prices[p] - min_Input)
#             elif prices[p] < prices[p-1]:
                
#                 output = output + max_Output
#                 # print(output)
#                 min_Input = prices[p]
#                 max_Output = 0
#         return output

# 方法2 贪心算法
# 只要明天的价格比今天高，就在明天卖出股票。但是明天也会再买回股票，以此递推

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <=1:
            return 0
        output = 0
        for i in range(1,len(prices)):
            if prices[i] >prices[i-1]:
                output = output + prices[i] - prices[i-1]
        return output

example = Solution()
princes = [7,1,5,3,6,4]
#princes = [7,1,3,2]
output = example.maxProfit(princes)
print(output)
