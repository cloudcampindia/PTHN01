# a = {"name": "cloud camp"}
# print(type(a))
# print(a["name"])

# a = {"name": ["Chaitanya", "Lavanya", "Harshita"], 
#      "course": "python", 
#      "email_address": ["a@abc.com", "b@abc.com", "c@abc.com"]
#     }
# print(a["name"])
# print(a["email_address"])

# a["name"].append("Nagendra")
# print(a)

# a["email_address"][2] = "d@abc.com"
# print(a)

# a["id"] = [1, 2, 3, 4]
# print(a)

# print(a.get("nae", -1))
# print(a.setdefault("country", ["India", "India", "India"]))
# print(a)

# squares = dict()
# for num in range(1, 11):
#     squares.setdefault(num, num**2)
# print(squares)


# a = {"name": ["Chaitanya", "Lavanya", "Harshita"], 
#      "course": "python", 
#      "email_address": ["a@abc.com", "b@abc.com", "c@abc.com"]
#     }

# for k, v in a.items():
#     print(k, v)

# item = a.popitem()
# print(a, item)

# item = a.pop("course")
# print(a, item)

# a = {1: 1, 2: 4, 3: 9}
# b = {4: 16, 5:25}
# c = a.update(b) # update is an inplace operation
# # print(a, c)
# print(a)

# del, clear
# del a[3] # del is an inplace operation
# print(a)

# a.clear() # clear is an inplace operation
# print(a)

# a['new'] = b
# print(a)

# a = {"name": ["Chaitanya", "Lavanya", "Harshita"], 
#      "course": "python", 
#      "email_address": ["a@abc.com", "b@abc.com", "c@abc.com"]
#     }

# for k, v in a.items():
#     print(k, v)

# print("============")

# print(a.keys())
# print(a.values())

# for k, v in zip(a.keys(), a.values()):
#     print(k, v)

# a = [1, 2, 3, 4, 5]
# b = [1, 4, 9, 16, 25]

# print(list(zip(a, b)))

# for ele, ele1 in zip(a, b): # (1, 1), (2, 4)
#     print(ele, ele1)

# d1 = {1: 1, 2: 4, 3: 9}
# # d2 = d1.copy()
# d2 = d1
# d2[4] = 16
# print("d1:", d1)
# print("d2:", d2)


# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# print(d['k1'][2]['k2'][1]['tough'][2][0]) # Solution 1
# print(d['k1'][-1]['k2'][-1]['tough'][-1][-1]) # Solution 2

cricket_scores = {
    "Kohli": 63.95,
    "Dhoni": 56.85,
    "Rohit": 61.25,
    "Ruturaj": 62.25
}

dict_sorted = dict(sorted(cricket_scores.items(), reverse=True))
print(dict_sorted)