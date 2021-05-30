# Leetcode practice
# author: orange
# date: 2021/5/30

# 方法1.先变成数值，然后相加，最后处理进位
# class Solution(object):
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         int_a = int(a)
#         int_b = int(b)
#         int_c = int_a + int_b
#         str_c = str(int_c)
        
#         list_c = []
#         for i in range(len(str_c)):
#             list_c.append(int(str_c[i]))
        
#         for i in range(len(list_c)-1,-1,-1):
#             print("i=",i)
#             if i !=0 and list_c[i] >= 2:
#                 list_c[i-1] += 1
#                 list_c[i] = list_c[i] - 2
                
#             if i == 0:
#                 if list_c[0] >= 2:
#                     list_c[0] = list_c[0] - 2
#                     output =  [1] + list_c
#                 elif list_c[0] != 2:
#                     output = list_c
        
#         result = ''
#         for i in range(len(output)):
#             result = result + str(output[i])
#         return result


# 方法二
# 使用内置函数，先将二进制转十进制，10进制加法运算之后转回二进制
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2)+int(b,2))[2:]

example = Solution()
a = '1010'
b = '1011'

output = example.addBinary(a,b)
print(output)
