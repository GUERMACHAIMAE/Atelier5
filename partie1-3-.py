class rectangle: #definition classe rectangle

    largeur = 0
    longueur = 0
    n = ""

    def _init_(self, largeur=0, longueur=0, n='rectangle'):  #initialisation avec valeurs par défaut
        self.largeur = largeur
        self.longueur = longueur
        self.n = n

    def display(self):
        print("(", self.n, ": (", self.largeur, ", ", self.longueur, ")")

    def surface(self):
        return self.largeur*self.longueur


class carre(rectangle):  #classe des carres herite de rectangle

     def _init_(self, largeur=0, longueur=0, n='carre'):
        super()._init_(largeur, longueur)
        self.n = n


car = carre(1, 2, 'carre')
rec = rectangle(3, 4, 'rectangle')
