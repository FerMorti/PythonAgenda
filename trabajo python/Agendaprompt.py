import pymongo
import Metodos

client=pymongo.MongoClient("mongodb://localhost:27017/")
db = client["DAW"]
coleccion = db["DAW"]
agenda=Metodos.Metodosdefinitivos(client,"DAW","DAW")

opcion = 0
while opcion < 4:
    print("")
    print("")
    print("")
    print("----'\U0001F603'-Bienvenido-'\U0001F603'----")
    print("  -----------A-----------")
    print("      ------TU-------")
    print("        --AGENDA--")
    print("     ----------------")
    print("  -----------------------")
    print("")
    print("--¿Qué deseas hacer?--")
    print("")
    print("1. Ingresar un contacto.")
    print("2. Borrar un contacto.")
    print("3. Actualizar los detalles de un contacto.")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        Xusuario = input("Dime el nombre: ") 
        Xapellido = input("Dime el apellido: ")  
        Xtelefono = input("Dime el teléfono: ")
        Xcorreo = input ("Dime el correo: ")  
        datos = {"nombre": Xusuario, "apellido": Xapellido, "numero": Xtelefono, "correo": Xcorreo}
        agenda.insertar(datos)

    elif opcion == 2:
        nombre=input("Introduce el nombre del contacto a borrar:")
        print(" ")
        print(" ")
        agenda.eliminar(nombre)
        print("El contacto se eliminó de forma adecuada.")

    elif opcion == 3:
        nombre = input("Introduce el nombre del contacto a actualizar:  ")
        NewNombre = input("Introduce el nombre: ")
        NewApellido = input("Introduce el apellido: ")
        NewTelefono = input("Introduce el número de teléfono: ")
        NewCorreo = input ("Introduce el correo: ") 
        agenda.actualizar(nombre, NewNombre, NewApellido, NewTelefono, NewCorreo)

    