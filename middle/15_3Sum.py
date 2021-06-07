
# Leetcode practice
# author: orange
# date: 2021/6/4


# 迭代法 + 双指针即可


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # a+b=-c, target=-c
        nums.sort()
        print(nums)
        N,result = len(nums),[]
        for i in range(N):
            print(nums[i])
            if i > 0 and nums[i] == nums[i-1]:  # 当target与前面相同时，会产生相同的元组
                continue
                
            target = - nums[i]
            s,e = i+1,N-1
            while s<e:  #从两端向中间搜索，直到两个指针相遇
                if nums[s] + nums[e] == target:
                    result.append([nums[i],nums[s],nums[e]])
                    s = s +1
                    while s<e and nums[s] == nums[s-1]: # 若下一个数与前一个相同，就继续找下一个，否则产生相同的元组
                        s = s + 1

                elif nums[s] + nums[e] < target:
                    s = s + 1
                else:
                    e = e - 1
                
        return result

nums = [-1,0,1,2,-1,-4]
example = Solution()
output = example.threeSum(nums)
print(output)

