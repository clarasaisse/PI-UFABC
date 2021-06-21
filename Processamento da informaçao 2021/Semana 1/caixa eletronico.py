valor_saque = (float(input("Digite o valor que você quer sacar, em reais: R$ ")))
total = valor_saque
moeda = 100.00
totalmoeda = 0

while True:
    if total >= moeda:
        total -= moeda
        totalmoeda += 1

    else:
        print('Cédulas de R$ {:.2f}'.format (moeda),":", +totalmoeda)
        if moeda == 100.00:
            moeda = 50.00   
        elif moeda == 50.00:
             moeda = 20.00
        elif moeda == 20.00:
             moeda = 10.00  
        elif moeda == 10.00:
             moeda = 5.00
        elif moeda == 5.00:
             moeda = 2.00   
        elif moeda ==2.00:
              moeda = 1.00
        elif moeda == 1:
             moeda = 0    
        totalmoeda = 0
        if total <= 0:
            break
                           



