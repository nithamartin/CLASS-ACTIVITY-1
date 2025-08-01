class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Grade: {self.grade}, Age: {self.age}")

# Create an object
student1 = Student("Alice", "A", 20)
student2 = Student("John", "B", 21)
student1.display()
student2.display()