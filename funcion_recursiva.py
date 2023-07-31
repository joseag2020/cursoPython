def factorial(numero):
    if numero > 1:
        numero = numero * factorial(numero -1)
    return numero

#numero = int(input('Ingrese un Numero: '))

#print(' El factorial es: ', factorial(numero))

def contador_atras(numero):
    numero -= 1
    if(numero > 0):
        print(numero)
        contador_atras(numero0)
    else:
        print('fin')
    
    print(f'Liberacion: {numero}')
    
contador_atras(5)