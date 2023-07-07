from mesClasses.personne import Personne

class Etudiant(Personne):

    def __init__(self):
        self.nom = ""
        self.birthDate = ""
        self.matricule = ""
        self.note = ""

    def display(self):
        print("-------------------------------------------")
        print(f"Nom de l'élève: {self.nom}")
        print(f"Date de naissance de l'élève: {self.birthDate}")
        print(f"Matricule de l'élève: {self.matricule}")
        print(f"Note de l'élève: {self.note}")

    def modify(etudiant):
        etudiant.nom = input("Veuillez entrer le nom de l'élève: ")
        etudiant.birthDate = input("Veuillez entrer la date de naissance de l'élève: ")
        etudiant.matricule = input("Veuillez entrer le matricule de l'élève: ")
        etudiant.note = input("Veuillez entrer la note de l'élève: ")