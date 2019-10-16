# Secuencia Fibonachi
# 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13
# 0   1   2   3  (4)  5  (6)  (7)
################################
# a + a = b 
# b + a = c
# c + b = d
#################################

def fibo(n):
    a, b = 0,1
    while a < n:
        print(a, end = '')
        a, b = b, a+b
    print()
m = int(input("Ingresa límite máximo de la sucesión: ")) 
fibo(m)







 

