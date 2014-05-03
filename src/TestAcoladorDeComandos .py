import AcoladorDeComandos

def run():
    print "Ejecutando test de Movimientos"
    
    id1 = 'lalo'
    id2 = 'pepe'
    valor1 = 'lalo1'
    valor2 = 'lalo2'
    
    AcoladorDeComandos.set(id1, valor1)
    print AcoladorDeComandos.get(id1) == valor1
    
    AcoladorDeComandos.set(id1, valor2)
    print AcoladorDeComandos.get(id1) == valor2
    
    AcoladorDeComandos.set(id2, valor1)
    print AcoladorDeComandos.get(id2) == valor1
    
    AcoladorDeComandos.set(id1, valor1)
    print AcoladorDeComandos.get(id1) == valor1
    
    
if __name__ == '__main__':
    run()