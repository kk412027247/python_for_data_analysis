def my_function(x, y, z=1.5):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)


print(my_function(5, 6, z=0.76))

print(my_function(3.14, 7, 3.5))

print(my_function(10, 20))


# 命名空间、作用域和本地函数

def func():
    a = []
    for i in range(5):
        a.append(i)


b = []


def func():
    for i in range(5):
        b.append(i)


c = None


def bind_c_variable():
    global c
    c = []


bind_c_variable()

print(c)


def f():
    a = 5
    b = 6
    c = 7
    return a, b, c


a, b, c = f()

return_value = f()


def f():
    a = 5
    b = 6
    c = 7
    return {'a': a, 'b': b, 'c': c}


print(type(f))

states = ['    Alabama', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south   carolina##', 'West virginia?']

import re


def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result


print(clean_strings(states))


def remove_punctuation(value):
    return re.sub('[!#?]', '', value)


clean_ops = [str.strip, remove_punctuation, str.title]


def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result


result = clean_strings(states, clean_ops)

print(result)

for x in map(remove_punctuation, states):
    print(x)