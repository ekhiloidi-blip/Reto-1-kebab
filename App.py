USUARIO_STR=str("usuario")
CONTRASENYA_INT=int(1234)

def menu_principal_str():
    print("Elige la operación que necesites realizar: \n" \
    "1. Limpieza del dispostivo. \n" \
    "2. Diagnostico del dispositivo. \n" \
    "0. Cerrar el programa. \n")

usuario_introducido_str=str(input("Nombre de usuario: "))
contrasenya_introducida_int=int(input("Contraseña: "))

if usuario_introducido_str==USUARIO_STR and contrasenya_introducida_int==CONTRASENYA_INT:
    print("Se ha iniciado la sesión correctamente.\n")
    input(menu_principal_str())

    while menu_principal_str != 0:
        if menu_principal_str == 1:
            print ("limpieza")
        if menu_principal_str == 2:
            print ("diagnostico del dispositivo")
else:
    print("Usuario y/o contraseña incorrecta. Vuelve a intentarlo.")


