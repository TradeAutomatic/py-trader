class MovingAverage :
    """
        Cette classe est celle qui permet d'encapsuler tous les attributs
        qui traitent sur les moyennes mobiles des symboles
    """

    def __init__(self):
        self.moving_average_open = 0.0
        pass

    def calculate(rate_list):
        for rate in rate_list:
            print("Rate : ", rate._get_id(), " -> open : ", rate._get_open());
            pass
        pass
    calculate = classmethod(calculate)

