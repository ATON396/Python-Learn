# Conversor de Tiempo.
# librerias importadas.
from decimal import Decimal
# Menú Input
print('')
print(' Conversor de Tiempo')
print('')
print(' Dijitar los que aparece dentro de los ()')
print('')
print('')


print(''' Convertir de: Años = (A)
              Meses = (M)
              Semanas = (S)
              Dias = (D)
              Horas = (H)
              Minutos = (Min)
              Seg = (Seg)
              ''')
De = input(' Convertir de: ')
DeNumber = int(input(' Valor: '))              

print(''' a :          Años = (A)
              Meses = (M)
              Semanas = (S)
              Dias = (D)
              Horas = (H)
              Minutos = (Min)
              Seg = (Seg)
              ''')
a = input('a : ')


# Desarrollo

# De Años a (A, M, S, D, H, Min, Seg);
if De == 'A' and a == 'A':
    print('')
    print('Resultado: ', DeNumber ,'Años.')
    print('')

elif  De == 'A' and a == 'M':
    r =  DeNumber * 12
    print('')
    print('Resultado: ', r ,'Meses.') 
    print('')   

elif  De == 'A' and a == 'S':
    r =  (DeNumber * 12)* Decimal(4.34822)
    print('')
    print('Resultado: ', r ,'Semanas.') 
    print('') 

elif  De == 'A' and a == 'D':
    r =  ((DeNumber * 12)* Decimal(4.34822))*7
    print('')
    print('Resultado: ', r ,'Dias.') 
    print('') 

elif  De == 'A' and a == 'H':
    r =  (((DeNumber * 12)* Decimal(4.34822))*7)*24
    print('')
    print('Resultado: ', r ,'Horas.') 
    print('')




              





