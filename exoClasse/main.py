from mesClasses import etudiant
from mesClasses import classe
import os

if __name__=='__main__':
    menu = 0
    mesEtudiants = []
    maClasse = classe.Classe("AJC FORMATION IVVQ")

    while(menu != 6):
        menu = int(input("-----------------------------\n\n1)Ajouter un étudiant\n2)Modifier un étudiant\n3)Supprimer un étudiant\n4)Afficher la liste des étudiants\n5)Donner la moyenne de la classe\n6)Quitter le programme   "))
        os.system("cls")
        
        if menu == 1:
            etudiant1 = etudiant.Etudiant()
            maClasse.addStudent(etudiant1)
            lastStudent = maClasse.students[len(maClasse.students) - 1]
            lastStudent.modify()
            # maClasse.students[len(maClasse.students) - 1].modify(maClasse.students[len(maClasse.students) - 1])

        elif menu == 2:
            studentId = int(input("Veuillez entrer l'ID de l'étudiant à modifier: "))
            maClasse.students[studentId - 1].modify(maClasse.students[studentId - 1])

        elif menu == 3:
            studentId = int(input("Veuillez entrer l'ID de l'étudiant à supprimer: "))
            maClasse.students.remove(maClasse.students[studentId - 1])

        elif menu == 4:
            for currentStudent in maClasse.students:
                 currentStudent.display()

        elif menu == 5:
                maClasse.moyenne(maClasse.students)
                print(f"Moyenne de la classe {maClasse.nom}: {maClasse.moyenneClasse}")