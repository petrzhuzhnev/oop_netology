class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.sr_summ = 0

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def _summ_rate(self):
        total = 0
        for i in self.grades.keys():
            for j in self.grades[i]:
                total += j
            sr = total/(len(self.grades[i]))
        self.sr_summ = sr


    def __str__(self):
        ref = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.sr_summ}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n'
        return ref

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Этот учебные персонаж не из этого класса")
            return
        return self.sr_summ < other.sr_summ
    #
    def __gt__(self, other):
        if not isinstance(other, Student):
            print("Этот учебные персонаж не из этого класса")
        return self.sr_summ > other.sr_summ



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor): #эксперт проверяющий домашнее задание

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        ref = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return ref

class Lecturer(Mentor): #лектор
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_for_student = {}
        self.sr_summ = 0

    def rate_lecture(self, student, course, grade):
        if course in student.courses_in_progress and course in self.courses_attached:
            for i in self.courses_attached:
                if course in self.grade_for_student:
                    self.grade_for_student[course] += [grade]  #.update({course:[grade]})
                else:
                    self.grade_for_student[course] = [grade]
        else:
            print('Этот лектор не вел лекции у этого студента')

    def _summ_rate(self):
        total = 0
        for i in self.grade_for_student.keys():
            for j in self.grade_for_student[i]:
                total += j
            sr = total/(len(self.grade_for_student[i]))
        self.sr_summ = sr



    def __str__(self):
        ref = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.sr_summ}\n'
        return ref

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Этот учебные персонаж не ЛЕКТОР")
            return
        return self.sr_summ < other.sr_summ

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print("Этот учебные персонаж не ЛЕКТОР")
            return
        return self.sr_summ > other.sr_summ


student_1 = Student('Petr', 'Zhuzhnev', 'man')
student_1.courses_in_progress += ['Python']
student_2 = Student('Andrew', 'Ilin', 'man')
student_2.courses_in_progress += ['Git']
student_3 = Student('Ruslan', 'Ivanov', 'man')
student_3.courses_in_progress += ['Git', 'Python']
print(student_1)

reviever_1 = Reviewer('Пайтон', 'Пайтонович')
reviever_1.courses_attached += ['Python']

reviever_2 = Reviewer('Гит', 'Гитович')
reviever_2.courses_attached += ['Git']


lecturer_1 = Lecturer('Пайтон', 'Пайтонович')
lecturer_1.courses_attached = reviever_1.courses_attached
lecturer_1.rate_lecture(student_3, 'Python', 10)

lecturer_1.rate_lecture(student_1, 'Python', 10)
lecturer_1.rate_lecture(student_2, 'Python', 8)
lecturer_1.rate_lecture(student_1, 'Python', 5)
lecturer_1._summ_rate()
print(lecturer_1)


# print(dir(cool_mentor)) #словарик методов
# print(type(cool_mentor)) #тип
# print(Reviewer.mro()) #список наслеования "method resolution order" «порядок разрешения методов»
reviever_1.rate_hw(student_1, 'Python', 10)
reviever_1.rate_hw(student_2, 'Python', 5)
reviever_1.rate_hw(student_3, 'Python', 10)
reviever_2.rate_hw(student_1, 'Git', 5)
reviever_2.rate_hw(student_2, 'Git', 10)
reviever_2.rate_hw(student_3, 'Git', 2)
reviever_1.rate_hw(student_1, 'Python', 5)
reviever_1.rate_hw(student_2, 'Python', 2)
reviever_1.rate_hw(student_3, 'Python', 8)
reviever_2.rate_hw(student_1, 'Git', 7)
reviever_2.rate_hw(student_2, 'Git', 5)
reviever_2.rate_hw(student_3, 'Git', 3)
print(reviever_1)

student_1._summ_rate()
student_2._summ_rate()
student_3._summ_rate()
lecturer_1._summ_rate()


print(student_1 > lecturer_1)
print(student_1 < lecturer_1)
student_2 < lecturer_1
lecturer_1 < student_3


print(type(lecturer_1.sr_summ))
print(type(student_1.sr_summ))