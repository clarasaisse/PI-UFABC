import math

x = input("Digite seu x:")
x_str = x.split(' ')

x = float(x_str[2])

if (x <= 1):
    print('f(x) = {:.2f}'.format  (1))

elif (x > 1) and (x <= 5):
    print('f(x) = {:.2f}'.format  (x))

elif (x > 5) and (x <= 10):
    x = x**2
    print('f(x) = {:.2f}'.format  (x))

else:
    x = x**3
    print('f(x) = {:.2f}'.format  (x))




