def menu():
    print '''
    STACK OPERATION MENU
    \n1.PUSH
    \n2.Pop
    \n3.Print
    \n4.Exit
    '''


class STACK:
    def __init__(self):
        self.stack = []

    def Push(self,Data):
        self.stack.append(Data)

    def POP(self):
        self.stack.pop()

    def Print(self):
        for i in range(len(self.stack)-1,-1,-1):
            print self.stack[i]


ob = STACK()
while True:
    menu()
    ch = input("\nENTER CHOICE:- ")
    if ch == 1:
        elements = input("How many elements u want to enter\n")
        print "Enter %s elements 1 by 1"%elements
        for i in range(elements):
            ob.Push(input(":- "))
    elif ch == 2:
        ob.POP()
    elif ch == 3:
        ob.Print()
    elif ch == 4:
        break
    else:
        print "Wrong Choice"










