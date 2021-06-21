import math

entrada = input("Digite o horario de entrada: ").split(':')
saida = input("Digite o horario de saida: ").split(':')


minuto_entrada = float(entrada[1]) / 60
hora_entrada = float(entrada[0]) + minuto_entrada

minuto_saida = float(saida[1]) / 60
hora_saida = float(saida[0]) + minuto_saida

tempo = hora_saida - hora_entrada

if(tempo <= 0.25):
    custo = 0
    print('R$ = {:.2f}'.format  (custo))
    
else:
    tempo = math.ceil(tempo)
   
    if(tempo < 2.00):
        custo = 5 * tempo
        print('R$ = {:.2f}'.format  (custo))
        
    elif((tempo >= 2.00) and (tempo <= 4.00)):
        custo = 5 + (3 * (tempo - 1))
        print('R$ = {:.2f}'.format  (custo))
        
    else:
        custo = 14 + (2 * (tempo - 4))
        print('R$ = {:.2f}'.format  (custo))
        