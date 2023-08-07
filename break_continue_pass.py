list = [1, 2, 3, 4, 5]

for item in list:
    pass

n = 1
while n <= len(list):
    print(n)
    n +=1
    if n == 3:
        continue
    print('No es 3')
    
"""n = 1
while n <= len(list):
    print(n)
    break
    n +=1"""
    

"""while True:
    respuesta = input('Ingrese un mensaje:')
    if(respuesta == 'bye'):
        print('adios')
        break
   """
    
