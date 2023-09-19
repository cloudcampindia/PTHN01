# s = "cloud camp"
# print(s[0:10:2])
# print('-' * 10)
# print(1, 2)
# print('-' * 10)
# print(1)
# print(2)
# print(1, 2, sep='\n', end=' ')
# print(1, 2, end=' ')

# num1, num2 = 100, 200
# print("The value of num1 is {} and the value of num2 is {}.".format(num1, num2))
# print("The value of num1 is {1} and the value of num2 is {0}.".format(num1, num2))
# print("The value of num1 is {num1} and the value of num2 is {num2}.".format(num1=100, num2=100))

# sample = {"num1": 100, "num2": 200}
# print(f"The value of num1 is {sample['num1']} and the value of num2 is {sample['num2']}.")

# s = "Python,C++,Java,Go"
# s_list = s.split(',')
# print(s_list)

# s = "Python C++ Java Go"
# s_list = s.split()
# print(s_list)

# s2 = ";".join(s_list)
# print(s2)

# s = "cloud"
# s_list = list("cloud") # ['c', 'l', 'o', 'u', 'd']
# print(s_list)

# sample = "a b c"
# sep = " "
# res = []

# # for ch in sample:
# #     if ch == sep:
# #         continue
# #     res.append(ch)
# # print(res)

# print(sample.split(" "))

# s = "Python,c++,Java,Go"
# ans = ""
# str_search = "c++" # substring
# str_idx = s.find(str_search)
# if str_idx == -1:
#     ans = "Not Found"
# else:
#     ans = str_idx
# print(f"{str_search}:", ans)

# s = "Python,c++,Java,Go"
# ans = ""
# str_search = "Python"
# if str_search in s:
#     ans = s.index(str_search)
# else:
#     ans = "Not Found"
# print(f"{str_search}:", ans)

# for row in range(5):
#     print("*" * (row + 1))

# for row in range(5):
#     for col in range(row + 1):
#         print("*", end='')
#     print("\n") 

# for row in range(5):
#     for col in range(5):
#         print("*", end='')
#     print("\n")

s = "aabcda"
# print(s.count('a'))

# s = s.replace('bcd', 'pqr')
# print(s)

# print(dir(s))

# s_methods = "'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'"
# s_methods_len = len(s_methods.split(", "))
# # print(s_methods_len)

# for idx, method in enumerate(s_methods.split(", ")):
#     print(idx, method) 

# s = "abcdEF"
# print(s.isupper())
# print(s.islower())
# s = s.capitalize()
# print(s)

# s = "     abc d       defff      "
# print(len(s))
# # s = s.strip()
# # s = s.lstrip()
# s = s.rstrip()
# print(s, len(s))

given_string = "HackerRank.com presents \"Pythonist 2\"."
expected_output = "hACKERrANK.COM PRESENTS \"pYTHONIST 2\"."

output = []
for char in given_string:
    output.append(char.swapcase())
res = "".join(output)
print(res)