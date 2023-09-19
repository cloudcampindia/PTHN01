# fruits = ["apple", "banana", "cherry", "dragon fruit"]

# for fruit in fruits:
#     print(fruit)

# for element in range(0, 10, 2):
#     print(element)

# fruits = ["apple", "banana", "cherry", "dragon fruit"]

# for idx in range(0, len(fruits)):
#     print(fruits[idx])

# for idx in range(0, len(fruits)):
#     print(idx, fruits[idx])

# Given list of student marks, total marks in the exam and pass percentage as well. 
# Seperate the student marks list based on who passed the exam and who failed the exam

# student_marks = [220, 350, 160, 400, 450]
# total_marks = 500
# pass_percentage = 40

# passed_students = []
# failed_students = []

# for mark in student_marks:
#     percentage = (mark / total_marks) * 100
#     if percentage >= pass_percentage:
#         passed_students.append([mark, percentage])
#     else:
#         failed_students.append([mark, percentage])
    
# print(passed_students, failed_students)


fruits = ["apple", "banana", "cherry", "dragon fruit", "cherry", "cherry"]
search_fruit = "cherry"

count = 0
# for fruit in fruits:
#     # print(fruit)
#     if fruit == search_fruit:
#         print("fruit found")
#         count += 1
#         break
#     count = 100
# # print("Outside loop")
# print("No: of cherries:", count)
# print("---------------------")

# count = 0
# for fruit in fruits:
#     # print(fruit)
#     if fruit == search_fruit:
#         print("fruit found")
#         count += 1
#         continue

# print("No: of cherries:", count)

# for fruit in fruits:
#     print(fruit)
#     if fruit == search_fruit:
#         print("fruit found")
#         count += 1
#         break
# else:
#     print("Loop completed")


# fruits = ["apple", "banana", "cherry", "dragon fruit", "cherry", "cherry"]
# search_fruit = "cherry"

# count = 0

# while (count < len(fruits)):
#     print(fruits[count])
#     if (fruits[count] == search_fruit):
#         print("fruit found")
#         break
#     count += 1
# else:
#     print("Loop completed")

list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for ele in list_2d:
    print(ele)
    for ele_1 in ele:
        print(ele_1)