# add = lambda a, b, c: a + b + c
# print(add(a=2, b=3, c=4))
# print(add(a=2, a=3, c=4)) # Throws an error because a is assigned multiple times

l = [1, 2, 3, 4, 5]
# ans = [2, 4, 6, 8, 10] -> multiply each element by 2

# ans = []
# for num in l:
#     ans.append(num * 2)
# print(ans)

multi = lambda x: x * 2
# print(multi(1))

# ans = []
# for num in l:
#     ans.append(multi(num))
# print(ans)

# ans = map(multi, l, l) # TypeError: <lambda>() takes 1 positional argument but 2 were given
# ans = map(multi, l)
# print(list(ans))

# nums = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ans = list(map(lambda x: x % 2 == 0, nums)) # [True, False, True, False, True, False, True, False, True, False]
# print(ans)

# for idx in range(10):
#     print(idx)

# x = list(range(10))
# print(x)

# nums = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ans = list(filter(lambda x: x % 2 == 0, nums)) # [0, 2, 4, 6, 8], filters only those elements which are true
# print(ans)


nums = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = list(map(lambda x: x % 2 == 0, nums)) # [True, False, True, False, True, False, True, False, True, False]
# print(ans)

# ans_1 = []

# for ele, res in zip(nums, ans):
#     if res:
#         ans_1.append(ele)
# print(ans_1)


# l = ['a', 'b', 'c', 'cab', 'aab', 'abc', 'aa']
# # print(sorted(l)) # ['a', 'aa', 'aab', 'abc', 'b', 'c', 'cab']
# print(sorted(l, key=len)) # ['a', 'b', 'c', 'aa', 'cab', 'aab', 'abc']

cricket_scores = {
    "Kohli": 63.95,
    "Dhoni": 56.85,
    "Rohit": 61.25,
    "Ruturaj": 62.25
}

# print(cricket_scores.items()) # dict_items([('Kohli', 63.95), ('Dhoni', 56.85), ('Rohit', 61.25), ('Ruturaj', 62.25)])
# dict_sorted = dict(sorted(cricket_scores.items(), reverse=True)) # {'Ruturaj': 62.25, 'Rohit': 61.25, 'Kohli': 63.95, 'Dhoni': 56.85}
dict_sorted = dict(sorted(cricket_scores.items(), reverse=True, key=lambda x: x[1])) # {'Kohli': 63.95, 'Ruturaj': 62.25, 'Rohit': 61.25, 'Dhoni': 56.85}
print(dict_sorted)