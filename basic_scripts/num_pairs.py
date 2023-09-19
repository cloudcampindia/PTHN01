given_list = [-1, 1, 5, 7, 100]
target_sum = 6
num_pairs = 0

# for idx in range(0, len(given_list) - 1):
#     for idy in range(idx + 1, len(given_list)):
#         ele1 = given_list[idx]
#         ele2 = given_list[idy]
#         if (ele1 + ele2 == target_sum):
#             num_pairs += 1
#             print(ele1, ele2)
# print(num_pairs)

valid_pair = []

for ele in given_list:
    if ele not in valid_pair:
        diff = target_sum - ele
        if diff in given_list:
            num_pairs += 1
            valid_pair.append(diff)
            print(valid_pair)

print(num_pairs)
