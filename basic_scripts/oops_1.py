class Person:
    def __init__(self, name):
        self.__name = name

    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name

class Instructor(Person):
    def __init__(self, inID, name, profession, experience, tech):
        super().__init__(name)
        self.__inID = inID
        self.__profession = profession
        self.__experience = experience
        self.__tech = tech

class Courses:

    courses = []

    @classmethod
    def checkCourse(cls, cID):
        for course in cls.courses:
            if course.__cID == cID:
                return course
        else:
            return -1
    
    @classmethod
    def add_course(cls, obj):
        cls.courses.append(obj)

    def __init__(self, cID, name, desc, instructor):
        self.__cID = cID
        self.__name = name
        self.__desc = desc
        self.__instructor = instructor
        Courses.add_course(self) # Courses.course.append(self) --> Not a better practice
    
    def __str__(self):
        return f"{self.__cID}, {self.__name}, {self.__desc}, {self.__instructor.getName()}"
    
    def setCourseName(self, name):
        self.__name = name

    def getCourseName(self):
        return self.__name

    def getCourseID(self):
        return self.__cID

    def getInstructor(self):
        return self.__instructor

class Tutorials:
    
    tutorials = []

    @classmethod
    def fetchTutorials(cls, cID):
        tutorials = []
        for tutorial in cls.tutorials:
            if tutorial.__cID.getCourseID() == cID:
                tutorials.append(tutorial)
        
        if len(tutorials) == 0: 
            return -1
        
        return tutorials
    
    @classmethod
    def addTutorial(cls, obj):
        cls.tutorials.append(obj)

    def __init__(self, tutID, name, content, cID):
        self.__tutID = tutID
        self.__name = name
        self.__content = content
        self.__cID = cID
        Tutorials.tutorials.append(self)
    
    def getTutorialName(self):
        return self.__name

# Instructor Objects
in1 = Instructor(1, "ABC", "XYZ", 5, ['python', 'java'])
in2 = Instructor(2, "ABD", "XY", 2, ['c', 'java'])
in3 = Instructor(3, "ABF", "XYE", 3, ['python'])
# print(in1.getName())

# Courses objects
course1 = Courses(101, "Python", "Python Dev", in1)
course2 = Courses(102, "C Programming", "Basics of Programming", in2)
course3 = Courses(103, "Python AI", "Python AI Dev", in1)

# Tutorials Objects
# tutID, name, content, cID
tut1 = Tutorials(1000, "Python Basics", "Operations, Conditional Statements", course1)
tut2 = Tutorials(2000, "Python AI", "Machine Learning, Object Detection", course3)

# Check if a course is present or not with a specific ID
# res = Courses.checkCourse(101)
# print(res)
# print("-----------")

# # Change the name of the course
# if res != -1:
#     res.setCourseName("Python API")

# print(res)

# res = Tutorials.fetchTutorials(101)
# for tutorial in res:
#     print(tutorial.getTutorialName())

for course in Courses.courses:
    if course.getInstructor().getName() == "ABC":
        print(course.getCourseName())