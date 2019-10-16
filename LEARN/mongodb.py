# MongoDB Local
# Importando librerias
import pymongo
from pymongo import MongoClient

# ENLAZANDO A LA DB
MONGO_URI = "mongodb://localhost"

client = MongoClient(MONGO_URI)

# CRENADO DB
db = client['ATON_BANK']
collections = db['USERS']

# Cabecera 
print("")
print("BASE DE DATOS ATÓN")
print("")

# FUNCION INSERTAR AL LA DB
def agregar1(Users1):
    inser = collections.insert_many([Users1]) 
    return inser
# Menú



# Inputs de datos a la db
print("")
print("AGREGA USUARIOS A LA BASE DE DATOS")
print("")
Users = {"_id":int(input("Cedula: ")),"Name":input("Name: "),"lastName":input("Last_Name: "),"Edad":int(input("Edad: ")),"Sexo":input("Sexo: ")}
# Agrgando los datos a la db
agregar1(Users)

# CONFIRMACION DE INGRESO DE DATOS A LA DB
def confir(agregar1):
    if agregar1 and True:
        print(' ')
        print("USUARIOS AGREGADOS CON EXITO")
        print(' ')
        results = collections.find()
        for r in results:
            print(r['Name'])
    else:
        print(' ')
        print("USUARIOS NO AGREGADOS CON EXITO")
        print(' ')
confir(agregar1)        

# ITERACION
condicion = input('Desea Seguir agregando usuarios dijita (yes) de lo contrario dijite (no): ')
if condicion == 'yes':
    inicio= 0
    maximo = int(input('Dijita el maximo de usuarioa a registrar: '))
    while (inicio < maximo):
        inicio = inicio + 1
        # Agrgando los datos a la db
        Users = {"_id":int(input("Cedula: ")),
        "Name":input("Name: "),"lastName":input("Last_Name: "),
        "Edad":int(input("Edad: ")),"Sexo":input("Sexo: ")}
        # Agrgando los datos a la db
        agregar1(Users)
        confir(agregar1)  
else:
    print(' ')
    print('FIN DEL PROGRAMA')
    print(' ')
    confir(agregar1)      

# COMANDOS DE MONGO
# ELIMINAR DB
# db.dropDatabase()
# BUSCAR EN LA DB
# db.collections.find({"Name":" "})
# ELIMINAR UN USUARIO
# db.USUARIOS.

   


  



 





