
# Leetcode practice
# author: orange
# date: 2021/6/2


# 方法1
# set集合的用法
'''
a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])
#求两个集合的交集
print(a & b)
print(a and b)
#求两个集合的并集
print(a | b)
print(a or b)
'''
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))



# 方法2
# 传统方法
# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         nums1 = list(set(nums1))
#         nums2 = list(set(nums2))
#         if nums1 == [] or nums2 == []:
#             return []
#         res = []
#         for i in range(len(nums1)):
#             if nums1[i] in nums2:
#                 res.append(nums1[i])
#         return res

example = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
output = example.intersection(nums2,nums1)
print(output)


list1 = [1,2]
list2 = [2]
set1 = {1,2}
set2 = {2}

print(set1 & set2)
#print(list(set(list1) & set(list2)))
