class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Students(Person):
    school = "MIT"
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | GPA: {self.gpa} | School: {self.school}"
    
    @staticmethod
    def valid_gpa(gpa):
        return 0<=gpa<=4
    
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
    
class Manager():
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if Students.valid_gpa(student.gpa):
            self.students.append(student)
        else:
            raise ValueError(f"Invalid GPA. {student.name}'s GPA is invalid")

    def show_student(self, arrange=None):
        students = self.students
        if arrange == "increase":
            print("Students list in increasing order:")
            students = sorted(self.students, key=lambda x: (x.gpa, x.name, x.age))
        elif arrange == "decrease":
            print("Students list in decreasing order:")
            students = sorted(self.students, key=lambda x: (-x.gpa, x.name, x.age))
        for s in students:
            print(s)
        
    
    def find_student(self, name):
        for s in self.students:
            if s.name == name:
                print(f"Found {name} - {s}")
                return
        print(f"Not found {name}")
    
    def del_student(self, name):
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                print(f"Deleted {name}")
                return
        print(f"Not found {name}")
        

manager = Manager()
Students.change_school("PTIT")
s1 = Students("Long", 19, 4)
s2 = Students("Vinh", 18, 3.6)
s3 = Students("Lam", 18, 3.2)
s4 = Students("Do", 18, 2.8)
s5 = Students("Mixi", 20, 3.2)

manager.add_student(s1)
manager.add_student(s2)
manager.add_student(s3)
manager.add_student(s4)
manager.add_student(s5)

manager.show_student("decrease")