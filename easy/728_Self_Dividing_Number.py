
# Leetcode practice
# author: orange
# date: 2021/6/23




# class Solution:
#     def selfDividingNumbers(self, left, right):
#         output = []
#         for i in range(left,right+1):
#             #print(i)
#             carry = 0
#             number = i 
#             num_list = []
#             while number >= 10:
#                 carry = i%10
#                 number = i//10
#                 num_list.append(carry)

#             num_list.append(number)
#             #print("num_list=",num_list)
#             flag = 0
#             for _,key in enumerate(num_list):
#                 if key == 0:
#                     flag = 1
#                 elif i % key != 0:
#                     flag = 1
            
#             if flag == 0:
#                 output.append(i)
#         return output

class Solution:
    def selfDividingNumbers(self, left, right):
        result = []
        for i in range(left,right+1):
            if '0' in str(i):
                continue
            for num in str(i):
                if i % int(num) != 0:
                    break
            else:
                result.append(i)
        return result



example = Solution()
left = 1
right = 1
output = example.selfDividingNumbers(left,right)
print(output)