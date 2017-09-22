def EmpSearch(empno, dict):
    key = dict.keys()
    to_search = 0
    if empno in key:
        to_search = 1
    if to_search:
        print "Employee details are:- "
        print dict[empno]
    else:
        print "Employ does not exist"


D = {}
n = input("Enter no. of employ:- ")
print "Enter details of ",n,"employee 1 by 1"
for i in range(n):
    print
    empNo = input("Number:- ")
    empName = raw_input("Name:- ")
    D[empNo] = empName
to_search = input("Enter employee number to search:- ")
EmpSearch(to_search, D)