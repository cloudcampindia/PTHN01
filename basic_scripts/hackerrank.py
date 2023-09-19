# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()

#     print(student_marks, query_name)

#     marks = student_marks[query_name]
#     res = 0

#     for mark in marks:
#         res += mark
    
#     # '{:0.2f}, kg={:0.2f}, lb={:0.2f}, gal={:0.2f}'.format(var1, var2, var3, var4)
#     print('{:0.2f}'.format(res / 3))

N, X = tuple(map(int, input().split()))

students = []

for _ in range(X):
    marks = list(map(float, input().split()))
    students.append(marks)
    
idx = 0

while idx < N:
    ans = 0
    for student in students:
        ans += student[idx]
    print('{0:.1f}'.format(ans / X))
    idx += 1