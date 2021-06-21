import math

calcular = input("Digite sua operação: ")
calcular_split = calcular.split(' ')

operacao = calcular_split[0]
x_str = calcular_split[1]
x = float(x_str)

if((operacao == "RAIZ") or (operacao == "LOG10")):
    if (operacao == "RAIZ"):
        raiz = math.sqrt(x)
        print('{:.2f}'.format  (raiz))
    else:
        log = math.log(x, 10)
        print('{:.2f}'.format  (log))

else:
    y_str = calcular_split [2]
    y = float(y_str)
    if (operacao == 'SUM'):
        soma = x + y 
        print('{:.2f}'.format  (soma))

    elif (operacao == 'DIF'):
        diferenca = x - y 
        print('{:.2f}'.format  (diferenca))

    elif (operacao == 'MULT'):
        multiplicacao = x * y 
        print('{:.2f}'.format  (multiplicacao))

    elif (operacao == 'DIV'):
        divisao = x/y 
        print('{:.2f}'.format  (divisao))

    elif (operacao == 'POT'):
        potencia = x**y 
        print('{:.2f}'.format  (potencia)) 

     