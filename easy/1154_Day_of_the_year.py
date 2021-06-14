

class Solution:
    def dayOfYear(self, date: str) -> int:
        date_list = date.split('-')
        print(date_list)

        mouth = int(date_list[1])
        day = int(date_list[2])
        year = int(date_list[0])
        calindar = {0:0,1:31,3:31,5:31,7:31,8:31,10:31,12:31,4:30,6:30,9:30,11:30}
        if year % 4 == 0:
            calindar[2] = 29
        else:
            
            calindar[2] = 28
        print(calindar)
        day_sum = 0
        for i in range(mouth):
            day_sum = day_sum + calindar[i]
        day_sum += day
        return day_sum

example = Solution()
date = '2019-02-10'
output = example.dayOfYear(date)
print(output)