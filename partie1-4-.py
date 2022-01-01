class Point:  #definition classe point
    a = 0
    b = 0

    def _init_(self, a=0, b=0):
        self.a = a
        self.b = b


class Segment:  #classe en utilisant classe point
    orig = Point(0, 0)
    extrem = Point(0, 0)

    def _init_(self, a1=0, b1=0, a2=0, b2=0 ):
        self.orig.a = a1
        self.orig.b = b1
        self.extrem.a = a2
        self.extrem.b = b2

    def display(self):
        print("l’origine : (", self.orig.a, ", ", self.orig.b, ")  l’extrémité : (", self.extrem.a, ", ", self.extrem.b, ")")


c = Point(1, 2)
d = Point(3, 4)
segment = Segment(0, 1, 2, 3)
segment.display()
