

# 双flag方法即可
# 如果递增，a=1
# 如果递减，b=1
# 如果a+b=2，说明有问题

class Solution:
    def isMonotonic(self, nums) -> bool:
        if len(nums) <= 2:
            return True
        i = 0
        a = 0    # 1代表递增
        b = 0
        while i != len(nums)-1:
            if nums[i] < nums[i+1]:
                a = 1
            elif nums[i] > nums[i+1]:
                b = 1
            i += 1    
        if a+b ==2:
            return False
        else:
            return True

        

example = Solution()
nums = [1,2,3,2]
output = example.isMonotonic(nums)
print(output)