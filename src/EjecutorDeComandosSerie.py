from EjecutorDeComandos import EjecutorDeComandos
import AcoladorDeComandos
from SerialController import SerialController
import time

class EjecutorDeComandosSerie (EjecutorDeComandos):
    __serial = None
    __debug = False
    
    def __init__(self,conf):
        self.__serial = SerialController(conf.DomoSeriePuerto,conf.DomoSerieRate,conf.DomoSerieTimeOut)
        self.__debug = conf.DomoSerieDebug
        EjecutorDeComandos.__init__(self)
        pass
    
    def run(self):
        while 1 :
            comandos = AcoladorDeComandos.getAll()
            if len(comandos) :
                self.__ejecutar(comandos)
            AcoladorDeComandos.clear()
            #time.sleep(1);
    
    def __ejecutar(self, comandos):
        for clave in comandos:
            valor = str(comandos[clave])
            if(len(valor)>1):
                self.__serial.write(valor)
                if self.__debug :
                    print '--> '+valor
                    self.__serial.fullRead()