import math
import numpy

lista=[]

def agregar1(nuser, puser):
    c = lista.insert(puser,nuser)
    return c
agregar1(input('Agrega un nuevo nombre: '),int(input('Agrega su pocicion en la lista: ')))

print(' ')
print('Nuevo usuario agregado: ',lista[0])
print(' ')


# //- - - - - // - - - - -//


condicion = input('Seguir agregando usuarios dijita (yes) de lo contrario dijite (no): ')

if condicion == 'yes':
    inicio= 0
    maximo = int(input('Dijita el maximo de usuarioa a registrar: '))
    while (inicio < maximo):
        inicio = inicio + 1
        agregar1(input('Agrega un nuevo nombre: '),int(input('Agrega su pocicion en la lista: ')))
        print(' ')
        print('Nuevo usuario agregado: ', lista[1:])
        print(' ')
        print('Usuarios Registrados: ','\n','\n',lista[:])
        print(' ')
        print(' ')
else: 
    print(' ')
    print('FIN DEL PROGRAMA')
    print(' ')      




