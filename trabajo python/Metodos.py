import pymongo
class Metodosdefinitivos:
    def __init__(self,cliente,db,coleccion):
        self.cliente = cliente
        self.db = self.cliente[db]
        self.coleccion = self.db[coleccion]
        
    def insertarContacto(self,datos):  
            self.coleccion.insert_one(datos)

    def eliminarContacto(self,nombre):
        self.coleccion.delete_one({"nombre":nombre})

    def actualizarContacto(self, nombre, NewNombre, NewApellido, NewTelefono, NewCorreo):
        query = {"nombre": nombre}
        update = {"$set": {"nombre": NewNombre, "apellido": NewApellido, "numero": NewTelefono, "correo": NewCorreo}}
        result = self.coleccion.update_one(query, update)

        
