# Leetcode practice
# author: orange
# date: 2021/6/3


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        for i in range(1,n+1):
            if i % 3 == 0:
                if i % 5 != 0:
                    output.append("Fizz")
                else:
                    output.append("FizzBuzz")
            elif i % 5 == 0:
                if i % 3 != 0 :
                    output.append("Buzz")
                else:
                    output.append("FizzBuzz")
            else:
                output.append("{}".format(i))
        return output


example = Solution()

output = example.fizzBuzz(2)
print(output)