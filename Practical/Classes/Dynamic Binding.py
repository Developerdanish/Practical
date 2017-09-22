class TEST:
    pass


def fun():
    print "Dynamic binding"


ob = TEST()
ob.x = fun  # binds function fun exclusively only for object ob
ob.x()
print vars(ob)
