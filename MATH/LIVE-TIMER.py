# |* LIVE | TIMER *|
# Librerias importadas
import math
# Draw.
print("- - - " * 9)
print("|* LIVE | TIMER *|" * 3)
print("- - - " * 9)

# The Sofware Start.
print(".")
print('|------ESTE PROGRAMA CALCULA TU EL TIEMPO QUE HAS DORMIDO Y HAS ESTADO DESPIERTO DURANTE TU VIDA------|\n.')

# Inputs User | Var.
name = input('¿Cual es tu nombre?: ' )
uyeards = int(input('¿Cuantos años tienes? : ' ))
usueño = int(input('¿Cunatas horas diarias duermes? : ' ))

# Software Logic Start.
# Años de Sueño
shora = (usueño * 30 )* 12
sdias =  shora / 24 
saños = sdias / 365.25
sdtoatal0 = saños * uyeards

print(' // - - - ' * 4)

if  sdtoatal0 <= 1:
    ddias0 = math.floor(sdtoatal0 * 365.25)
    adias1 =  math.floor( (uyeards * 365.25) - ddias0)   
    print(name,' has estado durante estos ',uyeards,' años\n',ddias0,' dias !!Dormiendo¡¡' )
    print( adias1,' dias !!Activo¡¡' )    
else :  
    satotal2 = math.floor(sdtoatal0)
    destotal4 =  math.floor(uyeards - satotal2) 
    print(name,' has estado durante estos ',uyeards,' años\n',satotal2,' años !!Dormiendo¡¡' )
    print( destotal4,' años !!Activo¡¡' ) 

# Att: Aton-396 
# My first alone code.


      






