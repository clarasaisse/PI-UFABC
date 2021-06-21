import math

triangulo = input("Digite os lados do triangulo:")
triangulo_split = triangulo.split(' ')

lado1 = float(triangulo_split[0])
lado2 = float(triangulo_split[1])
lado3 = float(triangulo_split[2])


if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1) or (lado1 + lado2 + lado3 == 0):
    print("Medidas nao formam um triangulo")

else:
    if (lado1 == lado2) and (lado1 == lado3):
        print("Triangulo equilatero")

    elif (lado1==lado2) or (lado2==lado3) or (lado1==lado3): 
        print('Triangulo isosceles') 

    else:
        print("Triangulo escaleno")     
