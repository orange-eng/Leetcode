

from collections import Counter
class Solution:
    def countLargestGroup(self, n: int) -> int:
        # # 分解做法
        # # 1.求每个数字的数位和
        # sum_list = list(map(lambda x: sum(map(int, str(x+1))), range(n)))
        # # 2. 记录每个和出现的次数
        # c_list = Counter(sum_list).values()
        # # 3. 记录每个和出现的次数进行计数
        # s_list = Counter(c_list).items()
        # # 4. 返回数字数目并列最多的组的次数，因此是[1]
        # return max(s_list)[1]

        return max(Counter(Counter(map(lambda x: sum(map(int, str(x+1))), range(n))).values()).items())[1]
