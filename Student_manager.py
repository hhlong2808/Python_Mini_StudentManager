import os

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
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
        self.students: list[Student] = []

    def add_student(self, student):
        if Student.valid_gpa(student.gpa):
            self.students.append(student)
        else:
            print(f"Warning: Invalid GPA for {student.name}. Cannot add to system.")

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
    
    def load_from_file(self, filename: str) -> None:
        """Read the student list from a text file."""
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return

        # Use 'with open' to automatically close the file after reading, preventing memory leaks
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip() 
                if not line:        
                    continue
                
                try:
                    # Split the string based on commas
                    parts = line.split(',')
                    
                    # Clean data: Remove extra whitespaces and quotes from the name
                    name = parts[0].strip().strip('"').strip("'")
                    age = int(parts[1].strip())     
                    gpa = float(parts[2].strip())   
                    
                    # Create an object and add it to the list
                    student = Student(name, age, gpa)
                    self.add_student(student)
                    
                except (IndexError, ValueError):
                    # Catch errors if the line is missing data or has incorrect text/number formats
                    print(f"Skipping line {line_number} due to wrong format: {line}")
                    
        print(f"-> Finished reading data from '{filename}'.")

    def save_to_file(self, filename: str) -> None:
        """Export the current student list to a file."""
        with open(filename, 'w', encoding='utf-8') as file:
            for s in self.students:
                # Format the string exactly as required: "Name", Age, GPA
                line = f'"{s.name}", {s.age}, {s.gpa}\n'
                file.write(line)
                
        print(f"-> Finished saving data to '{filename}'.")
    
    

with open("input.txt", 'w', encoding='utf-8') as f:
    f.write('"Long", 19, 4.0\n')
    f.write('"Vinh", 18, 3.6\n')
    f.write('Sai Dinh Dang, muoi_tam, 3.0\n') # This line will be caught as an error and skipped
    f.write('"Lam", 18, 3.2\n')

# 2. Initialize Manager and run tests
manager = Manager()

print("--- LOADING FILE ---")
manager.load_from_file("input.txt")

print("\n--- STUDENT LIST AFTER LOADING ---")
manager.show_student()

print("\n--- SAVING TO NEW FILE ---")
# Manually add a student before exporting to the file
manager.add_student(Student("Do", 18, 2.8))
print("\n--- FINDING STUDENTS ---")
manager.find_student("Vinh")  # Will print information of Vinh
manager.find_student("Hieu")  # Will report not found (Not found)

print("\n--- DELETING STUDENT ---")
manager.del_student("Long")   # Delete Long from the list
manager.show_student()        # Print the list again to check if Long has been removed
manager.save_to_file("output.txt")