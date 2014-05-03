from Navegador import Navegador
from SensorDeObjetos import SensorDeObjetos
from Led import Led
from Buzzer import Buzzer
import cv

"""
Clase que modela el Domo


"""
class Domo:
    
    __navegador = None
    __sensorDeObjetos = None
    __testigoLuminoso = None
    __testigoSonoro = None
    __config = None
    __windowName = "Visor de Centrado"
    __domoMostrarMovimiento = False
    
    """ Ventana Eje  (min,max) """
    __ventanaX = None
    __ventanY = None
    
    """ Constructor """
    def __init__ (self, config):
        self.__config = config
        self.__navegador = Navegador(self.__config)
        self.__sensorDeObjetos = SensorDeObjetos(config.DomoPatronAReconocer, config.DomoCamaraId, config.DomoMostrarEnVentanaReconocimiento, config.DomoFotogramasXCaptura)
        self.__testigoLuminoso = Led()
        self.__testigoSonoro = Buzzer()
        if self.__config.DomoMostrarEnVentanaCentrado :
            cv.NamedWindow(self.__windowName,1)
        self.__debugMode = self.__config.DomoDebugMode
    
    """ Destructor """
    def __del__(self):
        if self.__config.DomoMostrarEnVentanaCentrado :
            cv.DestroyWindow(self.__windowName)
        
    """ Calcula las coordenadas de las ventanas una unica vez de acuerdo al tamano de la  imagen """
    def __calcularVentana(self):
        if self.__ventanaX == None and self.__ventanY == None :
            imgSize = self.__sensorDeObjetos.getImageSize()
            imgSizeX = imgSize[0]
            imgSizeY = imgSize[1] 
            tmpPrincipio = int((imgSizeX - self.__config.DomoVentanaHorizontal)/2)
            tmpFin = imgSizeX - tmpPrincipio
            self.__ventanaX = (tmpPrincipio,tmpFin)
            tmpPrincipio = int((imgSizeY - self.__config.DomoVentanaVertical)/2)
            tmpFin = imgSizeY - tmpPrincipio
            self.__ventanaY = (tmpPrincipio,tmpFin)    
    
    
    """ Posiciona el Domo """
    def posicionar(self):
        self.__sensorDeObjetos.capturar()
        self.__calcularVentana()
        
        if self.__sensorDeObjetos.haveObjects() :
            self.__testigoLuminoso.encender()
            if self.__config.DomoMover :
                self.__posicionar()
        else :
            self.__testigoLuminoso.apagar()
            
    
    """ Calcula la posicion """
    def __posicionar(self):
        coordenadas = self.__sensorDeObjetos.getObjectPosition()
        
        """ ((x, y, w, h), n) """
        x = coordenadas[0]
        y = coordenadas[1]
        w = coordenadas[2]
        h = coordenadas[3]
        n = coordenadas[4]
        cx = int(x + (w /2))
        cy = int(y + (h /2))
        
        mov = self.__calcularMovimientoDomo(x, y, w, h, n, cx, cy)
        movX = mov[0]
        movY = mov[1]
        movZ = mov[2]
        
        if self.__config.DomoMostrarEnVentanaCentrado :
            self.__mostrarCentradoEnVentana(cx,cy, movX, movY)
        
        self.__realizarMovimientos(movX, movY, movZ)
    
    """ Muestra una imagen con la 'Ventana' para la imagen """
    def __mostrarCentradoEnVentana(self,cx,cy,movX,movY):
        tmpImage = self.__sensorDeObjetos.getImage()

        cv.Circle(tmpImage, (cx,cy), 3, cv.RGB(255, 0, 0))
        cv.Line(tmpImage, (self.__ventanaX[0],0), (self.__ventanaX[0],tmpImage.height), cv.RGB(255, 0, 0))
        cv.Line(tmpImage, (self.__ventanaX[1],0), (self.__ventanaX[1],tmpImage.height), cv.RGB(255, 0, 0))
        cv.Line(tmpImage, (0,self.__ventanaY[0]), (tmpImage.width,self.__ventanaY[0]), cv.RGB(255, 0, 0))
        cv.Line(tmpImage, (0,self.__ventanaY[1]), (tmpImage.width,self.__ventanaY[1]), cv.RGB(255, 0, 0))
        
        imgCenterX = int(tmpImage.width/2)
        imgCenterY = int(tmpImage.height/2)
        cv.Circle(tmpImage, (imgCenterX,imgCenterY), 3, cv.RGB(0, 0, 255))
        
        if self.__debugMode :
            print movX,movY
        
        cv.Line(tmpImage, (imgCenterX,imgCenterY), (imgCenterX+ (movX*self.__config.DomoPixelesPorMovimientoDebugLineX),imgCenterY), cv.RGB(0, 0, 255))
        cv.Line(tmpImage, (imgCenterX,imgCenterY), (imgCenterX,imgCenterY+ (movY*self.__config.DomoPixelesPorMovimientoDebugLineX)), cv.RGB(0, 0, 255))
        
        """cv.SaveImage("ImagenCentrado.jpg", tmpImage)"""
        cv.ShowImage(self.__windowName, tmpImage)
        return cv.WaitKey(10) <= 0
        
    
    """ Calcula el moviemiento del domo """
    def __calcularMovimientoDomo(self, x, y, w, h, n, cx, cy):
        return ( self.__calcularCantidadMoviemientoEje(self.__ventanaX, cx), self.__calcularCantidadMoviemientoEje(self.__ventanaY, cy), self.__calcularCantidadMoviemientoDistancia(w))


    """ Realiza el moviemiento del domo """
    def __realizarMovimientos(self,movX,movY, movZ):
        self.__navegador.mover(movX,movY,movZ)
        
    
    """ Devuelve la cantidad de movimientos que hay que realizar para centrar el Objeto """
    def __calcularCantidadMoviemientoEje(self, ventana, centroFigura):
        
        centroFronteraPrincipio = ventana[0];
        centroFronteraFin = ventana[1];
        
        if centroFigura < centroFronteraPrincipio :
            return self.__pixelesAMovimiento(centroFigura - centroFronteraPrincipio)
        elif centroFigura > centroFronteraFin :
            return self.__pixelesAMovimiento(centroFigura - centroFronteraFin)
        else :
            return 0
    
    """ Devuelve la cantidad de movimientos que hay que realizar para centrar el Objeto en Z """
    def __calcularCantidadMoviemientoDistancia(self,width):
       
       minimo = self.__config.DomoVentanaDistanciaMinima
       maximo = self.__config.DomoVentanaDistanciaMaxima
       
       if width < minimo :
           return minimo - width
       elif width > maximo :
           return maximo - width
       else :
           return 0
        
    """ Devuelve la cantidad de movimientos que implica la cantidad de pixeles pasada """
    def __pixelesAMovimiento(self,pixeles):
        return int(round(pixeles / self.__config.DomoPixelesPorMovimiento))
    