

# 递归法
# 会超时
# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         if low == high:
#             if low % 2 == 1:
#                 return 1
#             else:
#                 return 0
#         mid = (low + high)//2
#         return self.countOdds(low,mid) + self.countOdds(mid + 1,high)

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return  (high+1)//2 -  low//2
example = Solution()
low = 3
high = 7

output = example.countOdds(low,high)
print(output)
