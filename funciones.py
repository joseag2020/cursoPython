"""def saludos():
    print('Hola Bienvenido')
    
saludos()""" #lo anterior te imprime el resultado atravez de la funcion, sin retornar

#Funcion retornando valor
"""def saludos():
    return 'Hola Bienvenido'
    
datos = saludos()
print(datos)"""

#Funcion retornando valor con argumento
def saludos(nombre):
    #return 'Hola Bienvenido', nombre
    return (f'Hola Bienvenido, {nombre}')
    
datos = saludos('Jose Arlex')
print(datos)

def suma(a, b):
    return a + b

resultado = suma(10, 50)
print('La suma es: ', resultado)

def resta(a, b):
    return a - b

resultado1 = resta(80, 40)
print('La resta es: ', resultado1)
#Funciones con argumentos indefinidos
def sumar(*args):
    suma1 = 0
    #print(args)
    for n in args:
        suma1 += n
    
    return suma1
    
suma1 = sumar(5, 9, 15, 2, 4)
print('La suma es: ', suma1)