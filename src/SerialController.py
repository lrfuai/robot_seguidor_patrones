import sys
import serial

class SerialController :
    
    __serial = None
    
    def __init__(self, port, rate = 2400, timeout = 1):
        try:
            self.__serial = serial.Serial(int(port), int(rate))
            self.__serial.timeout=timeout;
        except serial.SerialException:
            #-- Error al abrir el puerto serie
            sys.stderr.write("Error al abrir puerto: " + str(port))
            sys.exit(1)
    
    def read (self):
        return self.__serial.read();
    
    def fullRead(self):
        readOnce = False
        buffer = str("")
        char = ''
        
        while (not readOnce or len(char)==1) :
            char = str(self.read())
            buffer += char
            readOnce = True
        return buffer
    
    def write (self, string):
        self.__serial.write(str(string))
