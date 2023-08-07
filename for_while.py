
#enumerate: para datos iterable
for i, char in enumerate('Hola'):
    print(i, char)
    
print()

for i, num in enumerate(list(range(50))):
    print(i, num)
    if(num == 25):
        print(f'index of 25 es:{i}')

print()
    
"""for y while: Cuando utilizo un for o un while
 El for en su condicion tiene el numero de veces o limite hasta donde se va a ejecutar
 While debe tener una condicion para controlar el bucle y ejecucion 
    """
for i in ([1,2,3]):
    print(i)
    
print()

i=1
while i<=3:
    print(i)
    i +=1