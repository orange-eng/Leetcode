# Leetcode practice
# author: orange
# date: 2021/6/9



# 回溯法

'''
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
'''

class Solution:
    def permute(self, nums):
        res = []
        def backtrack(nums,tmp):
            if not nums:
                res.append(tmp)
                return
            
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:],tmp + [nums[i]])
            
        backtrack(nums,[])

        return res

nums = [1,2,3]

output_1 = [] + [nums[0]] + [2]
print(output_1)

example = Solution()
output = example.permute(nums)
print(output)
        