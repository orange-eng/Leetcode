

# Leetcode practice
# author: orange
# date: 2021/5/31

# 动态规划问题
# 注意，不可以使用双循环的方式，因为会超时
# 动态规划的思想是：
# min_input = min(p,min_input)
# max_output = max(max_input,p - min_input)


# 方法1：双循环（会超时，时间复杂度太高）
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices) == 1 or prices == []:
#             return 0
#         max_price = 0
#         for i in range(len(prices)):
#             for j in range(i,len(prices)):
#                  if prices[j] - prices[i] > max_price:
#                      max_price = prices[j] - prices[i]
#         return max_price

# 方法2： 动态规划法
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1 or prices == []:
            return 0
        
        min_input = prices[0]
        max_profit = 0
        for _,p in enumerate(prices):
            min_input = min(p,min_input)
            max_profit = max(max_profit,p-min_input)
        return max_profit

example = Solution()
princes = [7,1,5,3,6,4]
princes = [7,5,4,3,1,8]
output = example.maxProfit(princes)
print(output)
