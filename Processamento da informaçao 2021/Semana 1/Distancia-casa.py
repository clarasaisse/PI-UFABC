import math

print('Digite as coordenadas do ponto A e ponto B, separadas por espaço:')
xa = float(input('ax: '))
ya = float(input('ay: '))
xb = float(input('bx: '))
yb = float(input('by: '))

distancia = math.sqrt((xa - xb)**2 + (ya - yb)**2)

print("Distancia =", round(distancia, 1))