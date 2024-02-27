import math

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
                    print("Number of students must be greater than 0")
            except ValueError:
                print("Invalid input")

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
                number = int(input("Enter the number of courses: "))
                if number > 0:
                    return number
                else:
                    print("Number of courses must be greater than 0")
            except ValueError:
                print("Invalid input")

    def input_course_info(self):
        course_id = input("ID of course: ")
        course_name = input("Course name: ")
        course = Course(course_id, course_name)
        return course

    def input_student_marks(self, students, course):
        course_id = course.course_id
        if course_id not in courses:
            print("Course does not exist")
            return
        for student in students:
            while True:
                try:
                    student_marks = float(input(f"Marks for student {student.student_name} in course {course_id}: "))
                    if 0 <= student_marks <= 20:
                        course.add_student_marks(student.student_id, math.floor(student_marks))
                        break
                    else:
                        print("Marks should be between 0 and 20")
                except ValueError:
                    print("Invalid input. Marks should be a number")

    def list_courses(self, courses):
        print("List of courses:")
        for course_id, course in courses.items():
            print(f"Course ID: {course_id}, Course Name: {course.course_name}")

    def list_students(self, students):
        print("List of students:")
        for student in students:
            print(f"Student ID: {student.student_id}, Student Name: {student.student_name}, Date of Birth: {student.student_dob}")

    def show_student_marks(self, students, courses):
        course_id = input("Enter the course ID to show student marks: ")
        if course_id not in courses:
            print("Course does not exist")
            return

        print("\n" + "-" * 58)
        print(f"Marks for course {course_id}:\n{"-" * 58}")
        print("| Student ID | Student Name             | Marks |")
        print("|------------|--------------------------|-------|")
        for student in students:
            if student.student_id in courses[course_id].marks:
                marks = courses[course_id].marks[student.student_id]
                print(f"| {student.student_id:<10} | {student.student_name:<24} | {marks:<5} |")
        print("-" * 58)

    def calculate_average_gpa(self, student, courses):
        credits = []
        for course in courses.values():
            if student.student_id in course.marks:
                credits.append(3)  
        total_credits = sum(credits)
        weighted_sum = sum(credits[i] * course.marks[student.student_id] for i, course in enumerate(courses.values()) if student.student_id in course.marks)
        gpa = weighted_sum / total_credits
        return round(gpa, 1)

    def sort_students_by_gpa(self, students, courses):
        return sorted(students, key=lambda student: self.calculate_average_gpa(student, courses), reverse=True)



university = University()
students = []
courses = {}

number_of_students = university.input_number_of_students()
for _ in range(number_of_students):
    student_id, student_name, student_dob = university.input_student_info()
    student = Student(student_id, student_name, student_dob)
    students.append(student)

number_of_courses = university.input_number_of_courses()
for _ in range(number_of_courses):
    course = university.input_course_info()
    courses[course.course_id] = course

university.list_students(students)
university.list_courses(courses)

for course in courses.values():
    university.input_student_marks(students, course)

university.show_student_marks(students, courses)

sorted_students = university.sort_students_by_gpa(students, courses)
print("\nStudents sorted by GPA (descending):")
for student in sorted_students:
    gpa = university.calculate_average_gpa(student, courses)
    print(f"Student ID: {student.student_id}, Student Name: {student.student_name}, GPA: {gpa}")
