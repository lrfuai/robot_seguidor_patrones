from SerialController import SerialController
from Config import Config

def run():
    conf = Config
    
    serial = SerialController(conf.DomoSeriePuerto,conf.DomoSerieRate,conf.DomoSerieTimeOut)
    print serial.fullRead()
    
    serial.write('s')
    print serial.fullRead()
    
    serial.write('w')
    print serial.fullRead()
    
    serial.write('a')
    print serial.fullRead()
    
    serial.write('d')
    print serial.fullRead()
    
    serial.write('q')
    print serial.fullRead()
    
    serial.write('e')
    print serial.fullRead()


if __name__ == '__main__':
    run()