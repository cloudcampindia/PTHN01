# l = [1, 2, 3, 4, 5, 10, 20]
# # print(l)
# # print(dir(l))
# # print('__iter__' in dir(l)) # True
# # print('__next__' in dir(l)) # False

# l = iter(l)
# # print(l)
# # print(dir(l))
# # print('__iter__' in dir(l))
# # print('__next__' in dir(l))

# print(next(l))
# # print(l[0]) # 'list_iterator' object is not subscriptable
# # print(l[1:3]) # 'list_iterator' object is not subscriptable
# l = list(l)
# print(l)

# print('__iter__' in dir(range))
# print('__next__' in dir(range))

import itertools
# print(dir(itertools))
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', '_grouper', '_tee', '_tee_dataobject', 'accumulate', 'chain', 'combinations', 'combinations_with_replacement', 'compress', 'count', 'cycle', 'dropwhile', 'filterfalse', 'groupby', 'islice', 'pairwise', 'permutations', 'product', 'repeat', 'starmap', 'takewhile', 'tee', 'zip_longest']
# l1 = [1, 2, 3, 4]
# l2 = ['a', 'b', 'c']
# l3 = range(100, 106)

# i = itertools.chain(l1, l2, l3) # l1 + l2 + l3
# print(i)
# # print(dir(i))
# print('__iter__' in dir(i))
# print('__next__' in dir(i))

# # for val in i:
# #     print(val)

# while True:
#     try:
#         print(next(i))
#     except StopIteration:
#         print("the iterator is empty")
#         break


l1 = [1, 2, 3]
l2 = ['a', 'b']
l3 = range(100, 102)

i = itertools.chain(l1, l2, l3) # l1 + l2 + l3
t = itertools.tee(i, 5)
print(type(t))
print(len(t))
print(t)

idx = 0
while idx < len(t):
    for val in t[idx]:
        print(val)
    print("***********")
    idx += 1

l1 = [1, 2, 3]
l2 = ['a', 'b']
i = itertools.chain(l1, l2) # [1, 2, 3, a, b]
p = itertools.pairwise(i)
for val in p:
    print(val)