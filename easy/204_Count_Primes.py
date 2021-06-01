
# Leetcode practice
# author: orange
# date: 2021/6/1



'''
这题搜到一个非常牛逼的算法,叫做厄拉多塞筛法. 
比如说求20以内质数的个数,首先0,1不是质数.2是第一个质数,然后把20以内所有2的倍数划去.
2后面紧跟的数即为下一个质数3,然后把3所有的倍数划去.3后面紧跟的数即为下一个质数5,
再把5所有的倍数划去.以此类推.
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        output_list = [1]*n
        output_list[0],output_list[1] = 0,0

        
        for i in range(2,int(n**0.5+1)):
            #print(output_list[i*i:n:i])
            if output_list[i] == 1:
                output_list[i*i:n:i] = [0] * len(output_list[i*i:n:i])
            #     print(output_list)
        #print(output_list)
        return sum(output_list)

example = Solution()
output = example.countPrimes(10)
print(output)