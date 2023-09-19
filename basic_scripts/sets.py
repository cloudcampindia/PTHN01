# a = {1, 2, 3, 4, 5}
# print(a[0]) # error
# print(a[0:2]) # error

# l = [1, 1, 2, 3, 4, 5, 2, 8]
# l_set = set(l)
# print(l_set)

# a = {[1, 2, 3, 4, 5]}
# print(a)


s1 = {10, 20, 30, 40, 50}
s2 = {40, 50, 60, 70, 80}

# s3 = s1.union(s2)
# s3 = s1.intersection(s2)
# s3 = s1.difference(s2)
# s3 = s2.difference(s1)
# s3 = s1.symmetric_difference(s2)

# s1.update(s2)
# s1.intersection_update(s2)
# s1.difference_update(s2)
# print(s1)

# s1 = {10, 20, 30, 40, 50}
# r = s1.pop()
# r = s1.remove(300)
# r = s1.discard(300)
# print(s1, r)

# for ele in s1:
#     print(ele)

s1 = {10, 20, 30, 40, 50}
s1.add(60) # inplace operation
print(s1)

s1.add(60) # inplace operation
print(s1)
