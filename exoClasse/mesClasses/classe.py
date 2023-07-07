from mesClasses.etudiant import Etudiant

class Classe:
    def __init__(self, nom):
        self.nom = nom
        self.students = []

    def addStudent(self, newStudent):
        self.students.append(newStudent)

    def moyenne(self, students):
        moyenneClasse = 0
        
        for student in students:
            moyenneClasse += float(student.note)
            print(moyenneClasse)
        self.moyenneClasse = moyenneClasse/len(students)