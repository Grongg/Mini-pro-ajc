import sqlite3

def connexion_bdd():
    connexion = sqlite3.connect('sql/bdd_school.db')
    curseur = connexion.cursor()
    return connexion, curseur

def create_student_table():
    
    connexion, curseur = connexion_bdd()

    curseur.execute('''
                        DROP TABLE IF EXISTS student;
                    ''')
    connexion.commit()
    curseur.execute('''

    CREATE TABLE student (
        id            INTEGER          PRIMARY KEY AUTOINCREMENT
                                    NOT NULL,
        name          TEXT (2, 255)    NOT NULL,
        date_of_birth TEXT (6, 8)      NOT NULL,
        matricule     TEXT (8, 10)     NOT NULL UNIQUE,
        mark          INTEGER (0, 100) NOT NULL,
        classe        INTEGER           REFERENCES classe (id) ON DELETE SET NULL
    );
    ''')
    curseur.close()

def create_classe_table():
    
    connexion, curseur = connexion_bdd()
    
    curseur.execute('''
                        DROP TABLE IF EXISTS classe;
                    ''')
    connexion.commit()
    curseur.execute('''
                    
    CREATE TABLE classe (
    id           INTEGER          PRIMARY KEY AUTOINCREMENT
                                  NOT NULL,
    name         TEXT (3, 5)    NOT NULL
                                  UNIQUE,
    average_mark INTEGER (0, 100) NOT NULL
    );

    ''')
    curseur.close()


def insert_in_student(data, classe_id):

    connexion, curseur = connexion_bdd()
    
    donnee = (data["name"], data["date_of_birth"], data["matricule"], data["mark"], classe_id)
    
    curseur.execute(f'''
                    INSERT INTO student (name, date_of_birth, matricule, mark, classe) VALUES (?, ?, ?, ?, ?)
                    ''', donnee)
    connexion.commit()
    curseur.close()

def insert_in_classe(data, average=0):

    connexion, curseur = connexion_bdd()
    
    
    curseur.execute(f'''
                    INSERT INTO classe (name, average_mark) VALUES (?, ?)
                    ''', (data, average))
    connexion.commit()
    curseur.close()

def delete_from_student(matricule):
    
    connexion, curseur = connexion_bdd()
    curseur.execute(f"""
                    DELETE FROM student where matricule = ?
                    """, (str(matricule),))
    connexion.commit()
    curseur.close()
    
def delete_from_classe(name):

    connexion, curseur = connexion_bdd()
    
    curseur.execute(f"""
                    DELETE FROM classe where name = ?
                    """, (name,))
    connexion.commit()
    curseur.close()
    
def update_in_student(param, data, matricule):
    
    connexion, curseur = connexion_bdd()

    curseur.execute(f"""
                    UPDATE student 
                    SET {param} = ?
                    where matricule = ?
                    """, (data, matricule))
    connexion.commit()
    curseur.close()

def update_in_classe(param, data, name):
    
    connexion, curseur = connexion_bdd()

    curseur.execute(f"""
                    UPDATE classe 
                    SET {param} = ?
                    where name = ?
                    """, (data, name))

    connexion.commit()
    curseur.close()

def check_matricule(matricule):
    connexion, curseur = connexion_bdd()
    curseur.execute(f'''
                    SELECT matricule FROM student
                    ''')
    res = curseur.fetchall()
    if len(matricule) < 8 or len(matricule) > 10:
        return 1
    matricule = f"('{matricule}',)"
    for mat in res:
        if str(mat) == matricule:
            return 1
    connexion.commit()
    curseur.close()
    return 0
            
def get_student(matricule):
    
    connexion, curseur = connexion_bdd()
    
    curseur.execute(f'''
                    SELECT * FROM student WHERE matricule = ?
                    ''', (str(matricule),))
    res = curseur.fetchone()
    connexion.commit()
    curseur.close()

    return res

def get_classe(name):
    
    connexion, curseur = connexion_bdd()
    
    curseur.execute(f'''
                    SELECT * FROM classe WHERE name = ?
                    ''', str(name),)
    res = curseur.fetchone()
    connexion.commit()
    curseur.close()

    return res

def list_students():
    
    connexion, curseur = connexion_bdd()

    curseur.execute(f"""
                    SELECT * FROM student
                    """)
    resultats = curseur.fetchall()
    for resultat in resultats:
        print(resultat)
    connexion.commit()
    curseur.close()
    
def list_classes():

    connexion, curseur = connexion_bdd()

    curseur.execute(f"""
                    SELECT * FROM classe
                    """)
    resultats = curseur.fetchall()
    for resultat in resultats:
        print(resultat)
    connexion.commit()
    curseur.close()

def get_classe_id(name):
    
    connexion, curseur = connexion_bdd()
    data = (name, )
    curseur.execute("""
                    SELECT id FROM classe where name = ?
                    """, data)
    res = curseur.fetchone()
    connexion.commit()
    curseur.close()

    return res

def get_all_students():
    
    connexion, curseur = connexion_bdd()

    curseur.execute(f"""
                    SELECT * FROM student
                    """)
    resultats = curseur.fetchall()
    transformed_resultats = []
    for resultat in resultats:
        transformed_resultats.append(list(resultat))
    connexion.commit()
    curseur.close()
    return resultats

def get_all_students_from_classe(id):
    
    connexion, curseur = connexion_bdd()

    curseur.execute(f"""
                    SELECT * FROM student where classe = ?
                    """, (id, ))
    resultats = curseur.fetchall()
    transformed_resultats = []
    for resultat in resultats:
        transformed_resultats.append(list(resultat))
    connexion.commit()
    curseur.close()
    return resultats




if __name__ == '__main__':
    # create_classe()
    # create_student()
    #
    # insert_in_classe({'name': '5eE', 'average_mark': 0})
    # insert_in_classe({'name': '6eE', 'average_mark': 0})
    # delete_from_student(2)
    # delete_from_classe('6eE')
#     update_in_student('student', 'name', 'Camille', 2)
#     update_in_classe('classe', 'name', '7eE', '6eE')
    pass