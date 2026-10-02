USUARIO_STR=str("usuario")
CONTRASENYA_INT=int(1234)

def menu_principal_str():
    print("Elige la operación que necesites realizar: \n" \
    "1. Limpieza del dispostivo. \n" \
    "2. Diagnostico del dispositivo. \n" \
    "0. Cerrar el programa. \n")

def menu_diagnostico_str():
    print("¿Que problema necesitas solucionar?\n" \
    "1.Velocidad del dispositivo.\n" \
    "2.Sobrecalentamiento.\n" \
    "3.Almacenamiento reducido.\n" \
    "0.Volver atrás.\n")

usuario_introducido_str=str(input("Nombre de usuario: "))
contrasenya_introducida_int=int(input("Contraseña: "))


if usuario_introducido_str==USUARIO_STR and contrasenya_introducida_int==CONTRASENYA_INT:
    print("Se ha iniciado la sesión correctamente.\n")

    opcion_menu_principal=-1
    while opcion_menu_principal != 0:

        (menu_principal_str())
        opcion_menu_principal=int(input("Selecciona una opción: "))

        if opcion_menu_principal == 1:
            print ("limpieza con barra progresiva\n")

        elif opcion_menu_principal == 2:
             
             opcion_menu_diagnostico=-1
             while opcion_menu_diagnostico !=0:

                (menu_diagnostico_str())
                opcion_menu_diagnostico=int(input("Selecciona una opción:\n "))

                if opcion_menu_diagnostico==1:
                    pregunta1_int=int(input("¿Las aplicaciones tardan mucho en abrir? \n" \
                    "1.Si\n" \
                    "2.No\n"))
                    pregunta2_int=int(input("¿El dispositivo se queda completamente congelado/bloqueado por unos segundos?\n" \
                    "1.Si\n" \
                    "2.No\n "))
                    pregunta3_int=int(input("¿Ocurre principalmente cuando tienes muchas apps abiertas a la vez?\n"
                    "1.Si\n"
                    "2.No\n "))

                    if pregunta1_int==1 and pregunta2_int==1 and pregunta3_int==1:
                        print("Problema: Saturación grave del dispositivo (el procesador y la memoria van al límite).\n" \
                        "Solución: Haz un reinicio completo, elimina las aplicaciones que no uses y considera restaurar el dispositivo si el problema persiste.\n")

                    elif pregunta1_int==1 and pregunta2_int==1:
                        print("Problema: Lentitud generalizada en el sistema, independiente de las apps abiertas.\n" \
                        "Solución: Apaga el dispositivo durante un par de minutos, enciéndelo y comprueba si tienes actualizaciones pendientes del sistema.\n")

                    elif pregunta1_int==1 and pregunta3_int==1:
                        print("Problema: Falta de recursos para abrir apps mientras otras siguen funcionando de fondo.\n" \
                        "Solución: Desactiva las opciones de 'inicio automático' de algunas apps y cierra las de segundo plano antes de abrir una nueva.\n")

                    elif pregunta2_int==1 and pregunta3_int==1:
                        print("Problema: Bloqueos por saturación al exigirle multitarea al dispositivo.\n" \
                        "Solución: Evita mantener juegos o redes sociales abiertas al mismo tiempo y libera espacio en la memoria.\n")

                    elif pregunta1_int==1:
                        print("Problema: Sobrecarga puntual al iniciar aplicaciones (acumulación de caché o apps desactualizadas).\n" \
                        "Solución: Borra la memoria caché de las aplicaciones más pesadas y actualízalas desde la tienda de aplicaciones.\n")

                    elif pregunta2_int==1:
                        print("Problema: Fallo temporal del sistema operativo o procesos colgados.\n" \
                        "Solución: Reinicia el dispositivo para limpiar la memoria interna y cerrar errores del sistema.\n")

                    elif pregunta3_int==1:
                        print("Problema: Límite de memoria de trabajo (RAM) al usar varias tareas a la vez.\n" \
                        "Solución: Acostúmbrate a cerrar del todo las aplicaciones que ya no estés usando en el menú de aplicaciones recientes.\n")

                elif opcion_menu_diagnostico==2:
                    print("Sobrecalentamiento\n")

                elif opcion_menu_diagnostico ==3:
                    print("Almacenamiento\n")

                elif opcion_menu_diagnostico==0:
                    print("Volver atrás\n")

                else:
                    print("opción no valida. intentalo de nuevo.")
            
        elif opcion_menu_principal==0:
            print("Cerrando el programa...")

        else:
            print("Opción no valida. Intentalo de nuevo.\n")
else:
    print("Usuario y/o contraseña incorrecta. Vuelve a intentarlo.")


