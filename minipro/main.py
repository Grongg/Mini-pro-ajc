import string, random
import re
from datetime import datetime
import time
import os 
import sql.bdd_request as sql

student_list = []

class classe():

    def __init__(self, name, average = 0):
        self.__name = name
        self.__average = average
        sql.insert_in_classe(self.__name, self.__average)
        print(self.__average)

    def add_student(self, student):
        sql.update_in_student("classe", sql.get_classe_id(str(self.__name))[0], student.get_matricule())
        self.calcul_moyenne()
        sql.update_in_classe("average_mark", int(self.__average), str(self.__name))

    def remove_student(self, student):
        for i in range(len(self.__students)):
            if self.__students[i]['id'] == student.get_id():
                del self.__students[i]
                break

    def calcul_moyenne(self):
        self.__average = 0
        students = sql.get_all_students_from_classe(sql.get_classe_id(str(self.__name))[0])
        for i in range(len(students)):
            self.__average += int(students[i][4])
        self.__average /= len(students)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name   

    def get_average(self):
        return self.__average

    def set_name(self, name):
        self.__name = name
        return self.__name

from abc import ABC, abstractmethod
class person(ABC):

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @abstractmethod
    def display_info(self):
        return self.name

    @abstractmethod
    def documentation(self):
        print("""
                Ceci est la class abstraite person
              """)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return self.name

class student(person):
    
    """Ceci est la classe student qui creer un eleve"""
    
    def __init__(self, name, date_of_birth, mark):
        super().__init__(name, date_of_birth)
        self.__mark = mark
        self.__name = name
        self.__matricule = ""
        self.create_matricule()
        self.__date_of_birth = date_of_birth
        sql.insert_in_student({"name": self.__name, "date_of_birth": self.__date_of_birth, "matricule": self.__matricule, "mark": self.__mark}, None)
        # print(student_list)
        student_list.append(student)
        print(student_list)

    # fonction qui test si le check de doublon marche bien
    # def get_matricule(self, counter=[0]):
    #     import string, random
    #     self.__matricule = ""
    #     for i in range(8):
    #         rdm = random.randrange(0, 2)
    #         if rdm == 0:
    #             self.__matricule += random.choice(string.ascii_letters)
    #         elif rdm == 1:
    #             self.__matricule += str(random.randrange(0,10))
    #     # print("counter:", counter[0])
    #     if counter[0] != 0:
    #         mat = sql.check_matricule(self.__matricule)
    #         # print("mat:", mat)
    #         if mat == 1:
    #             self.get_matricule()
    #         else:
    #             return self.__matricule
    #     else:
    #         self.__matricule = "0cx8P5z2"
    #         mat = sql.check_matricule(self.__matricule)
    #         if mat == 1:
    #             counter[0] += 1
    #             self.get_matricule()

    def create_matricule(self):

        self.__matricule = ""

        for i in range(8):
            rdm = random.randrange(0, 2)
            if rdm == 0:
                self.__matricule += random.choice(string.ascii_letters)
            elif rdm == 1:
                self.__matricule += str(random.randrange(0,10))
                
        mat = sql.check_matricule(self.__matricule)
        if len(sql.get_all_students()) == 0:
            mat = 0
        if mat == 1:
            self.create_matricule()

    def get_matricule(self):
        return self.__matricule

    def set_matricule(self, matricule):
        self.__matricule = matricule
        return self.__matricule

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth
        return self.__date_of_birth

    def get_mark(self):
        return self.__mark
    
    def set_mark(self, mark):
        self.__mark = mark
        return self.__mark

    def display_info(self):
        return self

    def documentation(self):
        print("""Ceci est la class student""")
        
    def modify_student(self):
        os.system('cls')
        while 1:
            entry = input("""Que voulez vous modifier chez l'etudiant:
                         [1]: Son nom
                         [2]: Son année de naissance
                         [3]: Son id
                         [4]: Sa note
                         [5]: Voir la liste des étudiants
                         [6]: Exit
                      """)
            if entry.isdigit():
                if int(entry) == 1:
                    while 1:
                        os.system('cls')
                        new_name = input("Veuillez ecrire le nouveau nom ou ecriver \"cancel\" ou \"c\" pour annuler:\n")
                        if new_name == "cancel" or new_name == "c":
                            os.system('cls')
                            break
                        elif re.search("[^a-zA-Zs]", new_name)  is None:
                            self.__name = new_name
                            sql.update_in_student("name", str(new_name), self.__matricule())
                            os.system('cls')
                            print("Name changé")
                            print(sql.get_student())
                            break
                        else:
                            print("Veuillez ecrire un nom valide ou ecriver \"cancel\" ou \"c\" pour annuler")
                            continue
                elif int(entry) == 2:
                    while 1:
                        os.system('cls')
                        new_dob = input("Veuillez ecrire la nouvelle date de naissance sous le format YYYY-DD-MM ou ecriver \"cancel\" ou \"c\" pour annuler :\n")
                        format = "%Y-%d-%m"
                        if new_dob == "cancel" or new_dob == "c":
                            os.system('cls')
                            break
                        try:
                            datetime.strptime(new_dob, format)
                        except ValueError as ve:
                            os.system('cls')
                            print("Veuillez ecrire une date valide au bon format YYYY-DD-MM")
                            time.sleep(2)
                            continue
                        self.__date_of_birth = new_dob
                        sql.update_in_student("date_of_birth", str(new_dob), self.__matricule())
                        os.system('cls')
                        print("Date de naissance changé")
                        print(sql.get_student())
                        break
                elif int(entry) == 3:
                    while 1:
                        os.system('cls')
                        new_matricule = input("Veuillez ecrire le nouveau matricule ou ecriver \"cancel\" ou \"c\" pour annuler:\n")
                        if new_matricule == "cancel" or new_matricule == "c":
                            os.system('cls')
                            break
                        elif re.search("[^a-zA-Z0-9]", new_matricule)  is None:
                            if sql.check_matricule(str(new_matricule)) == 0:
                                self.__matricule = new_matricule
                                sql.update_in_student("matricule", str(new_dob), self.__matricule())
                            else:
                                print("Veuillez ecrire un matricule valide ou ecriver \"cancel\" ou \"c\" pour annuler")
                                continue
                            os.system('cls')
                            print("matricule changé")
                            print(sql.get_student())
                            break
                        else:
                            print("Veuillez ecrire un matricule valide ou ecriver \"cancel\" ou \"c\" pour annuler")
                            continue
                elif int(entry) == 4:
                    while 1:
                        os.system('cls')
                        new_mark = input("Veuillez ecrire sa nouvelle moyenne ou ecriver \"cancel\" ou \"c\" pour annuler:\n")
                        if new_mark == "cancel" or new_mark == "c":
                            os.system('cls')
                            break
                        if new_mark.is_digit():
                            self.__mark = new_mark
                            os.system('cls')
                            print("Note changé")
                            break
                        else:
                            print("Veuillez ecrire une note valide ou ecriver \"cancel\" ou \"c\" pour annuler")
                            continue
                elif int(entry) == 5:
                    os.system('cls')
                    sql.list_students()
                    continue
                elif int(entry) == 6:
                    os.system('cls')
                    break
                else:
                    print("Veuillez ecrire une option entre 1 et 5 ex: 1")
                    continue
            elif entry == "e" or entry == "q" or entry == "quit" or entry == "exit":
                os.system('cls')
                break
            else:
                print("Veuillez ecrire une option valide ex: 1")
                continue

def school():
    os.system('cls')
    while 1:
        entry = input("""Que voulez vous faire:
                         [1]: Afficher la liste des Classes
                         [2]: Afficher la liste des Eleves
                         [3]: Ajouter une nouvelle Classe
                         [4]: Ajouter un nouvel Eleve
                         [5]: Modifier une Classe en particulier
                         [6]: Modifier un Eleve en particulier
                         [7]: Voir une demo du programme
                         [8]: Exit
                      """)
        if entry.isdigit():
            if int(entry) == 1:
                os.system('cls')
                sql.list_classes()
                time.sleep(2)
            elif int(entry) == 2:
                os.system('cls')
                sql.list_students()
                time.sleep(2)
            elif int(entry) == 3:
                os.system('cls')
                flag_name = False
                flag_qt = False
                flag_avgmark = False
                while 1:
                    if flag_name == True:
                                break
                    entry = input("Veuillez entrer le nom de la Classe ou ecriver \"cancel\" ou \"c\" pour annuler:\n")
                    if entry == "cancel" or entry == "c":
                        os.system('cls')
                        break
                    elif re.search("[^a-zA-Z0-9]", entry)  is None:
                        flag_name = True
                        while 1:
                            if flag_qt == True:
                                break
                            entry2 = input("Connaissez-vous la moyenne de la Classe ?\n[1]: Oui\n[2]: Non\n")
                            if entry2.isdigit():
                                if int(entry2) == 1:
                                    flag_qt = True
                                    while 1:
                                        if flag_avgmark == True:
                                            break
                                        entry3 = input("Veuillez entrer la moyenne de la Classe (ex: 10):\n")
                                        if entry3.isdigit():
                                            classe(entry, entry3)
                                            print(sql.get_classe(str(entry)))
                                            flag_avgmark = True
                                        else:
                                            print("Veuillez ecrire une option entre 1 et 2 ex: 1")
                                            continue
                                            
                                elif int(entry2) == 2:
                                    classe(entry)
                                    os.system('cls')
                                    print(sql.get_classe(str(entry)))
                                    flag_qt = True
                                    break
                                else:
                                    print("Veuillez ecrire une option entre 1 et 2 ex: 1")
                                    continue
                            else:
                                print("Veuillez ecrire une option entre 1 et 2 ex: 1")
                                continue
                    else:
                        print("Veuillez ecrire un nom valide ou ecriver \"cancel\" ou \"c\" pour annuler")
                        continue
            elif int(entry) == 4:
                os.system('cls')
                print(student_list)
                flag_name = False
                flag_dob = False
                flag_mark = False
                while 1:
                    if flag_name == True:
                        break
                    name = input("Veuillez entrer le nom de l'Eleve ou ecriver \"cancel\" ou \"c\" pour annuler:\n").lower()
                    if name == "cancel" or name == "c":
                        os.system('cls')
                        break
                    elif re.search("[^a-zA-Zs]", name) is None:
                        name = name.title()
                        print("Vous avez entré le nom suivant:", name)
                        flag_name = True
                        while 1:
                            if flag_dob == True:
                                break
                            dob = input("Veuillez ecrire la nouvelle date de naissance sous le format YYYY-DD-MM ou ecriver \"cancel\" ou \"c\" pour annuler :\n")
                            format = "%Y-%d-%m"
                            if dob == "cancel" or dob == "c":
                                os.system('cls')
                                break
                            try:
                                datetime.strptime(dob, format)
                            except ValueError as ve:
                                os.system('cls')
                                print("Veuillez ecrire une date valide au bon format YYYY-DD-MM")
                                time.sleep(2)
                                continue
                            print("Vous avez entré la date suivante:", dob)
                            flag_dob = True
                            while 1:
                                if flag_mark == True:
                                    break
                                mark = input("Veuillez ecrire sa nouvelle moyenne ou ecriver \"cancel\" ou \"c\" pour annuler:\n")
                                if mark == "cancel" or mark == "c":
                                    os.system('cls')
                                    break
                                if mark.isdigit():
                                    print("Vous avez entré la moyenne suivante:", mark)
                                    stud = student(name, dob, mark)
                                    print("Generation du matricule de l'etudiant...")
                                    time.sleep(3)
                                    print("Generation terminé!")
                                    time.sleep(2)
                                    os.system('cls')
                                    matricule = stud.get_matricule()
                                    print(sql.get_student(str(matricule)))
                                    # print(student_list)
                                    flag_mark = True
                                else:
                                    print("Veuillez ecrire une note valide ou ecriver \"cancel\" ou \"c\" pour annuler")
                                    continue
                    else:
                        os.system('cls')
                        print(name, re.search("[^a-zA-Zs]", name))
                        print("Veuillez ecrire un nom valide ou ecriver \"cancel\" ou \"c\" pour annuler")
                        continue
            elif int(entry) == 6:
                while 1:
                    entry = str(input("Veuillez entrer le matricule de l'Eleve qui vous voulez modifier:\n"))
                    print("entry:", entry)
                    if sql.check_exist_mat(entry) == 1:
                        print("Matricule invalide, veuillez reesayer svp")
                        continue
                    else:
                        stud = sql.get_student(entry)
                        found_student = ""
                        print(student_list)
                        for s in student_list:
                            test = s.get_matricule(s)
                            print(student_list, "&&", test, "&&", entry)
                            if s.get_matricule(s) == entry:
                                found_student = s
                                break
                        if found_student == "":
                            print("Matricule invalide, veuillez reesayer svp")
                        found_student.modify_student()
            elif int(entry) == 8:
                os.system('cls')
                break
            else:
                print("Veuillez ecrire une option entre 1 et 8 ex: 7")
                continue
        elif entry == "e" or entry == "q" or entry == "quit" or entry == "exit":
            os.system('cls')
            break
        else:
            print("Veuillez ecrire une option valide ex: 1")
            continue

if __name__ == '__main__':
    
    school()