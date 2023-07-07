import re
from datetime import datetime
import time
import os 
import sql.bdd_request as sql

class classe():
    
    __students = []
    
    def __init__(self, name, average = 0):
        self.name = name
        self.average = average
        sql.create_classe()
    
    def getStudentsList(self):
        return self.__students
    
    def add_student(self, student):
        stud = {"name": student.get_name(), "id": student.get_id(), "date_of_birth": student.get_date_of_birth(), "mark": student.get_mark()}
        print(sql.get_student(stud["id"]))
        #sql.insert_in_student(sql.get_student(stud["id"]), )
        self.__students.append(stud)
    
    def remove_student(self, student):
        for i in range(len(self.__students)):
            if self.__students[i]['id'] == student.get_id():
                del self.__students[i]
                break

    def calcul_moyenne(self):
        for i in range(len(self.__students)):
            #print(self.__students[i]['mark'])
            self.average += int(self.__students[i]['mark'])
        self.average /= len(self.__students)

    def print_average(self):
        os.system('cls')
        print("Moyenne: ", self.average)
        print("Nombre d'étudiants: ", len(self.__students))

    def modify_student(self, student):
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
                        elif re.search("[^a-zA-Zs]", entry):
                            student.set_name(new_name)
                            os.system('cls')
                            print("Name changé")
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
                        student.set_date_of_birth(new_dob)
                        os.system('cls')
                        print("Date de naissance changé")
                        break
                elif int(entry) == 3:
                    while 1:
                        os.system('cls')
                        new_id = input("Veuillez ecrire le nouveau id ou ecriver \"cancel\" ou \"c\" pour annuler:\n")
                        if new_id == "cancel" or new_id == "c":
                            os.system('cls')
                            break
                        elif re.search("[^a-zA-Z0-9]", entry):
                            student.setId(new_id)
                            os.system('cls')
                            print("id changé")
                            break
                        else:
                            print("Veuillez ecrire un id valide ou ecriver \"cancel\" ou \"c\" pour annuler")
                            continue
                elif int(entry) == 4:
                    while 1:
                        os.system('cls')
                        new_mark = input("Veuillez ecrire sa nouvelle note ou ecriver \"cancel\" ou \"c\" pour annuler:\n")
                        if new_mark == "cancel" or new_mark == "c":
                            os.system('cls')
                            break
                        if new_mark.is_digit():
                            student.set_mark(new_mark)
                            os.system('cls')
                            print("Note changé")
                            break
                        else:
                            print("Veuillez ecrire une note valide ou ecriver \"cancel\" ou \"c\" pour annuler")
                            continue
                elif int(entry) == 5:
                    os.system('cls')
                    print(self.__students)
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

    def display_list(self):
        print(self.__students)

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

    
class student(person):
    
    """Ceci est la classe student qui creer un eleve"""
    
    def __init__(self, name, date_of_birth, id, mark):
        super().__init__(name, date_of_birth)
        self.id = id
        self.mark = mark
        sql.create_student()
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        return self.name

    def get_date_of_birth(self):
        return self.date_of_birth
    
    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth
        return self.date_of_birth
    
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
        return self.id
    
    def get_mark(self):
        return self.mark
    
    def set_mark(self, mark):
        self.mark = mark
        return self.mark

    def display_info(self):
        return self
    
    def documentation(self):
        print("""Ceci est la class student""")
    
if __name__ == '__main__':
    
    my_class = classe("5eE")
    print("C'est la classe des:", my_class.name, my_class.average)
    
    studentA = student("Patrice", "2023-06-07", 1, 8)
    studentB = student("Mirah", "2023-06-07", 2, 18)
    
    my_class.add_student(studentA)
    my_class.add_student(studentB)
    print(my_class.getStudentsList())
    my_class.remove_student(studentB)
    print(my_class.getStudentsList())
    my_class.modify_student(studentA)
    my_class.calcul_moyenne()
    my_class.print_average()
    studentA.documentation()
    print(studentA.__doc__, end='')