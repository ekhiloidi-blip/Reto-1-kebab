USUARIO_STR=str("usuario")
CONTRASENYA_INT=int(1234)

MENU_PRINCIPAL_STR=str("Elige la operación que necesites realizar: \n" \
"1.Limpieza del dispostivo. \n" \
"2. Diagnostico del dispositivo. \n" \
"0. Cerrar el programa. \n")

usuario_introducido_str=str(input("Nombre de usuario: "))
contrasenya_introducida_int=int(input("Contraseña: "))

if usuario_introducido_str==USUARIO_STR and contrasenya_introducida_int==CONTRASENYA_INT:
    print("Se ha iniciado la sesión correctamente.\n")
    print(MENU_PRINCIPAL_STR)

else:
    print("Usuario y/o contraseña incorrecta. Vuelve a intentarlo.")


