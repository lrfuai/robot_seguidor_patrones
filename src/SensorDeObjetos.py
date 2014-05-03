import cv
from Sensor import Sensor

class SensorDeObjetos (Sensor):
    
    __detectionTime = 0;
    __detectPattern = None
    __camera = None
    __faces = None
    __windowName = "Visor del Reconocimiento de Caras"
    __showInWindow = True
    __analizeEach = None
    
    """ Images """
    __capturedImage = None
    __capturedImageTarget = None
    __capturedImageSmall = None
    __capturedImageInGray = None
    
    """ Resize Attributes """
    __min_size = (20, 20)
    __image_scale = 2
    __haar_scale = 1.2
    __min_neighbors = 2
    __haar_flags = 0
    
    
    """ Metodo Constructor """
    def __init__(self, patternFile,inputCameraDeviceId = 0, showInWindow = True, analyzeEach = 1):
        self.__detectPattern = cv.Load(patternFile)
        self.__camera = cv.CreateCameraCapture(int(inputCameraDeviceId))
        self.__showInWindow = showInWindow
        self.__analizeEach = analyzeEach
        if self.__showInWindow :
            cv.NamedWindow(self.__windowName, 1)

    """ Metodo Destructor """
    def __del__(self):
        if self.__showInWindow :
            cv.DestroyWindow(self.__windowName)

    """ Obtiene una imagen de la Camara y la Procesa """
    def capturar (self):
        analizeNumber = 0
        while (self.__analizeEach > analizeNumber) :
            self.__cameraCapture()
            analizeNumber = analizeNumber +1;
            

        if self.__capturedImage == None :
            print "NO HAY IMAGEN PARA RECONOCER"
        else :
            self.__findObjects()
            self.__drawObjects()
            if self.__showInWindow :
                self.__showWindow()
        
    
    """ Captura una imagen de la Camara """
    def __cameraCapture(self):
        self.__capturedImage = cv.QueryFrame(self.__camera)
        self.__capturedImageTarget = cv.CloneImage(self.__capturedImage)
        
        self.__capturedImageInGray = cv.CreateImage((self.__capturedImage.width,self.__capturedImage.height), 8, 1)
        self.__capturedImageSmall = cv.CreateImage((cv.Round(self.__capturedImage.width / self.__image_scale ),cv.Round (self.__capturedImage.height / self.__image_scale)), 8, 1)
        
        cv.CvtColor(self.__capturedImage, self.__capturedImageInGray, cv.CV_BGR2GRAY)
        cv.Resize(self.__capturedImageInGray, self.__capturedImageSmall, cv.CV_INTER_LINEAR)
        cv.EqualizeHist(self.__capturedImageSmall, self.__capturedImageSmall)
        """
        cv.SaveImage("orig.jpg", self.__capturedImage)
        cv.SaveImage("grey.jpg", self.__capturedImageInGray)
        cv.SaveImage("small.jpg", self.__capturedImageSmall)
        cv.SaveImage("target.jpg", self.__capturedImageTarget)
        """
    
    """ Devuelve la posicion de la/s Objetos """
    def __findObjects(self):
        t = cv.GetTickCount()
        self.__objects = cv.HaarDetectObjects(self.__capturedImageSmall, self.__detectPattern, cv.CreateMemStorage(0),
                                     self.__haar_scale, self.__min_neighbors, self.__haar_flags, self.__min_size) 
        t = cv.GetTickCount() - t
        self.__detectionTime = (t/(cv.GetTickFrequency()*1000.))
       
    
    """ Procesa la imagen capturada """
    def __drawObjects(self):
        if self.haveObjects():
            for ((x, y, w, h), n) in self.__objects:
                # the input to cv.HaarDetectObjects was resized, so scale the 
                # bounding box of each face and convert it to two CvPoints
                pt1 = (int(x * self.__image_scale), int(y * self.__image_scale))
                pt2 = (int((x + w) * self.__image_scale), int((y + h) * self.__image_scale))
                cv.Rectangle(self.__capturedImageTarget, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)
    
    
    """ Muestra la imagen procesada en una Ventana """
    def __showWindow (self):
        cv.ShowImage(self.__windowName, self.__capturedImageTarget)
        return cv.WaitKey(10) <= 0
    
    
    """" Devuelve si se han encontrado Objetos o no """
    def haveObjects(self):
        return bool(self.__objects)
    
    
    """ Devuelve la cantidad de Objetos  """
    def getObjectsCount(self):
        if self.haveObjects():
            return self.__objects.count()
        else :
            return 0
    
    
    """ Devuelve la posicion de la cara que se indique sino devuelve la primera """
    def getObjectPosition(self, objectNumber = 0):
        if self.haveObjects():
            """ ((x, y, w, h), n) """
            coords = self.__objects[objectNumber]
            x = coords[0][0] * self.__image_scale;
            y = coords[0][1] * self.__image_scale;
            w = coords[0][2] * self.__image_scale;
            h = coords[0][3] * self.__image_scale;
            n = coords[1]    * self.__image_scale;
            return (x,y,w,h,n)
        else :
            return None

    
    """ Devuelve las coordenadas de los Objetos """
    def getObjects(self):
        return self.__objects
    
    """ Devuelve el Tamano de la Imagen """
    def getImageSize(self):
        return (self.__capturedImage.width,self.__capturedImage.height)
    
    """ Devuelve la imagen Original de la captura """
    def getImage(self):
        return self.__capturedImage
