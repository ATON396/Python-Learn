def amigo():
    for i in ['A','M','I','G','O']:
        print(f"Dame una {i}")
    print("¡AMIGO!")

amigo()

def numeros():
    for i in [0,1,2,3,4,5,6,7,8,9]:
        print(f'{i} mas {i} es igual a {i+i}')  

numeros()  

def ParImpar():
    cuenta = 0
    cuenta2 = 0
    for i in range(0,101):
        if i % 2 == 0:
            cuenta =  cuenta + 1
            print ('Par = ',i)
        elif i % 2 != 0:
            cuenta2 =  cuenta2 + 1
            print('Impar = ',i)
    print('Hay ',cuenta,' Par en este rango y ',cuenta2,'Impar en el mismo rango. ' )         
ParImpar()    

def sumar():
    suma = 0
    for i in range(0,101):
        suma = suma + i
    print(f"La suma de los números de 0 a 100 es {suma}")
sumar()

       

