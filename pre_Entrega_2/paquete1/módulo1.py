class Cliente:
    def __init__(self, nombre, apellido, dni,  edad, email, dirección, última_compra, local):
        print(f'Creando al cliente {nombre}, {apellido}')
        self.nombre = nombre
        self.apellido = apellido
        self.dni = int.dni
        self.edad = edad
        self.email = email
        self.dirección = dirección
        self.última_compra = última_compra
        self.local = local


    def __str__(self):
       return f"Nombre: "+{self.nombre} + "\nApellido: "+{self.apellido}
    
    def comprar(self):
        print("El cliente: {self.nombre} compró: {self.última_compra}")

    def vivir(self):
        print("El cliente: {self.nombre} vive en: {self.dirección}")


    

    

    




