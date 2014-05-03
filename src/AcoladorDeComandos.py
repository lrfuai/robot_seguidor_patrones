"""
Clase que se utiliza para manejar la concurrencia de los hilos


"""
class AcoladorDeComandos :
    comandos = {}

"""
Devuelve el valor de Comando para el identificador pasado

"""   
def get(identificador):
    return AcoladorDeComandos.comandos[identificador]

"""
Setea un valor de Comando para el identificador pasado

"""   
def set( identificador, valor):
    AcoladorDeComandos.comandos[identificador] = valor

"""
Devuelve todos los Comandos que estan para ejecutar

"""
def getAll():
    return AcoladorDeComandos.comandos

"""
Limpia la cola

"""
def clear():
    AcoladorDeComandos.comandos = {}