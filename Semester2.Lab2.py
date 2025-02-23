class Student:
    def __init__(self, name=None, surname=None, birth_year=None, course=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.course = course

    def get_info(self):
        course_info = None if self.course >= 5 else self.course
        return f"І'мя: {self.name} {self.surname}, Рік Народження: {self.birth_year}, Курс: {course_info}"

    def get_names_list(self, students):
        return [f"{student.name} {student.surname}" for student in students]


class Online_Student(Student):
    def __init__(self, name=None, surname=None, birth_year=None, course=None, online_platform=None, in_Ukraine=None, device_used=None):
        super().__init__(name, surname, birth_year, course)
        self.online_platform = online_platform
        self.In_Ukraine = in_Ukraine
        self.device_used = device_used

    def _get_platform_info(self):
        return f"Online platform: {self.online_platform}"

    def __device_info(self):
        return f"Device used: {self.device_used}"

    def get_info(self):
        basic_info = super().get_info()
        platform_info = f", Платформа: {self.online_platform}"
        location_info = f", За кордоном: {'Так' if not self.In_Ukraine else 'Ні'}"
        return basic_info + platform_info + location_info


Student1 = Student("Віталій", "Книш", 2008, 2)
Student2 = Student("Васись", None, 2000, 5)
Student3 = Student("Петро", "Петренко", 2007, 2)

Student4 = Online_Student("Євген", "Сидоренко", 2006, 3, "Microsoft Teams", False, "ПК")
Student5 = Online_Student("Ангеліна", "Мирна", 2005, 4, "Zoom", True, "Ноутбук")

Students = [Student1, Student2, Student3, Student4, Student5]

Names_list = Student1.get_names_list(Students)

print(Names_list)
print(Student1.get_info())
print(Student2.get_info())
print(Student3.get_info())
print(Student4.get_info())
print(Student5.get_info())