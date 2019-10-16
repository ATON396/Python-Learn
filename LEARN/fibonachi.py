# SECUENCIA FINONACHI
# 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13
#   a     b   c   d
################################
# a , b = 0, 1
# a + a = b 
# b + a = c
# c + b = d
#################################
# FUNCION
def fib(numMax):
    #VARIABLES
    a, b = 0, 1
    # BUCLE
    while a < numMax:
        # IMPRIMIR SUCECIÓN HORIZONTAL
        print(a, end = ' ; ')
        # LOGICA
        a, b = b, a+b
# INPUTS = numMax    
G = int(input("Ingresa nuemro máximo de la sucesión: ")) 
# ACTIVAR LA FUNCIÓN
fib(G)


