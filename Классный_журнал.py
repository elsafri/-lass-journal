class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def list(self, student):
        if isinstance(student,Student):
            students.append(student)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self, course_name):
        sum = 0
        value = []
        if course_name == 'Python':
           value = self.grades.get("Python")
        if course_name == 'Git':
           value = self.grades.get("Git")
        for marks in value:
            sum += marks
        return round(sum/len(value),1)



    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка! Не является студентом!')
            return
        return self.average_grade("Python") < other.average_grade("Python")

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания:{self.average_grade("Python")}' \
              f'\nКурсы в процессе изучения:{",".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы:{",".join(self.finished_courses)}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def average_grade(self, course_name):
        sum = 0
        value = []
        if course_name == 'Python':
            value = self.grades.get("Python")
        if course_name == 'Git':
            value = self.grades.get("Git")
        for marks in value:
            sum += marks
        return round(sum / len(value), 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка! Не является лектором!')
            return
        return self.average_grade("Python") < other.average_grade("Git")

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции:{self.average_grade("Git")}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия:{self.surname}'
        return res
some_lecturer = Lecturer('Some','Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

other_lecturer = Lecturer('Jhon','Smith')
other_lecturer.courses_attached += ['Git']
other_lecturer.courses_attached += ['Python']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']
some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 9.6)
some_student.rate_hw(other_lecturer, 'Git', 10)
some_student.rate_hw(other_lecturer, 'Git', 10)
some_student.rate_hw(some_lecturer, 'Git', 10)
some_student.rate_hw(some_lecturer, 'Git', 10)
some_student.rate_hw(other_lecturer, 'Python', 10)
some_student.rate_hw(other_lecturer, 'Python', 10)

other_student = Student('Emma','Gane','female')
other_student.courses_in_progress += ['Python']
other_student.courses_in_progress += ['Git']
other_student.finished_courses += ['Введение в программирование']
other_student.rate_hw(some_lecturer, 'Git', 10)
other_student.rate_hw(some_lecturer, 'Git', 9.6)
other_student.rate_hw(some_lecturer, 'Python', 9)
other_student.rate_hw(some_lecturer, 'Python', 9)


some_reviewer = Reviewer('Some','Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9.6)
some_reviewer.rate_hw(other_student, 'Python', 10)
some_reviewer.rate_hw(other_student, 'Python', 10)
some_reviewer.rate_hw(other_student, 'Python', 10)
some_reviewer.rate_hw(other_student, 'Python', 10)

other_reviewer = Reviewer('Richard','Black')
other_reviewer.courses_attached += ['Git']
other_reviewer.rate_hw(some_student, 'Git', 10)
other_reviewer.rate_hw(some_student, 'Git', 8)
other_reviewer.rate_hw(some_student, 'Git', 9)
other_reviewer.rate_hw(some_student, 'Git', 9)
other_reviewer.rate_hw(other_student, 'Git', 10)
other_reviewer.rate_hw(other_student, 'Git', 10)
other_reviewer.rate_hw(other_student, 'Git', 9)
other_reviewer.rate_hw(other_student, 'Git', 9)

students = [some_student, other_student]
lecturers = [some_lecturer, other_lecturer]
def average_rating_students(students, course_name):
    av_sum = 0
    if course_name == 'Python':
        for student in students:
           av_sum += Student.average_grade(student,"Python")
    if course_name == 'Git':
        for student in students:
           av_sum += Student.average_grade(student,"Git")
    print(round(av_sum/len(students),1))

def average_rating_lecrturer(lecturers, course_name):
    av_sum = 0
    if course_name == 'Python':
        for lecturer in lecturers:
           av_sum += Lecturer.average_grade(lecturer, "Python")
    if course_name == 'Git':
        for lecturer in lecturers:
           av_sum += Lecturer.average_grade(lecturer, "Git")
    print(round(av_sum/len(lecturers),1))




print(some_lecturer)
print(other_lecturer)
print(some_reviewer)
print(other_reviewer)
print(some_student)
print(other_student)
print(some_student>other_student)
print(some_lecturer<other_lecturer)
average_rating_students(students, 'Git')
average_rating_lecrturer(lecturers,"Python")