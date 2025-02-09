class Student:
    def __init__(self, name=None, surname=None, birth_year=None, manual_course=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.manual_course = manual_course
    def college_year_calc(self):
        college_year = 2010 - self.birth_year
        if college_year >= 5:
            return self.manual_course if self.manual_course is not None and 1 <= self.manual_course <= 4 else "невідомому"
        return college_year
    def get_names_list(self, students):
        return [f"{student.name} {student.surname}" for student in students]
    


Student1 = Student("Віталій", "Книш", 2008)
Student2 = Student("Васись", None, 2000)
Student3 = Student("Петро", "Петренко", 2007, 2)

Students = [Student1, Student2]
Names_list = Student1.get_names_list(Students)
print(Names_list) 

print(*vars(Student1).values())

print(f"Студент {Student1.name} {Student1.surname} знаходиться на {Student1.college_year_calc()} курсі.")
print(f"Студент {Student2.name} {Student2.surname} знаходиться на {Student2.college_year_calc()} курсі.")
print(f"Студент {Student3.name} {Student3.surname} знаходиться на {Student3.college_year_calc()} курсі.")