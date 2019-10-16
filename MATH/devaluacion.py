
#DEPRESISACION DE PRODUCTOS EN FUNCION AL TIEMPO
# Funcion PRECIO DEVALUADO SOBRE AÑO 
#VARIABLES P1(PRECION INICIAL ES DECIR PRECIO EN EL AÑO 0); Pf(Precio al cabo de 16 años); DA(VALOR DE DEPRECIACION AL AÑO);t(tIEMPO EN AÑOS) 


i= int(input("Comiensa(t)en años: "))
f = int(input("Termina(t)en años: "))

def ecua (tt):
            P1 = 224000
            Pf = 11500
            DA = (P1 - Pf) / 16
            PF = P1-(DA*tt) # y = M(x)+b [DA(t)-P1]
            print(PF)

for tt in range(i,f):
    if tt >= 0:
      print(tt,ecua(tt))