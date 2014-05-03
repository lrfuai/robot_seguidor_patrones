import time
from threading import Thread
from AcoladorDeComandos import AcoladorDeComandos

"""
Clase que modela un ejecutor de comandos Abstracto

"""
class EjecutorDeComandos (Thread):
    
    def __init__(self):
        Thread.__init__(self)
    
    def __ejecutar(self):
        print 'Homero: Trabajo muy duro, como un esclavo, Paguenme dinero!'
    
    """ 
    Tarea de trabajo del Hilo
    
    """
    def run(self):
        while 1 :
            self.__ejecutar()
            time.sleep(5);