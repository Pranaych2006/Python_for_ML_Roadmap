class Student:
    def __init__(self, name,roll_number,courses):
        self.name = name
        self.roll_number = roll_number
        self.courses = courses

    def add_course(self,course_name):
        self.courses = course_name
    
    def get_course(self):
        return self.courses
    
    def get_details(self):
        print(f"Name : '{self.name}'")
        print(f"Roll number : {self.roll_number}")
        print(f"Courses : {self.courses}")


S = Student("Pranay",16,["Maths","Data structures"])
S.get_details()