# def add():
#     print(2 + 3)
#     print(3 + 4)
# add()

# def add(a, b):
#     print(a + b)
# add(2, 3)

# def sub(a, b):
#     print(a - b)
# sub(a = 3, b = 2)
# sub(b = 2, a = 3)

# def add(a, b, c = 10):
#     return a + b + c

# # res = add(a=2, 3, c=20) # Throws an error, as positional argument (3) should come before keyword argument (a=2)
# # res = add(a=2, c=20, 3) # Throws an error, as positional argument (3) should come before keyword argument (a=2, c=20)
# # res = add(3, a=2, c=20) # Throws an error, as multiple values are passed to argument 'a'
# res = add(a=3, b=2, c=20)
# print(res)


## Linear search
# def linear_search(given_list, search_element):
#     """
#     This function performs linear search
#     Input:
#         - Given list
#         - Search element
#     Output:
#         - If the value is present inside the list
#         the function returns True and its index
#         - If not, it returns False and -1
#     Note:
#         - This function returns only the first occurrence
#         of the search element inside the provided list
#     """
#     for idx, ele in enumerate(given_list):
#         if ele == search_element:
#             return True, idx
#     return False, -1

# given_list = [1, 2, 3, 10, 10, 20, 30]
# search_element = 10
# res = linear_search(given_list, search_element)

# Doesn't return Anything, rather prints on the console directly
# test_res = help(linear_search)
# print(test_res)

# print(type(res))
# is_found, idx = res # Tuple unpacking
# print(is_found, idx)

# def test_fun(a, b):
#     print(a + b)
#     # return # returns None by default

# res = test_fun(2, 36)
# print(res)


# def avg(*args):
#     # print(type(args))
#     # print(args)
#     # print(*args)
#     ans = 0
#     for num in args:
#         ans += num
#     return ans / len(args)

# res = avg(1, 2, 3, 4, 5)
# print(res)

# res = avg(1, 2, 3)
# print(res)


# def add(a=2, b=3, c=4, *args, **kwargs):
#     print(a + b + c)
#     print(args)
#     print(type(kwargs))
#     print(kwargs)

# add(a=5, b=6, c=7, d=10, e=11)

# def f1(n):
#     if n == 1:
#         return 1
#     s = n + f1(n-1)
#     return s

# ans = f1(3)
# print(ans)

# def fact(n):
#     if n == 1:
#         return 1
#     s = n * fact(n-1)
#     return s

# ans = fact(5)
# print(ans)

# print(fact)

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     return a / b

# def calc(fn, a, b):
#     return fn(a, b)

# ans = calc(mul, 2, 3)
# print(ans)

# a = 2

# def fn():
#     b = 10
#     return a + 2
# print(fn())
# print(b)

# a = 2

# def fn():
#     global b
#     b = 10
#     # print("Locals:",locals())
#     # print("Globals:",globals())
#     a += 2
#     # return a
# print(a)
# print(fn())
# # print(b)

# print("Locals:",locals())
# print("Globals:",globals())

# def add():
#     print(2 + 3)
#     print(3 + 4)
# # print(add)
# # print(add())
# x = add # Function Object
# print(x())

# a = int
# print(a)

# def add(num1, num2):
#     return num1 + num2

# def add(num1, num2, num3):
#     return num1 + num2 + num3

# def add(*args):
#     return sum(args)

# print(add(10, 20))
# print(add(10, 20, 30))