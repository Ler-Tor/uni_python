#Nalog
'''
oklad = int(input('Vvedite stavku: '))
stavka = float(input('Vvedite procent (format 0.X): '))

print('Razmer poluchki: ', int(oklad - oklad * stavka))
print('Nolog v dengah: ', int(oklad * stavka))
'''

#Son
'''
Den = int(input('Son dnem: '))
Night = int(input('Son noch: '))
print('Son v sutki: ', Den + Night * 60)
'''

#Kolya
'''
a = int(input('Minuts: '))
print (a//60)
print (a%60)
'''

#Kate
'''
a = int(input('X Minutes: '))
hour = int(input('Hour: '))
minute = int(input('Minute: ')) 

print ((a // 60 + hour))
print ((a + minute)%60)
'''

#Math
#Variant 8

import math as ma

a = int(input('Vvedi a : '))
b = int(input('Vvedi b : '))
l = float(input('Vvedi l : '))

print('F = ', (2 * (1 - ma.pi)) / (b * b + l * l -1) + (2*ma.pi / (b * b + l * l -1)) * ma.tan(2))
print('a = ', a)
print('b = ', b)
print('l = ', l)
