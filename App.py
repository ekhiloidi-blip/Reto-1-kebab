import time

USUARIO_STR=str("usuario")
CONTRASENYA_INT=int(1234)

def menu_principal_str():
    print("\nElige la operación que necesites realizar: \n" \
    "1. Limpieza del dispostivo. \n" \
    "2. Diagnostico del dispositivo. \n" \
    "0. Cerrar el programa. \n")

def menu_diagnostico_str():
    print("¿Que problema necesitas solucionar?\n" \
    "1.Velocidad del dispositivo.\n" \
    "2.Sobrecalentamiento.\n" \
    "3.Almacenamiento reducido.\n" \
    "0.Volver atrás.\n")



incio_sesion_int=int(input("Bienvenido!! Elige una opción: \n" \
"1. Iniciar sesión.\n" \
"2. Continuar como invitado.\n"))

if incio_sesion_int==1:
    usuario_introducido_str=str(input("Nombre de usuario: "))
    contrasenya_introducida_int=int(input("Contraseña: "))


    if usuario_introducido_str==USUARIO_STR and contrasenya_introducida_int==CONTRASENYA_INT:
        print("Se ha iniciado la sesión correctamente.\n")

        opcion_menu_principal=-1
        while opcion_menu_principal != 0:

            (menu_principal_str())
            opcion_menu_principal=int(input("Selecciona una opción: "))

            if opcion_menu_principal == 1:
                print("Cargando...\n", end="", flush=True)
                for x in range(0,101,10):
                    print("█", end=" ", flush=True)#Para que el contador salga en la misma linea
                    time.sleep(0.4)
                print(x,"%")

                print("\nCarga completada")
                time.sleep(0.3)
                print ("limpieza con barra progresiva\n")

                print("Se han eliminado los archivos repetidos y temporales. La limpieza de tu dispositivo se ha realizado con éxito")          

            elif opcion_menu_principal == 2:
                
                opcion_menu_diagnostico=-1
                while opcion_menu_diagnostico !=0:

                    (menu_diagnostico_str())
                    opcion_menu_diagnostico=int(input("Selecciona una opción:\n "))

                    if opcion_menu_diagnostico==1:
                        pregunta_velocidad_1_int=int(input("¿Las aplicaciones tardan mucho en abrir? \n" \
                        "1.Si\n" \
                        "2.No\n"))
                        pregunta_velocidad_2_int=int(input("¿El dispositivo se queda completamente congelado/bloqueado por unos segundos?\n" \
                        "1.Si\n" \
                        "2.No\n "))
                        pregunta_velocidad_3_int=int(input("¿Ocurre principalmente cuando tienes muchas apps abiertas a la vez?\n"
                        "1.Si\n"
                        "2.No\n "))

                        if pregunta_velocidad_1_int==1 and pregunta_velocidad_2_int==1 and pregunta_velocidad_3_int==1:
                            print("Problema: Saturación grave del dispositivo (el procesador y la memoria van al límite).\n" \
                            "Solución: Haz un reinicio completo, elimina las aplicaciones que no uses y considera restaurar el dispositivo si el problema persiste.\n")

                        elif pregunta_velocidad_1_int==1 and pregunta_velocidad_2_int==1:
                            print("Problema: Lentitud generalizada en el sistema, independiente de las apps abiertas.\n" \
                            "Solución: Apaga el dispositivo durante un par de minutos, enciéndelo y comprueba si tienes actualizaciones pendientes del sistema.\n")

                        elif pregunta_velocidad_1_int==1 and pregunta_velocidad_3_int==1:
                            print("Problema: Falta de recursos para abrir apps mientras otras siguen funcionando de fondo.\n" \
                            "Solución: Desactiva las opciones de 'inicio automático' de algunas apps y cierra las de segundo plano antes de abrir una nueva.\n")

                        elif pregunta_velocidad_2_int==1 and pregunta_velocidad_3_int==1:
                            print("Problema: Bloqueos por saturación al exigirle multitarea al dispositivo.\n" \
                            "Solución: Evita mantener juegos o redes sociales abiertas al mismo tiempo y libera espacio en la memoria.\n")

                        elif pregunta_velocidad_1_int==1:
                            print("Problema: Sobrecarga puntual al iniciar aplicaciones (acumulación de caché o apps desactualizadas).\n" \
                            "Solución: Borra la memoria caché de las aplicaciones más pesadas y actualízalas desde la tienda de aplicaciones.\n")

                        elif pregunta_velocidad_2_int==1:
                            print("Problema: Fallo temporal del sistema operativo o procesos colgados.\n" \
                            "Solución: Reinicia el dispositivo para limpiar la memoria interna y cerrar errores del sistema.\n")

                        elif pregunta_velocidad_3_int==1:
                            print("Problema: Límite de memoria de trabajo (RAM) al usar varias tareas a la vez.\n" \
                            "Solución: Acostúmbrate a cerrar del todo las aplicaciones que ya no estés usando en el menú de aplicaciones recientes.\n")

                    elif opcion_menu_diagnostico==2:
                        pregunta_sobrecalentamiento_1_int=int(input("¿El dispositivo se calienta cuando está conectado al cargador? \n" \
                        "1.Si\n" \
                        "2.No\n"))

                        pregunta_sobrecalentamiento_2_int=int(input("¿Se calienta incluso cuando no lo estás usando activamente? \n" \
                        "1.Si\n" \
                        "2.No\n")) 

                        pregunta_sobrecalentamiento_3_int=int(input("¿La batería se descarga mucho más rápido de lo normal?\n" \
                        "1.Si\n" \
                        "2.No\n"))

                        if pregunta_sobrecalentamiento_1_int==1 and pregunta_sobrecalentamiento_2_int==1 and pregunta_sobrecalentamiento_3_int==1:
                            print("Problema: Posible deterioro o fallo físico de la batería / circuito de carga.\n" \
                            "Solución: Evita usar el dispositivo a altas temperaturas y llévalo a un servicio técnico para comprobar el estado de salud de la batería.\n")

                        elif pregunta_sobrecalentamiento_2_int==1 and pregunta_sobrecalentamiento_3_int==1:
                            print("Problema: Consumo constante de energía que desgasta la batería y genera calor.\n" \
                            "Solución: Revisa en los ajustes de 'Batería' qué aplicación está gastando más energía de lo normal y desinstalala si no es necesaria.\n")

                        elif pregunta_sobrecalentamiento_1_int==1 and pregunta_sobrecalentamiento_3_int==1:
                            print("Problema: Esfuerzo de la batería durante la carga que afecta a su autonomía diaria.\n" \
                            "Solución: Utiliza siempre el cargador y cable originales del fabricante para evitar picos de temperatura dañinos.\n")

                        elif pregunta_sobrecalentamiento_1_int==1 and pregunta_sobrecalentamiento_2_int==1:
                            print("Problema: Esfuerzo excesivo del sistema al cargar debido a tareas activas de fondo.\n" \
                            "Solución: Carga el dispositivo en un lugar fresco, sobre una superficie plana (evita la cama o sofás) y sin usarlo.\n")

                        elif pregunta_sobrecalentamiento_3_int==1:
                            print("Problema: Desgaste natural o uso elevado de energía por brillo alto/funciones activadas.\n" \
                            "Solución: Reduce el brillo de la pantalla, apaga el GPS y el Bluetooth cuando no los uses.\n")

                        elif pregunta_sobrecalentamiento_2_int==1:
                            print("Problema: Hay aplicaciones o procesos 'trabajando a escondidas' en segundo plano.\n" \
                            "Solución: Cierra todas las apps, revisa los permisos de ubicación en segundo plano y reinicia el equipo.\n")

                        elif pregunta_sobrecalentamiento_1_int==1:
                            print("Problema: Sobrecalentamiento normal o provocado por el tipo de carga.\n" \
                            "Solución: No uses el dispositivo mientras se carga y retira la funda protectora durante la carga si retiene mucho calor.\n")

                    elif opcion_menu_diagnostico ==3:
                        pregunta_almacenamiento_1_int=int(input("¿Te sale el mensaje de sistema 'Almacenamiento casi lleno'? \n"
                        "1.Si\n"
                        "2.No\n")) 
                        pregunta_almacenamiento_2_int=int(input("¿Tienes muchas fotos, vídeos o descargas antiguas sin borrar? \n"
                        "1.Si\n"
                        "2.No\n")) 
                    
                        if pregunta_almacenamiento_1_int==1:
                            print("Problema: La memoria se ha llenado con archivos invisibles (caché de WhatsApp, redes sociales o archivos temporales).\n" \
                            "Solución:  Limpia la memoria caché general del dispositivo y elimina las conversaciones o archivos pesados guardados dentro de las apps de mensajería.\n")
                        
                        elif pregunta_almacenamiento_2_int==1:
                            print("Problema: Acumulación de archivos personales. Aún tienes espacio, pero estás cerca del límite.\n" \
                            "Solución: Revisa tu galería, elimina los vídeos más largos, vacía la carpeta de descargas y la papelera de reciclaje.\n")    
                        
                        elif pregunta_almacenamiento_1_int==1 and pregunta_almacenamiento_2_int==1:
                            print("Problema: Memoria del dispositivo en estado crítico por exceso de archivos guardados.\n" \
                            "Solución: Pasa tus fotos y vídeos antiguos a un ordenador o a la nube (como Google Drive o iCloud) y borra del dispositivo todo lo que ya esté guardado a salvo.\n")    

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

elif incio_sesion_int==2:
    (menu_principal_str())
    opcion_menu_principal_invitado_int=int(input("Elige una opción:"))
    if opcion_menu_principal_invitado_int==1:
        print("Cargando...\n", end="", flush=True)
        for x in range(0,101,10):
            print("█", end=" ", flush=True)#Para que el contador salga en la misma linea
            time.sleep(0.4)
        print(x,"%")
    
        print("\nCarga completada")
        time.sleep(0.3)
    
        print("Se han eliminado los archivos repetidos y temporales. La limpieza de tu dispositivo se ha realizado con éxito")

    elif opcion_menu_principal_invitado_int==2:
        print("Debes de iniciar sesión para poder utilizar esta función.")

    elif opcion_menu_principal_invitado_int==0:
        print("Cerrando programa...")

    else:
        print("Opción no valida. Vuelve a intentarlo.")

else:
    print("Opción no valida, vuelve a intentarlo.")

    


