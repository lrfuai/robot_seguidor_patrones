from Actuador import Actuador
import time

"""
Clase que modela concretamente a un Actuador Motor


"""
class Motor (Actuador):
    __identificador = 0;
    __debug = False
    
    """
    Constructor
    
    """
    def __init__(self,identificador):
        self.__identificador = identificador

    """
    Devuelve el identificador del Motor
    
    """
    def getIdentificador(self):
        return self.__identificador
        