class MovingAverage :
    """
        Cette classe est celle qui permet d'encapsuler tous les attributs
        qui traitent sur les moyennes mobiles des symboles
    """

    def __init__(self):
        self.open = (0.0)
        self.close = 0.0
        self.low = 0.0
        self.high = 0.0
