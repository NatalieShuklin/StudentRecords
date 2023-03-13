from __future__ import print_function

dataset = [{'Major': 'Biology', 'GPA': '2.4', 'Name': 'Edward'}, {'Major': 'Physics', 'GPA': '2.9', 'Name': 'Emily'},
           {'Major': 'Mathematics', 'GPA': '3.5', 'Name': 'Sarah'}]



class Student:

    def __init__(self, name, age):
        self.student_name = name
        self.age = age

    def set_info(self, name, age):
        self.student_name = name
        self.age = age

    def get_name(self):
        return self.student_name

    def get_age(self):
        return self.age

    def __repr__(self):
        return self.student_name


class Record:

    def __init__(self, courses, grades):
        # self.student = student
        self.courses = courses
        self.grades = grades

    def get_grades(self):
        return self.grades

    def get_courses(self):
        return self.courses

    def __repr__(self):
        s = "grades: "
        for g in self.grades:
            s += str(g)
            s += " "
        s += "courses: "
        s += str(self.courses)
        return s


class RecordsTable:
    index = 0

    def __init__(self):
        self.records = {}

    def add_student(self, name, age, courses, grades):
        s = Student(name, age)
        r = Record(courses, grades)

        self.records[s.student_name] = r
        self.index += 1

    def display(self):
        for k in self.records:
            print(k, " ", self.records[k])

    def search(self, st):
        return self.records[st.student_name]


# ==============================================================================

# List of dicts of students



students = []
student = {}


def menu():
    print('Enter an option of your choice')
    print('1 Add students\n2 Delete students \n3 Find student \n4 Exit')
    option = input('= ')
    if option == '1':
        add()
    elif option == '2':
        delstu()
    elif option == '3':
        findstu()
    elif option == '4':
        print('Good bye')
    else:
        while option != '1' or option != '2' or option != '3':
            print('Invalid entry, enter again')
            option = input('= ')


def add():
    num = int(input('how many students do you want to enroll?'))
    for i in range(num):
        student = {}
        student['Name'] = input('Enter student Name: ')
        student['number'] = input('Enter roll number: ')
        student['quarter'] = input('Enter quarter: ')
        students.append(student)
    print('Number of students enrolled: ', len(students))
    print('press any key to go back to menu')
    goto_menu = input()
    menu()


def delstu():
    delname = input('Enter the name of the student whose data you want to delete')
    for student in students:
        if student['Name'] == delname:
            del student['Name']
            del student['number']
            del student['quarter']
    goto_menu = input('Enter any key to go back')
    menu()


def findstu():
    findname = input('Enter student name to get his data: ')
    for student in students:
        if student['Name'] == findname:
            print(student)
    goto_menu = input('Enter any key to go back')
    menu()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    r = RecordsTable()
    s1 = Student("n", 31)
    s2 = Student("n", 31)
    r1 = Record(["gg", "gg"], [99, 100])
    r2 = Record(["a", "b"], [100, 100])

    r.add_student(s1.student_name, s1.age, r1.courses, r1.grades)
    r.add_student(s2.student_name, s2.age, r2.courses, r2.grades)

    # r.display()
    # ==============================================================================

    print('Welcome to student management')
    menu()
    [print("%s %s: %s\n" % (item['Name'], item['Major'], item['GPA'])) for item in dataset]
