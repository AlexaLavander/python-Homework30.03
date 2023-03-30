class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредння оценка за домашние задания: {self.middle_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        print

    def __str__(self):
        str = f'Имя: {self.name}\nФамилия: {self.surname}'
        return str


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        str = f'Имя: {self.name}\nФамилия: {self.surname}\nСредння оценка за лекции: {self.middle_grade}'
        return str


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_reviewer = Reviewer("Some", "Buddy")
some_reviewer.courses_attached += ['Python']

some_reviewer._Reviewer__rate_hw(best_student, 'Python', 10)
some_reviewer._Reviewer__rate_hw(best_student, 'Python', 10)
some_reviewer._Reviewer__rate_hw(best_student, 'Python', 10)

best_student.rate_lecturer(some_lecturer, 'Python', 10)
best_student.rate_lecturer(some_lecturer, 'Python', 10)
best_student.rate_lecturer(some_lecturer, 'Python', 10)

best_student.add_courses('Введение в программирование')


def count_middle_grade(self):
    for grades in self.grades:
        count = len(self.grades[grades])
        sum_of_grades = sum(self.grades[grades])
        return sum_of_grades / count


best_student.middle_grade = count_middle_grade(best_student)
some_lecturer.middle_grade = count_middle_grade(some_lecturer)


def __lt__(middle_grade, middle_rate):
    if middle_rate > middle_grade:
        return middle_grade < middle_rate
    elif middle_rate < middle_grade:
        return middle_grade > middle_rate
    else:
        return middle_grade == middle_rate


print(some_reviewer)
print()
print(some_lecturer)
print()
print(best_student)
print()

print("Полевые испытания")
girl_student = Student("Linda", "Bard", "Female")
boy_student = Student("Barny", "Kendall", "Male")

mentor_best = Mentor("Best", "Mentor")
mentor_looser = Mentor("Looser", "Mentor")

timid_reviewer = Reviewer("Timid", "Reviewer")
confident_reviewer = Reviewer("Confident", "Reviewer")

happy_lecturer = Lecturer("Hapy", "Lecturer")
sad_lecturer = Lecturer("Sad", "Lecturer")
happy_lecturer.courses_attached += ["Python"]
sad_lecturer.courses_attached += ["Python"]

timid_reviewer.courses_attached += ["Python"]
confident_reviewer.courses_attached += ["Python"]

girl_student.add_courses("Python")
boy_student.add_courses("Python")

girl_student.rate_lecturer(happy_lecturer, "Python", 10)
boy_student.rate_lecturer(sad_lecturer, "Python", 10)

girl_student.courses_in_progress += ["Python"]
boy_student.courses_in_progress += ["Python"]

timid_reviewer._Reviewer__rate_hw(girl_student, 'Python', 10)
confident_reviewer._Reviewer__rate_hw(boy_student, "Python", 10)

girl_student.middle_grade = count_middle_grade(girl_student)
boy_student.middle_grade = count_middle_grade(boy_student)
print(count_middle_grade(girl_student) == count_middle_grade(happy_lecturer))

students_list = [girl_student, boy_student, best_student]


def middle_grades_course(students_list, course):
    grades_list = []
    sum_grades = 0
    for student in students_list:
        if student.courses_in_progress.__contains__(course) or student.finished_courses.__contains__(course):
            grades_list.append(student.grades[course])
        else:
            return 0
    count = len(grades_list)
    sum_grades = sum(student.grades[course])
    return sum_grades / count


fun = middle_grades_course(students_list, "Python")
print(f"1 функция: {fun}")

lecturers_list = [happy_lecturer, sad_lecturer, some_lecturer]


def middle_lecturers_grades_course(lecturers_list, course):
    grades_list = []
    sum_grades = 0
    for lecturer in lecturers_list:
        if lecturer.courses_attached.__contains__(course):
            grades_list.append(lecturer.grades[course])
        else:
            return 0
    count = len(grades_list)
    sum_grades = sum(lecturer.grades[course])
    return sum_grades / count


fun2 = middle_lecturers_grades_course(lecturers_list, "Python")
print(f"2 функция: {fun2}")