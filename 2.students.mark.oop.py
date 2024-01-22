class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob

    def is_valid_name(self):
        if any(char.isdigit() for char in self.student_name):
            print("Name has a number. Please write again.")
            return False
        return True


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.marks = {}

    def add_student_marks(self, student_id, marks):
        self.marks[student_id] = marks


class University:
    def is_valid_name(self, name):
        if any(char.isdigit() for char in name):
            print("Name has a number. Please write again.")
            return False
        return True

    def validate_date_of_birth(self):
        while True:
            dob = input("Date of birth (DD/MM/YYYY): ")
            try:
                day, month, year = map(int, dob.split('/'))
                if 1990 <= year <= 2023 and 1 <= month <= 12:
                    if month == 2:
                        if 1 <= day <= 28:
                            return dob
                        else:
                            print("February has 28 days")
                    elif month in [4, 6, 9, 11]:
                        if 1 <= day <= 30:
                            return dob
                        else:
                            print("Month has less than 30 days and more than 1 day.")
                    else:
                        if 1 <= day <= 31:
                            return dob
                        else:
                            print("Month has less than 31 days and more than 1 day.")
                else:
                    print("Invalid year or month!")
            except ValueError:
                print("Invalid date format!")

    def input_number_of_students(self):
        while True:
            try:
                number = int(input("Enter the number of students: "))
                if number > 0:
                    return number
                else:
                    print("not empty or less than 0")
            except ValueError:
                print("not satify")

    def input_student_info(self):
        student_id = input("ID of student: ")
        while True:
            student_name = input("Student name: ")
            student = Student(student_id, student_name, "")
            if self.is_valid_name(student_name):
                break
        student_dob = self.validate_date_of_birth()
        return student_id, student_name, student_dob

    def input_number_of_courses(self):
        while True:
            try:
                number = int(input("Enter the number of courses "))
                if number > 0:
                    return number
                else:
                    print("cannot be empty or less than 0")
            except ValueError:
                print("Invalid ")

    def input_course_info(self):
        course_id = input("ID of course: ")
        course_name = input("Course name: ")
        course = Course(course_id, course_name)
        return course

    def input_student_marks(self, students, course):
        course_id = course.course_id
        if course_id not in courses:
            print("Course not true")
            return
        for student in students:
            while True:
                try:
                    student_marks = float(input(f"Marks for student {student.student_name} in course {course_id}: "))
                    if 0 <= student_marks <= 20:
                        course.add_student_marks(student.student_id, student_marks)
                        break
                    else:
                        print("0 < mark < 20")
                except ValueError:
                    print("input must be number")

    def list_courses(self, courses):
        print("List : courses")
        for course_id, course in courses.items():
            print(f"Course ID: {course_id}, Course Name: {course.course_name}")

    def list_students(self, students):
        print("list of students:")
        for student in students:
            print(f"Student ID: {student.student_id}, Student Name: {student.student_name}, Date of Birth: {student.student_dob}")

    def show_student_marks(self, students, courses):
        course_id = input("the course ID to show student marks: ")
        if course_id not in courses:
            print("no course")
            return

        print("\n" + "-" * 58)
        print(f"| {'Student ID':<12} | {'Student Name':<15} | {'Date of Birth':<12} | {'Marks':<5} |")
        print("|" + "-" * 56 + "|")

        course = courses[course_id]
        if course.marks:
            for student in students:
                student_id = student.student_id
                student_name = student.student_name
                student_dob = student.student_dob
                if student_id in course.marks:
                    student_marks = course.marks[student_id]
                    print(f"| {student_id:<12} | {student_name:<15} | {student_dob:<13} | {student_marks:<5} |")
                else:
                    print(f"| {student_id:<12} | {student_name:<15} | {student_dob:<13} | Not available |")
        else:
            print("|" + " " * 65 + "|")
            print("| No marks " + " " * 39 + "|")

        print("-" * 58)


university = University()

num_students = university.input_number_of_students()
students = []
for _ in range(num_students):
    student_info = university.input_student_info()
    student = Student(*student_info)
    students.append(student)

num_courses = university.input_number_of_courses()
courses = {}
for _ in range(num_courses):
    course = university.input_course_info()
    courses[course.course_id] = course
    university.input_student_marks(students, course)

university.list_courses(courses)
university.list_students(students)
university.show_student_marks(students, courses)
