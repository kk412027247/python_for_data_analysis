# 列表推导式

# [expr for val in collection if condition]

# result = []
# for val in collections:
#     if condition:
#         result.append(expr)


strings = ['a', 'as', 'bat', 'car', 'dove', 'python']

list1 = [x.upper() for x in strings if len(x) > 2]

print(list1)

#  字典的推导式

# dict_comp = {key-expr: value-expr for value in collection if condition}

# 集合的推导式

# set_comp = {expr for value in collection if condition}

unique_lengths = {len(x) for x in strings}
print(unique_lengths)

unique_lengths2 = set(map(len, strings))

print(unique_lengths2)

loc_mapping = {val: index for index, val in enumerate(strings)}
print(loc_mapping)

# 嵌套列表推导式

all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'], ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]

names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') >= 2]
    names_of_interest.extend(enough_es)

print(names_of_interest)

result = [name for names in all_data for name in names if name.count('e') >= 2]
print(result)

some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]

print(flattened)

# 请牢记for表达式的顺序应当和你写嵌套for循环来替代列表推导式的顺序一致：

flattened2 = []

for tup in some_tuples:
    for x in tup:
        flattened2.append(x)

print(flattened2)

net_list = [[x for x in tup] for tup in some_tuples]
print(net_list)

#
# 生成器表达式
#
# 用生成器表达式来创建生成器更为简单。生成器表达式与列表、字典、集合的推导式很类似，创建一个生成器表达式，只需要将列表推导式的中括号替换为小括号即可：

# 生成器是构造新的可遍历对象的一种非常简洁的方式。普通函数执行并一次返回单个结果，而生成器则“惰性”地返回一个多结果序列，在每一个元素产生之后暂停，直到下一个请求。如需创建一个生成器，只需要在函数中将返回关键字return替换为yield关键字：

gen = (x ** 2 for x in range(100))
print(gen)


def _make_gen():
    for x in range(100):
        yield x ** 2


gen2 = _make_gen()

s = sum(x ** 2 for x in range(100))

s2 = sum([x ** 2 for x in range(100)])

d = dict((i, i ** 2) for i in range(5))

d2 = dict([(i, i**2) for i in range(5)])

print(s)
print(s2)
print(d)
print(d2)
