from types import MethodType


class SAMPLE:
    def __init__(self, nm):
        self.name = nm


def play(self):
    print "Lets play", self.name


object = SAMPLE("DANISH")
object.x = MethodType(play, object)  # Binds function FO for entire class and each object
object.x()                           # can access it
print vars(SAMPLE)
