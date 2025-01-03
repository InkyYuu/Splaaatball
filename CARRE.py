class Carre:
    def __init__(self, x, y, cote, tag):
        """
        Initialise un carré.
        :param x: Coordonnée X du coin supérieur gauche.
        :param y: Coordonnée Y du coin supérieur gauche.
        :param cote: Longueur du côté du carré.
        :param tag: Identifiant ou description du carré.
        """
        self.x = x
        self.y = y
        self.x2 = x + cote
        self.y2 = y + cote
        self.cote = cote
        self.tag = tag
        
    def to_dict(self):
        return {
            "type": "carre",
            "x": self.x,
            "y": self.y,
            "cote": self.cote,
            "tag": self.tag
        }
