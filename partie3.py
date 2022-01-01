class Professeur():  #classe professeur

    __ppr = 0
    __grade = ""
    module = Module()
    ListeMatieres = []
    ListeAnnesAcademique = []

    def _init_(self, nom="", email="", mot_de_passe="", genre="", age=0, ppr=0, grade=""):
        super()._init_(self, nom, email, mot_de_passe, genre, age)
        self.__ppr = ppr
        self.__grade = grade

    def display(self):
        print(self._ppr, self._grade)


class Matiere():   #classe matiere

    __nom = 0
    __pourcentage = 0
    module = Module()
    ListeAnnesAcademique = []
    def _init_(self, nom="", pourcentage=0):
        self.__nom = nom
        self.__pourcentage = pourcentage

    def display(self):
        print(self._nom, self._pourcentage)


class Annee_Academique():       #classe annee academique

    __anne = ""
    Listetudiant = []
    Listematiesre = []
    Listeprofesseur = []

    def _init_(self, anne=""):
        self.__anne = anne

    def display(self):
        print(self.__anne)


class Etudiant():   #classe etudiant

    __code_massar = ""
    ListAnneAcademique = []

    def _init_(self, nom="", email="", mot_de_passe="", genre="", age=0, code_massar=""):
        super()._init_(nom, email, mot_de_passe, genre, age)
        self.__code_massar = code_massar

    def display(self):
        print(self.__code_massar)


