import random

numeros_loteria = []

for n in range(0, 6):
    numeros = random.randint(1, 35)
    
    while numeros in numeros_loteria:
        numeros = random.randint(1, 35)
        
    numeros_loteria.append(numeros)
    
numeros_loteria.sort()
print(numeros_loteria)