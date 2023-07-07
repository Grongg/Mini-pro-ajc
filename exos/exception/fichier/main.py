# def basicExep(nb1, nb2):
#     try:
#         nb1/nb2
#     except:
#         print("No division by 0 pls")
#     finally:
#         print("do it again\n--------------------------------")
    

# import erreur

# class joueur():
   
#     def __init__(self, name, age, gender, number) -> None:
#         try:
#             if age < 18:
#                 raise erreur.ErreurMinAge
#             elif age > 35:
#                 raise erreur.ErreurMaxAge
#             if gender != "F" and gender != "f":
#                 raise erreur.ErreurSexe
#         except erreur.ErreurMAxAge:
#             print(erreur.ErreurMAxAge.__doc__)
#             return
#         except erreur.ErreurMinAge:
#             print(erreur.ErreurMinAge.__doc__)
#             return
#         except erreur.ErreurSexe:
#             print(erreur.ErreurSexe.__doc__)
#             return
#         except Exception as e:
#             print("Error hapenned:", e.__context__)
#             return
#         print("Joueur créer correctement")
            
#         self.__name = name
#         self.__age = age
#         self.__gender = gender
#         self.__number = number
    
#     def display(self):
#         print(self.__name, self.__age, self.__gender, self.__number)
#         pass

import os, pytz, datetime, time


# def clock():
    
#     paris = pytz.timezone("Europe/Paris")
#     douala = pytz.timezone("Africa/Douala") 
#     format = "%H:%M:%S"
    
#     t1 = datetime.datetime.now(douala).strftime(format)
#     t2 = datetime.datetime.now(paris).strftime(format)
     
#     while 1:
#         os.system('cls')
#         print(f"Heure Douala: {t1} <__>  Heure Paris: {t2}")
#         time.sleep(1)




def file(name):
    try:
        file = open("logs/historique.txt", "r")
    except FileNotFoundError:
        try:
            os.mkdir("logs")
        except FileExistsError:
                pass
    finally:
        file = open("logs/historique.txt", "a")
    try:    
        nb1 = 5
        nb2 = 5
        res = nb1+nb2
        res2 = nb1-nb2
        file.write(f"nom-utilisateur: {name}\n\noperations: {nb1} + {nb2} = {res}, res = {nb1} - {nb2} = {res2}\n\ndate et heure: {datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("\n**************************************\n\n")
        
    except Exception as e:
        print("Error:", e)
    finally:
        file.close()
        
        

if __name__ == '__main__':
    #basicExep(15, 0)
    #basicExep(15, 15)
    # joueur1 = joueur("Stan", 25, "M", 50.12)
    # joueur2 = joueur("Stane", 25, "F", 50.12)
    # joueur3 = joueur("Stane", 25, "f", 50.12)
    #joueur1.display()
    # print(clock())
    file("Toto")
    