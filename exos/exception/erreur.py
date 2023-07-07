class Erreur(Exception):
    """classe de base qui herite de la classe exception"""
    pass

class ErreurMinAge(Erreur):
    """Joueur est mineur"""
    pass

class ErreurMAxAge(Erreur):
    """Joueur est trop vieux"""
    pass

class ErreurSexe(Erreur):
    """Joueur est pas une femme"""
    pass