from paquete1.módulo1 import Cliente
#from paquete1.módulo2 import *

nombre = str(input('Nombre: ')).capitalize()
apellido =str(input('Apellido: ')).capitalize()
dni = int(input("DNI: "))
edad = int(input("Edad: "))
email = str(input('Email: '))
dirección = str(input('Dirección: '))
última_compra = str(input('Última compra: '))
local = str(input("Local: "))


cliente1 = Cliente(nombre, apellido, dni, edad, email, dirección, última_compra, local)

print(cliente1) 
print(cliente1.comprar)
print(cliente1.vivir)


