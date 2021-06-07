# Leetcode practice
# author: orange
# date: 2021/6/6



# 复杂度为log(m+n)说明大概率是要用二分法查找中间数


# 方法一
# 传统方法

# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         len1 = len(nums1)
#         len2 = len(nums2)
#         i = 0
#         j = 0
#         output = []
#         while i != len1 and j != len2:
#             if nums1[i] <= nums2[j]:
#                 output.append(nums1[i])
#                 i = i + 1
#             else:
#                 output.append(nums2[j])
#                 j = j + 1
        
#         if i == len1:
#             while j != len2:
#                 output.append(nums2[j])
#                 j = j + 1
#         if j == len2:
#             while i != len1:
#                 output.append(nums1[i])
#                 i = i + 1
#         print("output=",output)
#         len_out = len(output)
#         if (len_out/2) % 1 == 0:
#             print('yes')
#             return 0.5 * output[int(len_out//2-1)] + 0.5*output[int(len_out//2)]
#         else:
#             return output[int(len_out//2)]


# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         s = nums1 + nums2
#         s.sort()
#         return (s[int((len(s) - 0.5) / 2)] + s[-int((len(s)+1) / 2) ]) / 2

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        lenA=len(nums1)
        lenB=len(nums2)
        if lenA>lenB:
            nums1,nums2,lenA,lenB=nums2,nums1,lenB,lenA
        imin,imax=0,lenA,
        mid=int((lenA+lenB)/2)
        while imin<=imax:
            i=int((imin+imax)/2)
            j=mid-i
            if i<lenA and nums1[i]<nums2[j-1]:
                imin=i+1
            elif 0<i and nums1[i-1]>nums2[j]:
                imax=i-1
            else:
                if lenA == 0:
                    if (lenA + lenB) % 2 == 0:
                        return (nums2[int(lenB / 2)] + nums2[int(lenB / 2) - 1]) / 2
                    else:
                        return nums2[int(lenB / 2)]
                min_right,max_left=0,0
                if i==0:max_left=nums2[j-1]
                elif j==0:max_left=nums1[i-1]
                else: max_left=max(nums1[i-1],nums2[j-1])
 
                if i==lenA:min_right=nums2[j]
                elif j==lenB:min_right=nums1[i]
                else:min_right=min(nums1[i],nums2[j])
                if (lenA+lenB)%2==0:
                    return (max_left+min_right)/2
                else:
                    return min_right

example = Solution()

nums1 = [1,2]
nums2 = [3,4]

output = example.findMedianSortedArrays(nums1,nums2)
print(output)