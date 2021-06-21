import math

print("Digite quatro números reais:")
num1 = float(input('Numero 1 '))
num2 = float(input('Numero 2 '))
num3 = float(input('Numero 3 '))
num4 = float(input('Numero 4 '))

media = (num1 + num2 + num3 + num4)/4

variancia = (((num1-media)**2 + (num2-media)**2 + (num3-media)**2 + (num4-media)**2))/3

desvioP = math.sqrt(variancia)

print('media = {:.2f}'.format  (media))
print('variancia = {:.2f}'.format (variancia))
print('desvio = {:.2f}'.format (desvioP))
