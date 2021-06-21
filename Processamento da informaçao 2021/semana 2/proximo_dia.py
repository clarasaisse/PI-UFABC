data = input("Digite a data ")

data_split = data.split("/")

dia = int(data_split[0])
mes = int(data_split[1])
ano = int(data_split[2])
 

if ((ano % 4 == 0) and (ano % 100!= 0)) or (ano %400 == 0):

    if (mes== 2):
        dia1=29

    elif (mes==1) or (mes==3) or (mes==5) or (mes==7) or (mes==8) or (mes==10) or (mes==12):
        dia1=31

    else :

        dia1=30
else:

    if (mes==2):

        dia1=28

    elif (mes== 1) or (mes==3) or (mes==5) or (mes==7) or (mes==8) or (mes==10) or (mes==12):
        dia1=31

    else:
        dia1=30

if (dia==31) and (mes==12):
    dia=1
    mes=1
    ano=ano+1   

elif (dia1-dia==0):
    mes=mes+1
    dia=1

else:
    dia=dia+1

if (dia >=1) and (dia<10) and (mes >= 1) and (mes < 10):

    print('0{}/0{}/{}'.format(dia, mes, ano))

elif (dia >=1) and (dia<10) and (mes >= 10):
    print('0{}/{}/{}'.format(dia, mes, ano))  

elif (dia >=10) and (mes >= 1) and (mes < 10):
    print('{}/0{}/{}'.format(dia, mes, ano))      

else:    
    print('{}/{}/{}'.format(dia, mes, ano))


