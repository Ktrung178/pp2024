def is_valid_name(name):
    if any(char.isdigit() for char in name):
        print("nam has number. write again")
        return False
    return True

def validate_date_of_birth():
    while True:
        dob = input("date of birth (DD/MM/YYYY): ")
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
                        print("less than 30 days and more than 1 day")
                else:
                    if 1 <= day <= 31:
                        return dob
                    else:
                        print("less than 31 days and more than 1 day")
            else:
                print("Invalid year or month!")
        except ValueError:
            print("Invalid date format!")


def input_number_of_students():
    while True:
        try:
            number = int(input("Enter the number of students  "))
            if number > 0:
                return number
            else:
                print("not empty or less than 0")
                return 1
        except ValueError:
            print("not satify")
     
    return int(input("Enter the number of students "))

def input_student_info():
    student_id = input("ID of student ")
    while True:
        student_name = input("student name: ")
        if is_valid_name(student_name):
            break
    student_dob = validate_date_of_birth()
    return (student_id, student_name, student_dob)

def input_number_of_courses():
    return int(input("number of courses: "))

def input_course_info():
    course_id = input("ID of course ")
    course_name = input("course name: ")
    course_info = (course_id, course_name)
    return course_info

def input_student_marks(students, courses, course_info):
    course_id = course_info[0]  
    if course_id not in courses:
        print("Course not true")
        return
    marks = {}
    for student in students:
        while True:
            try:
                student_marks = float(input(f"marks for student {student[1]} in course {course_id}: "))
                if 0 <= student_marks <= 20:
                    marks[student[0]] = student_marks
                    break
                else:
                    print("0 < mark < 20")
            except ValueError:
                print("input must be number")
    courses[course_id]["marks"] = marks  

def list_courses(courses):
    print("List : courses")
    for course_id, course_info in courses.items():
        print(f"Course ID: {course_id}, Course Name: {course_info['name']}")

def list_students(students):
    print("list of students:")
    for student in students:
        print(f"Student ID: {student[0]}, Student Name: {student[1]}, Date of Birth: {student[2]}")

def show_student_marks(students, courses):
    course_id = input("the course ID to show student marks: ")
    if course_id not in courses:
        print("no course")
        return
    
    print("\n" + "-" * 58)
    print(f"| {'Student ID':<12} | {'Student Name':<15} | {'Date of Birth':<13} | {'Marks':<5} |")
    print("|" + "-" * 56 + "|")
    
    if "marks" in courses[course_id]:
        marks = courses[course_id]["marks"]
        for student in students:
            student_id = student[0]
            student_name = student[1]
            student_dob = student[2]
            if student_id in marks:
                student_marks = marks[student_id]
                print(f"| {student_id:<12} | {student_name:<15} | {student_dob:<13} | {student_marks:<5} |")
            else:
                print(f"| {student_id:<12} | {student_name:<15} | {student_dob:<13} | Not available |")
    else:
        print("|" + " " * 65 + "|")
        print("| No marks " + " " * 39 + "|")
    
    print("-" * 58)


students = []
courses = {}

num_students = input_number_of_students()
for _ in range(num_students):
    student_info = input_student_info()
    students.append(student_info)

num_courses = input_number_of_courses()
for _ in range(num_courses):
    course_info = input_course_info()
    courses[course_info[0]] = {"name": course_info[1]}  
    input_student_marks(students, courses, course_info)  

list_courses(courses)
list_students(students)
show_student_marks(students, courses)
