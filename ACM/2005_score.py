


class Solution():
    def score(self, input):
        sum = 0
        cnt = 0
        for i in range(len(input)):
            if input[i] == 'O':
                cnt += 1
            else:
                cnt = 0
            sum = sum + cnt
        return sum

example = Solution()

input = 'OOXXOXXOOO'
output = example.score(input)
print(output)