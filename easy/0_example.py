

# 由于数据类型set本身具有无序，唯一值的特性，可以用内置函数set对字符串和列表进行去重，挺方便的
# str = "asdfasdlklfgklgjsdfjkjl"
# se = set(str)       # 变为集合set，已经不是列表list
# print (se)          # {'j', 'f', 'a', 'd', 'l', 's', 'g', 'k'}
# str = list(se)      # 再变为列表list
# print(str)          # ['j', 'f', 'a', 'd', 'l', 's', 'g', 'k']


dict = {'Name': 'Xiaoxiao', 'Age': 18, 'School': 'Hrbeu'}

print (dict.get('School'))
print (dict.get('Sex'))