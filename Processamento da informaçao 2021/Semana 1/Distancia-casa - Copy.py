import math

A = input('Entre com dois números separados por espaço: ')
xa, ya = (float(numero) for numero in A.split(' '))

B = input('Entre com dois números separados por espaço: ')
xb, yb = (float(numero) for numero in B.split(' '))

distancia = math.sqrt((xa - xb)**2 + (ya - yb)**2)

print("Distancia =", round(distancia, 1))