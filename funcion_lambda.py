"""def potencia(numero, exponente):
    valor = pow(numero, exponente)
    return valor

print(potencia(5,2))"""

#funcion lambda
potencia = lambda num, exp : pow (num, exp)

print(potencia(5, 2))