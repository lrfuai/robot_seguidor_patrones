
class Config:
    
    """ Indica si el domo debe Moverse o permanecer Inmovil """
    DomoMover = True
    
    """ Cada cuantas capturas analiza """
    DomoFotogramasXCaptura = 1
    
    """ Indica la cantidad de movimientos en cada Eje por Captura """
    DomoMovimientosXCaptura = 1
    
    """ Indica la ventana en la cual una imagen esta 'Centrada' en X """
    DomoVentanaHorizontal = 100
    
    """ Indica la ventana en la cual una imagen esta 'Centrada' en Y """
    DomoVentanaVertical = 150
    
    """ Indica el tamanio minimo de Distancia esperada en 'Z' """
    DomoVentanaDistanciaMinima = 90
    
    """ Indica el tamanio maximo de Distancia esperada en 'Z' """
    DomoVentanaDistanciaMaxima = 130
    
    """ Indica Cuantos pixeles mueve el Domo por cada Unidad de Movimiento """
    DomoPixelesPorMovimiento = 10
    
    """ Indica el Multiplicador de la linea de Debug del movimiento """
    DomoPixelesPorMovimientoDebugLineX = 5
    
    """ Indica el patron de Objeto a Reconocer """
    DomoPatronAReconocer = "haarcascades/haarcascade_frontalface_alt.xml"
    
    """ Indica si deben mostrarse en ventana los resultados del reconocimiento """
    DomoMostrarEnVentanaReconocimiento = True

    """ Indica si deben mostrarse en ventana los resultados del Centrado """
    DomoMostrarEnVentanaCentrado = True

    """ Indica el Id del dispositivo de Captura """
    DomoCamaraId = 1
    
    """ Indica si detalla sus actividades """
    DomoDebugMode = False
    
    """ Numero de Puerto Serie """
    DomoSeriePuerto = 32
    
    """ La velocidad de comunicacion del Puerto Serie """
    DomoSerieRate = 2400
    
    """ Time Out del Puerto Serie """
    DomoSerieTimeOut = 1
    
    """ Si debe mostrar actividad del Puerto """
    DomoSerieDebug = 1