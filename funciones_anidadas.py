def primera(datos):
    print(datos)
    
    def segunda():
        for n in datos:
            print(n)
        
        def tercera():
            print("Hola desde la tercera funcion")
        tercera()
        
    segunda()
            
primera([2, 4, 6, 8, 10])