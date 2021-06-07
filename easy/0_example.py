

# 由于数据类型set本身具有无序，唯一值的特性，可以用内置函数set对字符串和列表进行去重，挺方便的
# str = "asdfasdlklfgklgjsdfjkjl"
# se = set(str)       # 变为集合set，已经不是列表list
# print (se)          # {'j', 'f', 'a', 'd', 'l', 's', 'g', 'k'}
# str = list(se)      # 再变为列表list
# print(str)          # ['j', 'f', 'a', 'd', 'l', 's', 'g', 'k']

# -------------------------------------------------------------------
# dict = {'Name': 'Xiaoxiao', 'Age': 18, 'School': 'Hrbeu'}

# print (dict.get('School'))
# print (dict.get('Sex'))

# ----------------------------------------------------------------------

#定义一个空字典
dict = {}

print(dict.setdefault('name','Bill'))
#向字典中添加一个名为name的key，默认值是Bill，输出结果：Bill

print(dict)
#输出结果：{'name': 'Bill'}

print(dict.setdefault('name','Mike'))
#并没有改变name的值，输出结果：Bill

print(dict)
#输出结果：{'name': 'Bill'}
