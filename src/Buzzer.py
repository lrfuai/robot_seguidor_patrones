"""
Clase que modela un Buzzer

"""
class Buzzer :
    __encendido = False

    def encender (self):
        self.__encendido = True
        
    def apagar(self):
        self.__encendido = False