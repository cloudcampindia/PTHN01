# a = (10, 20, 30)
# value_to_insert = 40

# a = list(a)
# # a.insert(-1, value_to_insert)
# a.append(40)
# a = tuple(a)
# print(a)

# a = 10, 20, 30
# print(type(a))

# a, b = 10, 20
# print(a, b)

# a, b = 10, 20, 30
# print(a, b)


# a = (10, 20, 30)
# for idx, ele in enumerate(a):
#     print(idx, ele)

# a = (10, 20, 30, 40, 30, 50)
# print(a.count(30)) # 2
# print(a.index(30, 0)) # 2

# a = (10, 10, 20, 30, 40, 40, 30)
# print(a.index(30, ))

# fruits = ['apple', 'banana', 'cherry', 'banana', 'apple', 'cherry']
# fruit_to_search = "cherry"

# idx = 0

# for idx, fruit in enumerate(fruits):
#     if fruit == fruit_to_search:
#         # print(fruits.index(fruit_to_search, idx))
#         print(idx)

# print(x)

# print(dir(tuple))

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

# print(dir(list))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


a = (4, 1, 2, 3)
a = tuple(sorted(a))
print(a)