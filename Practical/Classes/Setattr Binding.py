def FO(self):
    print "Outside Class"


class TEST:
    def FI(self):
        print "Inside class"



ob = TEST()
setattr(TEST, 'NEW', FO)   # Binds function FO for entire class and each object can access it
ob.FI()
ob.NEW()
print vars(TEST)
