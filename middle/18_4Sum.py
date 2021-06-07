


# 补: setdefault()函数的用法
'''
setdefault方法用于设置key的默认值。该方法接收两个参数，
第1个参数表示key，第2个参数表示默认值。
如果key在字典中不存在，那么setdefault方法会向字典中添加这个key，
并用第2个参数作为key的值。该方法会返回这个默认值。如果未指定第2个参数，
那么key的默认值是None。如果字典中已经存在这个key，
setdefault不会修改key原来的值，而且该方法会返回key原来的值。
'''
# tuple函数
'''
 tuple()函数用于将列表、区间（range）等转换为元组。

注意：元组和列表非常类似，但列表与元组最大的区别在于：
元组是不可改变的，列表是可改变的。元组支持的操作，列表基本上都支持；
列表支持对元素的修改，而元组则不支持。从这个角度来看，可以认为列表是增强版的元组。

虽然大部分时候都可使用列表来代替元组，但如果程序不需要修改列表所包含的元素，
那么使用元组代替列表会更安全。

'''

# class Solution:
#     def fourSum(self, nums: list, target: int):
#         d = {}
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 d.setdefault(nums[i]+nums[j],[]).append((i,j))
#         #print(d)
#         result = set()
#         #result = []
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for a,b in d.get(target - nums[i] - nums[j],[]):
#                     temp = {i,j,a,b}
#                     print(temp)
#                     if len(temp) == 4:
#                         result.add(tuple(sorted(nums[t] for t in temp)))
#                         #result.append(tuple(sorted(nums[t] for t in temp)))
#         return result

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        ln = len(nums)
        ret = []
        if ln < 4:
            return []
        for i in range(0,ln-3):
            num1 = nums[i]
            for j in range(i+1,ln-2):
                num2 = nums[j]
                left = j + 1
                right = ln - 1
                while left < right:
                    total = num1+num2+nums[left]+nums[right]
                    if total == target:
                        temp = [num1,num2,nums[left],nums[right]]
                        if temp not in ret:
                            ret.append(temp)
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return ret



example = Solution()

nums = [1,0,-1,0,-2,2]
output = example.fourSum(nums,0)
print("output=",output)
            