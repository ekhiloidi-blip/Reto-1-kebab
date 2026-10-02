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

    opcion=-1
    while opcion != 0:
        (menu_principal_str())
        opcion=int(input("Selecciona una opcion: "))

        if opcion == 1:
            print ("limpieza\n")
        elif opcion == 2:
            print ("diagnostico del dispositivo\n")
        elif opcion==0:
            print("Cerrando el programa...")
        else:
            print("Opción no valida. Intentalo de nuevo.\n")
else:
    print("Usuario y/o contraseña incorrecta. Vuelve a intentarlo.")


