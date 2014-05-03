from Domo import Domo

class Robot:
    __config = None
    __domo = None
    
    """  """
    def __init__(self,config):
        self.__config = config
        self.__domo = Domo(config)
    

    def actuar(self):
        self.__domo.posicionar()
        pass