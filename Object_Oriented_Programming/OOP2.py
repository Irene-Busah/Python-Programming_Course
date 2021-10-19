# Object-Oriented Programming

class SchoolMember:
    """Initializing the base class
    contain common attributes of a member of a school
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print("{} is a member of the school".format(self.name))

    def tell(self):
        """Introducing yourself"""
        print('Name: "{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    """Initializing a sub-class to contain specific attributes"""

    def __init__(self, name, age, salary, faculty):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        self.faculty = faculty
        print("I am {}, a staff of ALU".format(self.name))
        print("I work in the {} faculty".format(faculty))

    def tell(self):
        """Introducing yourself as a teacher with specific info"""
        SchoolMember.tell(self)
        print("I receive {} as my salary".format(self.salary))


class Student(SchoolMember):
    """Initializing another sub-class to contain specific attribute"""

    def __init__(self, name, age, course):
        SchoolMember.__init__(self, name, age)
        self.course = course
        print("{} is a student of the ALU".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("I'm pursuing {}".format(self.course))


status = input("what is your status in ALU(student or staff)? ")
if status == 'staff':
    staff1 = input("What is name? ")
    age1 = input("Enter your age: ")
    salary1 = input("Enter your salary: ")
    faculty1 = input("Enter your your department: ")
    staff = Teacher(staff1, age1, salary1, faculty1)
    members = [staff]
    for member in members:
        member.tell()

elif status == 'student':
    student1 = input("Enter your name: ")
    age2 = input("Enter your age: ")
    course1 = input("Enter the course you're offering: ")
    student = Student(student1, age2, course1)
    members = [student]
    for member in members:
        member.tell()

print()


