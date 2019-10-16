
i= int(input("Comiensa(X) MIlEs: "))
f = int(input("Termina(X) MILEs: "))

def ecua (tt):
            P1 = 12000
            Pf = 60
            PF = tt*(P1-(Pf*tt))
            print(PF)

for tt in range(i,f):
    if tt >= 0:
      print(tt,ecua(tt))
