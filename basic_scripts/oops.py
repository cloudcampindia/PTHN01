# class Add:
#     def __init__(self):
#         self.a = 2
#         self.b = 3

#     def sum(self):
#         return self.a + self.b

# add = Add()
# print(type(add))
# print(add.a)
# print(add.b)
# print(add.sum())

# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.password = password
#         self.email = email
#         self.user_logged_in = False
#         self.is_active = True

#     def add_contact(self, number):
#         self.number = number

#     def login(self, username, password):
#         if self.username == username and self.password == password:
#             self.user_logged_in = True
#             return True
#         else:
#             return False

#     def get_details(self):
#         return self.username, self.email
    
#     def change_active_status(self, status):
#         self.is_active = status
    


# user1 = User("chaitanya", "chaitanya@camp.com", 123456)
# user1.add_contact(987654321)

# print(user1)
# print(user1.username)
# print(user1.email)
# print(user1.password)
# print(user1.number)

# is_logged_in = user1.login("abc", 456)
# # is_logged_in = user1.login("chaitanya", 123456)
# if is_logged_in:
#     print("Login Successful")
#     print(user1.user_logged_in)
# else:
#     print("Invalid credentials")
#     print(user1.user_logged_in)


# user1 = User("chaitanya", "chaitanya@camp.com", 123456)
# user2 = User("vijay", "vijay@camp.com", 123456)
# user3 = User("jhansi", "jhansi@camp.com", 123456)

# users = [user1, user2, user3]
# for user in users:
#     print(user.get_details())
#     if user.email == "vijay@camp.com":
#         user.change_active_status(False)
#     print(user.is_active)


# class Student:
    
#     failed_students = [] # Class variable
#     count = 0 # Class variable

#     def __init__(self, roll_no, marks, branch, teacher):
#         self.roll_no = roll_no
#         self.marks = marks
#         self.branch = branch
#         self.result = None
#         self.teacher = teacher
#         self.failed_students = [] # Instance variable
#         Student.count += 1

#     def get_details(self):
#         return f"{self.roll_no}, {self.branch}, {self.marks}, {self.teacher.name}"
    
#     def calc_result(self):
#         stud_marks = self.marks.values()
#         stud_marks_filter = list(map(lambda x: x >=40, stud_marks))
#         stud_marks_filter = sum(stud_marks_filter)
#         self.percentage = sum(stud_marks) / (len(stud_marks))
#         if (self.percentage >= 40 and stud_marks_filter == 5):
#             self.result = "Pass"
#         else:
#             self.result = "Fail"
#             Student.failed_students.append(self.roll_no)


# class Teacher:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject


# teacher1 = Teacher("abc", "maths")
# teacher2 = Teacher("bcd", "eng")

# stud1 = Student(1, {"eng": 80, "phy": 60, "chem": 85, "maths": 95, "programming": 81}, branch="ECE", teacher=teacher1)
# stud2 = Student(2, {"eng": 60, "phy": 70, "chem": 45, "maths": 96, "programming": 82}, branch="Civil", teacher=teacher2)
# stud3 = Student(3, {"eng": 80, "phy": 80, "chem": 75, "maths": 45, "programming": 83}, branch="Mech", teacher=teacher1)
# stud4 = Student(4, {"eng": 30, "phy": 40, "chem": 65, "maths": 83, "programming": 84}, branch="CSE", teacher=teacher1)
# stud5 = Student(5, {"eng": 60, "phy": 80, "chem": 95, "maths": 92, "programming": 85}, branch="IT", teacher=teacher2)

# print("No: of students:", Student.count)

# studs = [stud1, stud2, stud3, stud4, stud5]
# top_3_students = []

# for stud in studs:
#     print(stud.get_details(), end=' ')
#     print(stud.count, end=' ')
#     stud.calc_result()
#     if stud.roll_no not in Student.failed_students:
#         top_3_students.append(stud.percentage)
#     print(stud.percentage, stud.result, stud.teacher.subject)

# print(Student.failed_students)
# print(top_3_students) # [80.2, 70.6, 72.6, 82.4]
# sorted_top_3 = sorted(top_3_students, reverse=True)
# print(*sorted_top_3[:3], sep='\n') # * -> Iterable unpacking

# print(dir(stud1))
# print(stud1.__dict__)


# class Student:
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Student.count += 1
    
# obj1 = Student('a')
# obj2 = Student('b')

# # obj1.count = 10
# Student.count = 5
# print(Student.count)
# print(obj2.count)
# print(obj1.count)


# class Student:
#     def __init__(self, marks):
#         self.__marks = marks # Data hiding

#     # Getter
#     def getMarks(self):
#         return self.__marks

#     # Setter
#     def setMarks(self, marks):
#         self.__marks = marks

# stud1 = Student(50)
# # print(stud1._marks) # Error
# # print(stud1.__marks) # Error
# # print(stud1.marks) # Error
# # print(stud1._Student__marks) # NOT PREFERRED
# print(stud1.getMarks())
# stud1.setMarks(70)
# print(stud1.getMarks())

# class Animal:
#     def __init__(self):
#         print("Animal created")
#         self.class_name = "Animal"
    
#     def eat(self):
#         print("Eating")
    
#     def whoAmI(self):
#         print("Animal")

# class Dog(Animal):
#     # pass
#     def __init__(self):
#         # Animal.__init__(self) # Method 1
#         super().__init__() # Method 2
#         print("Dog created")

#     # Overrides / Modifies the functionality of whoAmI method defined in parent class
#     def whoAmI(self):
#         print("Dog")

# d = Dog()
# print(d.class_name)
# d.eat()
# d.whoAmI()


# class Student:
    
#     """
#     This class accepts list of students and marks and performs the following
#     1. Calculates the result
#     2. Stores the failed students in a list
#     """

#     failed_students = [] # Class variable
#     count = 0 # Class variable

#     def __init__(self, roll_no, marks, branch, teacher):
#         self.roll_no = roll_no
#         self.marks = marks
#         self.branch = branch
#         self.result = None
#         self.teacher = teacher
#         self.failed_students = [] # Instance variable
#         Student.count += 1

#     def __str__(self):
#         return f"{self.roll_no}, {self.branch}, {self.marks}, {self.teacher.name}"
    
#     def calc_result(self):
#         stud_marks = self.marks.values()
#         stud_marks_filter = list(map(lambda x: x >=40, stud_marks))
#         stud_marks_filter = sum(stud_marks_filter)
#         self.percentage = sum(stud_marks) / (len(stud_marks))
#         if (self.percentage >= 40 and stud_marks_filter == 5):
#             self.result = "Pass"
#         else:
#             self.result = "Fail"
#             Student.failed_students.append(self.roll_no)


# class Teacher:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject


# teacher1 = Teacher("abc", "maths")
# teacher2 = Teacher("bcd", "eng")

# stud1 = Student(1, {"eng": 80, "phy": 60, "chem": 85, "maths": 95, "programming": 81}, branch="ECE", teacher=teacher1)
# stud2 = Student(2, {"eng": 60, "phy": 70, "chem": 45, "maths": 96, "programming": 82}, branch="Civil", teacher=teacher2)
# stud3 = Student(3, {"eng": 80, "phy": 80, "chem": 75, "maths": 45, "programming": 83}, branch="Mech", teacher=teacher1)
# stud4 = Student(4, {"eng": 30, "phy": 40, "chem": 65, "maths": 83, "programming": 84}, branch="CSE", teacher=teacher1)
# stud5 = Student(5, {"eng": 60, "phy": 80, "chem": 95, "maths": 92, "programming": 85}, branch="IT", teacher=teacher2)

# # print(stud1.__dict__) # prints all the variables that are applicable for this instance
# # print(Student.__dict__)  # prints all the variables that are applicable for this Class
# # print(Student.__doc__) # prints the document string of the class
# print(stud1)


# class Student:

#     # class variable
#     count = 0

#     @classmethod
#     def test(cls):
#         print("class method")
#         print(cls.count)

# Student.test()


# class A:
#     test = 10
#     __abc = 100

# print(A.__dict__)
# print(A._A__abc)

# class A:
#     @staticmethod
#     def f1():
#         print('A')

# class B:
#     @staticmethod
#     def f1():
#         print('B')

# A.f1()

# obj = A()
# obj.f1() # f1()

# obj = B()
# obj.f1() # f1()

# class A:
#     def __init__(self):
#         self.a = 5

# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.a = 500
#         self.b = 50

# b = B()
# print(b.a)

# class A:
#     x = 10

# class B(A):
#     x = 20

# print(B.x)

# class A:
#     def f1(self, a):
#         print('A')

# class B:
#     def f1(self):
#         print('B')

# b = B()
# b.f1('10') # Gives an error

class A:
    x = 10
    def __init__(self):
        self.x = 20

a = A()
print(a.__dict__)
print(A.__dict__)