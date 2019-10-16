# DataBase
# Cabecera 
print("")
print("AGREGA USUARIOS A LA BASE DE DATOS")
print("")

# CRENADO DB
db = []

def agregar1(Users1):
    inser = db.append(Users1)
    return inser

# FUNCION INSERTAR AL LA DB
def menu():
    response = None
    while response not in ["1", "2", "3"]:
        response = input("""What do you want to do?
        1. Add Users
        2. Deleate Users
        3. Find Users\n""")
        print('')
    if response == "1":
        # Add Users
        # Inputs de datos a la db
        Users = input("Name: ")
        # Agrgando los datos a la db
        agregar1(Users)
        
    elif response == "2":
        # Deleate Users
        print("For Deleate User: ")
        Deleate = db.remove(input("Name: "))
        print(Deleate)

    elif response == "3":
         # Find Users
         print("For Find Users: ")
         print(db)
       
menu() 

# CONFIRMACION DE INGRESO DE DATOS A LA DB
def confir(agregar1):
    if agregar1 and True:
        print(' ')
        print("Succesfully User add to DB")
        print(' ')
        print(db)
    else:
        print(' ')
        print("Unsuccesfully User add to DB")
        print(' ')
        print(db)
confir(agregar1)

# Volver al menu
def munur():
  rmenu = input('Do you like return to menu y/n: ')
  if rmenu == 'y':
     menu()
  else:
      print(' ')
      print('FIN DEL PROGRAMA')
      print(' ')     

# Iteracion de datos
def iteracion():
    print(' ')
    condicion = input('Desea Seguir agregando usuarios dijita (y) de lo contrario dijite (n): ')
    if condicion == 'y':
        inicio= 0
        maximo = int(input('Dijita el maximo de usuarioa a registrar: '))
        while (inicio < maximo):
            inicio = inicio + 1
            # Agrgando los datos a la db
            Users = input("Name: ")
            # Agrgando los datos a la db
            agregar1(Users)
            confir(agregar1)
            print(' ')
            munur()
                
    elif condicion == 'n':
        print(' ')
        print('FIN DEL PROGRAMA')
        confir(agregar1)
        print(' ')
        

    else:
        print(' ')
        print('Only Write y/n')
        print(' ')
        print('FIN DEL PROGRAMA')
        print(' ')
        iteracion()

iteracion()

    