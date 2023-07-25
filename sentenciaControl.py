# el numero hace comentario en una linea
#3 comillas simples dan comentarios en bloques
"""n=4

if n>5:
    print('Condicion verdadera')
else:
    print('Condicion Falsa')"""
    
"""
num = int(input('Ingresar un numero: '))

if num % 2 == 0:
    print(f'Numero {num} es Par')
else:
    print(f'Numero {num} es Impar') """
    
"""   
num = int(input('Ingresar un numero: '))
#condicion para saber si es un numero neutro
if num != 0:
    #Condicion para saber si el numero es mayor a cero o cumplir la conduccion de numero negativo.
    if num > 0:
        #condicion para saber si el numero es par o no
        if num % 2 == 0:
            print(f'El Numero {num} es Par Positivo')
        else:
            print(f'El Numero {num} es Impar Positivo')
    else:
        #condicion para saber si el numero es par o no
        if num % 2 == 0:
                print(f'El Numero {num} es Par Negativo')
        else:
                print(f'El Numero {num} es Impar Negativo')
        
else:
        print(f'El numero {num} es neutro') """
        
"""
Instruccion elif
vocal = input('Ingrese un dato: ')        
if vocal == 'a':
    print(vocal, 'Es vocal')
elif vocal == 'e':
    print(vocal, 'Es vocal')
elif vocal == 'i':
    print(vocal, 'Es vocal')
elif vocal == 'o':
    print(vocal, 'Es vocal')
elif vocal == 'u':
    print(vocal, 'Es vocal')
else:
    print(vocal, 'No es vocal')
"""

#ver bucle para iterar
#While
""" 
num = 1
while num <= 10 :
     print(num)
     num +=1
""" 
#suma de los N primeros numeros
"""
num = int(input('Ingrese el numero: '))
cont = 1
suma = 0
while cont <= num:
    suma += cont
    cont += 1

print(suma) 

"""  
#Muestre el numero menor de N numeros ingresados

"""
n = int(input('Cantidad de numero: '))
menor = 0
i = 1
while (i <= n):
    numero = int(input('Numeros: '))
    if(i==1):
        menor = numero
    elif numero < menor:
        menor = numero
    i += 1

print(f'El numero menor es:  {menor}')      
"""

for i in range(5):
    print(i)                 

