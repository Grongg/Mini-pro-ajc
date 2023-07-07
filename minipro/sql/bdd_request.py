import sqlite3

def connexion_bdd():
    connexion = sqlite3.connect('bdd_school')
    curseur = connexion.cursor()
    return connexion, curseur

def create_student():
    
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
        classe        INTEGER          REFERENCES classe (id) ON DELETE SET NULL
                                    UNIQUE
    );
    ''')
    curseur.close()

def create_classe():
    
    connexion, curseur = connexion_bdd()
    
    curseur.execute('''
                        DROP TABLE IF EXISTS classe;
                    ''')
    connexion.commit()
    curseur.execute('''
                    
    CREATE TABLE classe (
    id           INTEGER          PRIMARY KEY AUTOINCREMENT
                                  NOT NULL,
    name         TEXT             NOT NULL
                                  UNIQUE,
    average_mark INTEGER (0, 100) NOT NULL
    );

    ''')
    curseur.close()

def get_student(matricule):
    
    connexion, curseur = connexion_bdd()
    
    curseur.execute(f'''
                    SELECT * FROM student WHERE matricule =?
                    ''', str(matricule),)
    res = curseur.fetchone()
    connexion.commit()
    curseur.close()

    return res

def insert_in_student(data, classe_id):

    connexion, curseur = connexion_bdd()
    
    donnee = (data["name"], data["date_of_birth"], data["id"], data["mark"], classe_id)
    
    curseur.execute(f'''
                    INSERT INTO student (name, date_of_birth, matricule, mark, classe) VALUES (?, ?, ?, ?, ?)
                    ''', donnee)
    connexion.commit()
    curseur.close()

def insert_in_class(table, data):

    connexion, curseur = connexion_bdd()
    
    donnee = (data["name"], data["average_mark"])
    
    curseur.execute(f'''
                    INSERT INTO {table} (name, average_mark) VALUES (?, ?)
                    ''', donnee)
    connexion.commit()
    curseur.close()

def delete_from_student(table, matricule):
    
    connexion, curseur = connexion_bdd()
    curseur.execute(f"""
                    DELETE FROM {table} where matricule = ?
                    """, (str(matricule),))
    connexion.commit()
    curseur.close()
    
def delete_from_classe(table, name):

    connexion, curseur = connexion_bdd()
    
    curseur.execute(f"""
                    DELETE FROM {table} where name = ?
                    """, (name,))
    connexion.commit()
    curseur.close()
    
def update_in_student(table, param, data, matricule):
    
    connexion, curseur = connexion_bdd()

    curseur.execute(f"""
                    UPDATE {table} 
                    SET {param} = ?
                    where matricule = ?
                    """, (data, matricule))

    connexion.commit()
    curseur.close()

def update_in_classe(table, param, data, name):
    
    connexion, curseur = connexion_bdd()

    curseur.execute(f"""
                    UPDATE {table} 
                    SET {param} = ?
                    where name = ?
                    """, (data, name))

    connexion.commit()
    curseur.close()

# if __name__ == '__main__':
#     create_classe()
#     create_student()
#     insert_in_student('student', {'name': 'John', 'date_of_birth': '1998', 'id': 1, 'mark': 10, 'classe': 1}, 1)
#     insert_in_student('student', {'name': 'John', 'date_of_birth': '1998', 'id': 2, 'mark': 10, 'classe': 1}, 2)
#     insert_in_class('classe', {'name': '5eE', 'average_mark': 0})
#     insert_in_class('classe', {'name': '6eE', 'average_mark': 0})
#     delete_from_student('student', 1)
#     delete_from_classe('classe', '5eE')
#     update_in_student('student', 'name', 'Camille', 2)
#     update_in_classe('classe', 'name', '7eE', '6eE')
