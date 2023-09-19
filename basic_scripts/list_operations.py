# a = [10, 20, 30, 40, 50]
# print(a[0:4])
# print(a[-1])
# print(a[len(a) - 1])
# print(a[:3])
# print(a[3:])

# print(a[::2]) # even positions
# print(a[1::2]) # odd positions
# print(a[-3:-1])
# print(a[-1:-3:-1])

# print(a[::-1])

# a.append(60)
# print(a)
# a.extend(25, 35)

# a = [10, 20, 30, 40, 50]
# a.append([25, 35])
# print(a, len(a))

# a = [10, 20, 30, 40, 50]
# a.extend([25, 35])
# print(a, len(a))

# a = [10, 20, 30, 40, 50]
# a.insert(1, 100)
# print(a)

# a = [10, 20, 30, 40, 50]
# a[1] = 200
# print(a)

# a = [10, 20, 30, 40, 50, [25, [50, 60, 15, [10, 8, 6]]]]
# print(a[5][1][3][1])

# a = [10, 20, 30, 40, 50]
# del a
# print(a)

# a = [10, 20, 30, 40, 50]
# b = a.pop(1)
# print(a)
# print(b)

# a = [10, 20, 30, 40, 50]
# b = a.pop()
# print(a)
# print(b)

# a = [10, 20, 30, 40, 50]
# b = a.pop(10, 20) # Throws an error
# print(a)
# print(b)

# a = [10, 20, 30, 40, 50]
# b = a.pop([10]) # Throws an error
# print(a)
# print(b)

# a = [10, 20, 30, 40, 50]
# b = a.remove(30)
# print(a)
# print(b)

# a = [10, 20, 30, 40, 50]
# b = a.clear()
# print(a)
# print(b)
# print(a == b)

# a = [5, 3, 2, 4, 1]
# a.sort()
# print(a)

# a = [5, 3, 2, 4, 1]
# b = sorted(a)
# print(a)
# print(b)

# a = ['w', 'a', 'c', 'z', 'y']
# a.sort()
# print(a)

# a = ['w', 'a', 'c', 'z', 'y', 21]
# a.sort() # Error
# print(a)

# a = ['a', 'A', 'b', 'C']
# a.sort()
# print(a) # ['A', 'C', 'a', 'b']

# a = [5, 3, 2, 4, 1]
# b = sorted(a, reverse=True)
# print(a)
# print(b)

# a = [10, 20, 30, 40, 50]
# a = [10, 20, 20, 30, 10, 20, 50]
# a_idx = a.index(20)
# a_idx = a.index(200) # throws an error if not present
# print(a_idx)


# a = [10, 20, 20, 30, 10, 20, 50]
# a_idx = a.count(20)
# a_idx = a.count(200) # returns 0 if not present
# print(a_idx)

# l1 = [10, 20, 30, 40, 50]
# l2 = [1, 2, 3, 4, 5]

# l = list() # empty list
# l.append(l1)
# l.append(l2)
# l.extend([l1, l2])
# print(l, len(l))

# l = list()
# l.extend(l1)
# l.extend(l2)
# l = l1 + l2 # extends the list
# print(l, len(l))

# l = [1, 2, 3, 4, 5]
# l = l + l # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] len -> 10
# l *= 2 # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5] len -> 20
# l.extend(l) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5] len -> 40
# print(l, len(l))

# l1 = [1, 2, 3, 4, 5]
# # l2 = l1 # shallow copy
# l2 = l1.copy() # deep copy
# l2[-1] = 500
# print("l2:", l2)
# print("l1:", l1)

# l1 = [1, 2, 3, 4, 5]
# # ans: [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
# l2 = l1.copy()

# for ele in l1:
#     l2.append(ele * 10)
#     print("l2:", l2)
#     print("l1:", l1)
#     break

A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]
print(list(zip(*X)))