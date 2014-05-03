from Motor import Motor
from EjecutorDeComandosSerie import EjecutorDeComandosSerie
import AcoladorDeComandos

"""

Clase que se encarga de la convercion de la posicion de la camara a movimientos en los servos

"""
class Navegador:
    __servoHorizontal = None
    __servoVertical = None
    __servoDistancia = None
    __ejecutorDeComandos = None
    
    """
    Constructor
    
    """
    def __init__(self, conf):
        self.__servoHorizontal = Motor('horizontal')
        self.__servoVertical = Motor('vertical')
        self.__servoDistancia = Motor('distancia')
        self.resetear()
        
        """ Comienza el hilo de ejecucion de Comandos """
        self.__ejecutorDeComandos = EjecutorDeComandosSerie(conf)
        self.__ejecutorDeComandos.start()
        
    """
    Resetea la posicion
    
    """
    def resetear(self):
        AcoladorDeComandos.set(self.__servoHorizontal.getIdentificador(), '')
        AcoladorDeComandos.set(self.__servoVertical.getIdentificador(), '')
        AcoladorDeComandos.set(self.__servoDistancia.getIdentificador(), '')
    
    """
    Metodo que Actualiza los movimientos de los actuadores
    
    """
    def mover (self, movimientoX, movimientoY, movimientoZ):
        
        idHorizontal = self.__servoHorizontal.getIdentificador()
        
        if movimientoX > 0 :
            AcoladorDeComandos.set(idHorizontal, 'a-RobotGirarIzquierda')
        elif movimientoX < 0 :
            AcoladorDeComandos.set(idHorizontal, 'd-RobotGirarDerecha')
        else :
            AcoladorDeComandos.set(idHorizontal, '')
        
        idVertical = self.__servoVertical.getIdentificador()
        
        if movimientoY > 0 :
            AcoladorDeComandos.set(idVertical, 'e-RobotDescencerCamara')
        elif movimientoY < 0 :
            AcoladorDeComandos.set(idVertical, 'q-RobotElevarCamara')
        else :
            AcoladorDeComandos.set(idVertical, '')
            
        idDistancia = self.__servoDistancia.getIdentificador()
        
        if movimientoZ > 0 :
            AcoladorDeComandos.set(idDistancia, 'w-RobotAvanzar')
        elif movimientoZ < 0 :
            AcoladorDeComandos.set(idDistancia, 's-RobotRetroceder')
        else :
            AcoladorDeComandos.set(idDistancia, '')