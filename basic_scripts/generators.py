# def fibo():
#     """
#     Generating infinite Fibonnaci Series
#     using Generators
#     """
#     num1 = 0
#     yield num1
#     num2 = 1
#     yield num2

#     while True:
#         next_num = num1 + num2
#         yield next_num
#         num1, num2 = num2, next_num

# g = fibo()
# # print(g)
# # print(dir(g))
# """
# ['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_suspended', 'gi_yieldfrom', 'send', 'throw']
# """
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# Use case 2: print 5 fibonacci numbers with each next call

# def fibo():
#     """
#     Generating infinite Fibonnaci Series
#     using Generators
#     """
#     output = []
#     num1 = 0
#     num2 = 1
#     output.extend([num1, num2])
#     count = 2
#     while True:
#         next_num = num1 + num2
#         output.append(next_num)
#         count += 1
#         if count == 5:
#             yield output
#             count = 0
#             output = []
#         num1, num2 = num2, next_num

# g = fibo()
# print(next(g))
# print(next(g))

# def printlist(l):
#     for value in l:
#         yield value

# l = [10, 20, 30, 40]
# g = printlist(l)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) # StopIteration

# NEVER EVER COMBINE BOTH RETURN AND YIELD 
# WITHIN ONE GENERATOR
# def printlist(l):
#     for value in l:
#         if value == 20:
#             return value
#         yield value

# l = [10, 20, 30, 40]
# g = printlist(l)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) # StopIteration

# l = [10, 20, 30, 40, 50]
# # t = [value ** 2 for value in l]
# t = (value ** 2 for value in l)
# print(t)
# print(next(t))