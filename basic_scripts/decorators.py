# def add_deco(func):
#     def add_new(val1, val2):
#         if type(val1) == type(val2):
#             return func(val1, val2)
#         else:
#             return func(str(val1), str(val2))
#     return add_new

# @add_deco
# def add(val1, val2):
#     return val1 + val2

# res = add(10, 20)
# print(res)

# res = add(10, "Python")
# print(res)

# def login_required(func):
#     def login(username, password, value):
#         if username == "abc" and password == 123:
#             return func(username, password, value)
#         else:
#             return "Not Authorised"
#     return login

# @login_required
# def update_email(username, password, new_email):
#     return f"Your new email address is {new_email}"

# @login_required
# def update_contact(username, password, new_contact):
#     return f"Your updated contact number is {new_contact}"

# print(update_email("abc", 123, "abc@123.com"))
# print(update_contact("abc", 124, "123456789"))

def result_deco(func):
    def distinction(marks):
        for m in marks:
            if m > 75:
                print("Distinction")
        func(marks)
    return distinction

@result_deco
def result(marks):
    for m in marks:
        if m < 35:
            print("Fail")
            break
    else:
        avg = round(sum(marks) / len(marks), 2)
        if avg > 40:
            print("Pass")
        else:
            print("Fail")

result([50, 40, 90, 80, 30])
print("-------------")
result([50, 40, 90, 80, 50])
