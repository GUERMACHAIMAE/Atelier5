class vecteur2d:   #definition class vecteur2D

    x1 = 0
    x2 = 0

    def _init_(self, x1=0, x2=0):  #constructeur avec parametre par defaut
        self.x1 = x1  #initialisation de x et y
        self.x2 = x2

    def display(self):
        print("(", self.x1, ", ", self.x2, ")")
                     
    def _add_(self, autre):  #addition
        x = self.x1 + autre.x1
        y = self.x2 + autre.x2
        vecteur = vecteur2d(x, y)
        return vecteur


vecteur1 = vecteur2d()
vecteur2 = vecteur2d(5, 5)
vecteur1.x1 = 20
vecteur1.x2 = 18

vecteur1.display()
vecteur2.display()

vecteur3 = vecteur1 + vecteur2
vecteur3.display()



