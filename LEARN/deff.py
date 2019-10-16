# librerias 
import math

print(' ')
print('Funcion A')
print(' ')
# Funcion A
print('Halla la Hipotenusa')
print(' ')
def operacionA():
    bnum = int(input('CATETO UNO: '))
    cnum = int(input('CATETO DOS: '))
    rnum = math.hypot(bnum, cnum)
    print('Hipotenusa es igual a : ', rnum)

operacionA() 
  
# //________//________//_________//__________//
print(' ')
print('Funcion B')
print(' ')
# //________//________//_________//__________//

# Funcion B 
def operacionB(bnum,cnum):
    o = math.hypot(bnum, cnum)
    return o
rh = operacionB(int(input('CATETO UNO: ')), int(input('CATETO DOS: ')) )

print('Hipotenusa es igual a : ',rh)
print(' ') 
print('Fin')
print(' ')


# //- - - Comentario - - -//    
# Tanto Funcion A como Funcion B
#son la misma solo que escrita de diferente forma.