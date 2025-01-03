from functools import lru_cache

class Boule:
    def __init__(self, x:int, y:int, rayon:int, tag:str):
        """
        Initialise une instance de la classe Boule.

        :param x: Coordonnée x de la boule (int).
        :param y: Coordonnée y de la boule (int).
        :param rayon: Rayon de la boule (int).
        :param tag: Étiquette associée à la boule (str).
        """
        self.x = x
        self.y = y
        self.rayon = rayon
        self.tag = tag

    def __repr__(self):
        """
        Représentation textuelle de l'objet Boule.

        :return: Une chaîne décrivant la boule.
        """
        return f"Boule {self.tag} (x={self.x}, y={self.y}, rayon={self.rayon})"
    
    def changer_rayon(self, rayon:int):
        """
        Change le rayon de la boule.

        :param nouveau_rayon: Nouveau rayon à appliquer (int).
        """
        if rayon > 0 :
            self.rayon = rayon
        else :
            raise ValueError("Le rayon doit être positif")
        
    def to_dict(self):
        return {
            "type": "boule",
            "x": self.x,
            "y": self.y,
            "rayon": self.rayon,
            "tag": self.tag
        }
        
@lru_cache
def distance(Boule1: Boule, Ox:int, Oy:int):
    return (Boule1.x - Ox)**2 + (Boule1.y - Oy)**2

@lru_cache
def point_dans_boule(Boule1: Boule, Ox:int, Oy:int, R:int = 0):
    return distance(Boule1, Ox, Oy) < (Boule1.rayon + R)**2