class Person:
    def __init__(self):
        self.name = ""
        self.age = ''

    def out(self):
        print self.name
        print self.age

    def inp(self):
        self.name = raw_input("NAME:- ")
        self.age = raw_input("AGE:- ")


class Stu(Person):
    def __init__(self):
        Person.__init__(self)
        self.school = ''
        self.Class = 0

    def show(self):
        Person.out(self)
        print self.school
        print self.Class

    def In(self):
        Person.inp(self)
        self.school = raw_input("SCHOOL:- ")
        self.Class = input("CLASS:- ")


OB = Stu()
OB.In()
OB.show()
