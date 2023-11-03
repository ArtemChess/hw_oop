class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}
        Student.student_list.append(self)

    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def grades_average(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades_student:
            grades_count += len(self.grades_student[grade])
            grades_sum += sum(self.grades_student[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваются объекты разных классов')
            return
        return self.grades_average() > other.grades_average()

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваются объекты разных классов')
            return
        return self.grades_average() < other.grades_average()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Сравниваются объекты разных классов')
            return
        return self.grades_average() == other.grades_average()

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {round(self.grades_average(), 0)}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_lecturer = {}
        Lecturer.lecturer_list.append(self)

    def grades_average_(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades_lecturer:
            grades_count += len(self.grades_lecturer[grade])
            grades_sum += sum(self.grades_lecturer[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравниваются объекты разных классов')
            return
        return self.grades_average_() > other.grades_average_()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравниваются объекты разных классов')
            return
        return self.grades_average_() < other.grades_average_()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравниваются объекты разных классов')
            return
        return self.grades_average_() == other.grades_average_()

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {round(self.grades_average_(), 0)}\n")


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")


def courses_average_students(student_list, course):
    for student in student_list:
        for cours_name, average in student.grades_student.items():
            if course == cours_name:
                sum_average = sum(average) / len(average)
                print(f"Студент: {student.name} {student.surname}\n"
                      f"Курс: {cours_name}\n"
                      f"Cредняя оценка за домашние задания: {round(sum_average, 0)}\n")


def courses_average_lecturer(lecturer_list, course):
    for lecturer in lecturer_list:
        for cours_name, average in lecturer.grades_lecturer.items():
            if course == cours_name:
                sum_average = sum(average) / len(average)
                print(f"Лектор: {lecturer.name} {lecturer.surname}\n"
                      f"Курс: {cours_name}\n"
                      f"Cредняя оценка за домашние задания: {round(sum_average, 0)}\n")


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.courses_in_progress += ['C++']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Joe', 'Parker', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['C++']
student_2.finished_courses += ['Введение в программирование']

mentor_reviewer_1 = Reviewer('Some', 'Buddy')
mentor_reviewer_1.courses_attached += ['Python']
mentor_reviewer_1.courses_attached += ['Git']
mentor_reviewer_1.courses_attached += ['C++']

mentor_reviewer_2 = Reviewer('Some', 'Buddy')
mentor_reviewer_2.courses_attached += ['Python']
mentor_reviewer_2.courses_attached += ['Git']
mentor_reviewer_2.courses_attached += ['C++']

mentor_lecturer_1 = Lecturer('Ivan', 'Ivanov')
mentor_lecturer_1.courses_attached += ['Python']
mentor_lecturer_1.courses_attached += ['Git']
mentor_lecturer_1.courses_attached += ['C++']

mentor_lecturer_2 = Lecturer('Katherine', 'Petrova')
mentor_lecturer_2.courses_attached += ['Python']
mentor_lecturer_2.courses_attached += ['Git']
mentor_lecturer_2.courses_attached += ['C++']

mentor_reviewer_1.rate_hw_student(student_1, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_1, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_1, 'Python', 8)
mentor_reviewer_1.rate_hw_student(student_1, 'Git', 10)
mentor_reviewer_1.rate_hw_student(student_1, 'C++', 7)

mentor_reviewer_1.rate_hw_student(student_2, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_2, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_2, 'Python', 8)
mentor_reviewer_1.rate_hw_student(student_2, 'Git', 10)
mentor_reviewer_1.rate_hw_student(student_2, 'C++', 8)

student_1.rate_hw_lecturer(mentor_lecturer_1, 'Python', 10)
student_1.rate_hw_lecturer(mentor_lecturer_1, 'Python', 10)
student_1.rate_hw_lecturer(mentor_lecturer_1, 'Python', 7)
student_1.rate_hw_lecturer(mentor_lecturer_1, 'Git', 6)

student_2.rate_hw_lecturer(mentor_lecturer_2, 'Python', 10)
student_2.rate_hw_lecturer(mentor_lecturer_2, 'Python', 10)
student_2.rate_hw_lecturer(mentor_lecturer_2, 'Python', 7)
student_2.rate_hw_lecturer(mentor_lecturer_2, 'Git', 9)

print(f'Оценки студента {student_1.name} {student_1.surname}: ',
      *[f"{key}: {', '.join(map(str, value))}" for key, value in student_1.grades_student.items()])
print(f'Оценки студента {student_2.name} {student_2.surname}: ',
      *[f"{key}: {', '.join(map(str, value))}" for key, value in student_2.grades_student.items()])
print(f'Курсы студента {student_1.name} {student_1.surname}: ', ', '.join(student_1.courses_in_progress))
print(f'Курсы студента {student_2.name} {student_2.surname}: ', ', '.join(student_2.courses_in_progress))

print(f'Оценки лектора {mentor_lecturer_1.name} {mentor_lecturer_1.surname}: ',
      *[f"{key}: {', '.join(map(str, value))}" for key, value in mentor_lecturer_1.grades_lecturer.items()])
print(f'Оценки лектора {mentor_lecturer_2.name} {mentor_lecturer_2.surname}: ',
      *[f"{key}: {', '.join(map(str, value))}" for key, value in mentor_lecturer_2.grades_lecturer.items()])
print()

print(mentor_reviewer_1)
print(mentor_lecturer_1)
print(mentor_lecturer_2)
print(student_1)
print(student_2)

if student_1 > student_2:
    print(
        f'Средняя оценка {student_1.name} {student_1.surname} больше, чем средняя оценка {student_2.name} {student_2.surname}')
elif student_1 < student_2:
    print(
        f'Средняя оценка {student_1.name} {student_1.surname} меньше, чем средняя оценка {student_2.name} {student_2.surname}')
else:
    print(
        f'Средняя оценка {student_1.name} {student_1.surname}  равна средней оценке {student_2.name} {student_2.surname}')
print()

if mentor_lecturer_1 > mentor_lecturer_1:
    print(
        f'Средняя оценка {mentor_lecturer_1.name} {mentor_lecturer_1.surname} больше, чем средняя оценка {mentor_lecturer_2.name} {mentor_lecturer_2.surname}')
elif mentor_lecturer_1 < mentor_lecturer_1:
    print(
        f'Средняя оценка {mentor_lecturer_1.name} {mentor_lecturer_1.surname} меньше, чем средняя оценка {mentor_lecturer_2.name} {mentor_lecturer_2.surname}')
else:
    print(
        f'Средняя оценка {mentor_lecturer_1.name} {mentor_lecturer_1.surname}  равна средней оценке {mentor_lecturer_2.name} {mentor_lecturer_2.surname}')
print()

courses_average_students(Student.student_list, 'Python')
courses_average_lecturer(Lecturer.lecturer_list, 'Git')
