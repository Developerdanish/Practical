from pickle import dump, load


class EMPLOYEE:
    def __init__(self):
        self.Eno = ''
        self.EName =''

    def show(self):
        print "Employee number:- ", self.Eno
        print "Employee name:- ", self.EName

    def In(self):
        self.Eno = raw_input("ENO:- ")
        self.EName = raw_input("ENAME:- ")
        


def write_stu():
    f = open('employee', 'a')
    ob = EMPLOYEE()
    ob.In()
    dump(ob, f)
    print 'Record added successful'
    f.close()


def read_stu():
    fil = open('employee', 'rb')
    ob = EMPLOYEE()
    ob.show()
    try:
        while True:
            ob = load(fil)
            ob.show()
    except EOFError:
        fil.close()

read_stu()




