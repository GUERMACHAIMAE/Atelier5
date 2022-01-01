class Etudiant:

    nom = ""
    prenom = ""
    age = 0
    cne = ""
    moyenne = 0

    def _init_(self, nom="", prenom="", age=0, cne="", moyenne=0):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne
    def display(self):
        print(self.nom, self.prenom, self.age, self.cne, self.moyenne)


student1 = Etudiant("xxxxx", "xxx", 20, "1111", 15)
student2 = Etudiant("yyyyy", "yyy", 19, "2222", 16)
student3 = Etudiant("zzzzz", "zzz", 18, "3333", 17)
student4 = Etudiant("wwwww", "www", 17, "4444", 18)


ListEtudiants = []
ListEtudiants.append(student1)
ListEtudiants.append(student2)
ListEtudiants.append(student3)
ListEtudiants.append(student4)


#sort selon l'age et la moyen :

def MySort1(etudiant):
    return -etudiant.moyenne - etudiant.age

#sort selon la moyenne :

def MySort2(etudiant):
    return -etudiant.moyenne

#sort selon l'age  :

def MySort3(etudiant):
    return -etudiant.age

#affichage:

#sort selon l'age et la moyenne :
ListEtudiants.sort(key=MySort1)
for i in ListEtudiants:
    i.display()


#sort selon la moyenne :
ListEtudiants.sort(key=MySort2)
for i in ListEtudiants:
    i.display()

#sort selon la l'age :
ListEtudiants.sort(key=MySort3)
for i in ListEtudiants:
    i.display()
