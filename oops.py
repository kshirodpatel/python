class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student) 

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Tim", 50, 100)
s2 = Student("Kevin", 10, 75)
s3 = Student("Jane", 89, 67)

course = Course("Science", 1000)
course.add_students(s1)

print(course.get_average_grade())