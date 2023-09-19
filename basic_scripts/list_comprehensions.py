# l = [10, 20, 30, 40]

# ans = []
# for element in l:
#     ans.append(element * 10)


# ans = [element * 10 for element in l]

# l = ["a", "abc", "bacd", "abcdefd"]
# ans = [len(element) for element in l]
# print(ans)

# import timeit

# t = timeit.timeit(stmt="""
# ans = []
# for ele in range(100000000):
#     ans.append(ele * 10)
# """, number=1)
# print(t)

# t = timeit.timeit(stmt="""
# ans = [ele * 10 for ele in range(100000000)]
# """, number=1)
# print(t)

# print(help(timeit.timeit))

# import math
# print(math.pow(2, 3))

# l = [10, 15, 20, 25, 30, 35, 40]

# ans = []
# for ele in l:
#     if ele % 2 == 0:
#         ans.append(ele)
# print(ans)

# ans = [ele for ele in l if ele % 2 == 0]
# print(ans)

# l = [10, 15, 20, 25, 30, 35, 40]

# # Using Loops and normal if-else
# ans = []
# for ele in l:
#     if ele % 2 == 0:
#         res = "Even"
#     else:
#         res = "Odd"
#     ans.append(res)
# print(ans)

# # Using Loops and single line if-else
# ans = []
# for ele in l:
#     ans.append("Even" if ele % 2 == 0 else "Odd")
# print(ans)

# # Using Loops and List Comprehension
# ans = ["Even" if ele % 2 == 0 else "Odd" for ele in l]
# print(ans)


# l = [10, 15, 20, 25, 30, 40, 45, 60]

# ans = []
# for ele in l:
#     if ele % 3 == 0:
#         if ele % 5 == 0:
#             ans.append(ele)
# print(ans)

# ans = [ele if ele % 3 == 0 else None for ele in l if ele % 5 == 0]
# print(ans)

# Dict Comprehension
# l = [10, 15, 20, 25, 30, 40, 45, 60]
# ans = {val: val**2 for val in l}
# print(ans)

# Set Comprehension
l = [10, 15, 20, 25, 30, 40, 45, 60]
ans = {val % 2 for val in l}
print(ans)

# l = [10, 15, 20, 25, 30, 40, 45, 60]
# ans = ("Even" if ele % 2 == 0 else "Odd" for ele in l)
# print(ans)


