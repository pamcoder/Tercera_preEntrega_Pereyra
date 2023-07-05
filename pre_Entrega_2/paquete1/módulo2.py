import json

def cargar(diccionario, list1, list2):
    name = str(input("Ingrese Nombre del Usuario: "))
    password = str(input("Ingrese Contraseña de Usuario [Puede incluir caracteres alfanuméricos]: "))

    list1 += [name]
    list1 += [password]
    print("\nUsuario creado correctamente\n")

def muestreo(diccionario, list1, list2):
    print("Lista de Usuarios")
    print("---------------------------------------------------")
    nombres = diccionario["Nombres"]

    for i in range(len(list1)):
        print(f'{i+1}.{nombres[i]}')

    num = int(input("\nElija un Usuario para imprimir credenciales: "))
    print(f'Nombre:  {list1[num-1]}, Contraseña: {list2[num-1]}')

def imprimir(diccionario,list1,list2):
    print("Lista de Usuarios")
    print("-----------------------------------------------------")
    nombres = diccionario["Nombres"]
    for i in range(len(list1)):
        print(f'{i+1}.{nombres[i]}')

    num = int(input("\nElija un Usuario para imprimir credenciales: "))
    archivo = open("lista.json", "w")
    data = f'Name: {list1[num-1]}, Password: {list2[num-1]}'
    json.dump(data,archivo)
    archivo.close

def login(diccionario,list1,list2):
    name = str(input("Nombre del Usuario: "))
    while name not in list1:
        name = str(input("Error...Usuario incorrecto. Vuelva a ingresar: "))
        pos = list1.index(name)
        password = str(input("Contraseña: "))
    if password != list2[pos]:
        password = str(input("Error...Contraseña incorrecta. Vuelva a ingresar: "))
    elif name in list: 
        name = str(input("Error...Usuario ya existente. Vuelva a ingresar: "))
    else:
        print("Se ha logueado correctamente")


Namelist = []
Passwordlist = []
BaseDatos = {}

BaseDatos = {"Nombres": Namelist, "Contraseñas": Passwordlist}

print("Bienvenido....\n")
while True:
    print("---------------------------------------------------------------")
    print("Menú de inicio\n")
    print("1-Crear Usuario \n2.Ver Credencial Usuario \n3.Imprimir Credencial Usuario \n4.Loguearse \n5.Salir")
    opcion = int(input("Qué desea realizar?[1-5]: "))
    print("---------------------------------------------------------------")

    if opcion ==1:
        cargar(Namelist,Passwordlist)
    if opcion ==2:
        muestreo(BaseDatos, Namelist, Passwordlist)
    if opcion ==3:
        print(BaseDatos, Namelist, Passwordlist)
    if opcion ==4:
        login(BaseDatos, Namelist, Passwordlist)
    if opcion ==5:
        exit()
    break

    Input("Presione ENTER para volver al menú")