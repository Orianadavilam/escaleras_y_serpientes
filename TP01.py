import random 

def main() -> None: 
    #Constantes con el valor de las opciones del MENU
    OP_NUEVA_PARTIDA:int = 1
    OP_MOSTRAR_ESTADISTICAS:int = 2
    OP_RESET_ESTADISTICAS:int = 3
    OP_SALIR_JUEGO:int = 4

    #Constante del diccionario con las posiciones de las escaleras y serpientes 
    POS_ESCALERAS_SERPIENTES:dict = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96, 86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}

    #Realizo la creacion del menú 
    print("Bienvenido al entretenido y maravilloso juego de 'SERPIENTES Y ESCALERAS'. Por favor ingrese una opción para continuar: ")
    print("Ingrese (1) para - INICIAR UNA NUEVA PARTIDA -")
    print("Ingrese (2) para - MOSTRAR ESTADÍSTICAS DE CASILLEROS - ")
    print("Ingrese (3) para - RESETEAR ESTADÍSTICAS DE CASILLEROS -")        
    print("Ingrese (4) para - SALIR - ")
    opcion_user:str = input("") 
    
    while not (opcion_user.isnumeric()) or int(opcion_user) not in range(1, 4+1):
        print("Por favor ingrese una opción válida:")
        opcion_user = input("")

    opcion:int = int(opcion_user)

    if (opcion == OP_NUEVA_PARTIDA): 
        print(" ----- INICIANDO NUEVA PARTIDA -----")
        print("")
        CANTIDAD_FILAS_TABLERO:int = 10
        CANTIDAD_COLUMNAS_TABLERO:int = 10
        ultima_pos_fila:int = 1 

        for fila in range(1, CANTIDAD_FILAS_TABLERO + 1):
            print(f"-- Fila {fila}:")
            for posicion in range(ultima_pos_fila, ultima_pos_fila+CANTIDAD_FILAS_TABLERO):
                print(posicion, end=' ')
            ultima_pos_fila = posicion + 1
            print("")

    elif (opcion == OP_MOSTRAR_ESTADISTICAS):
        print(" ----- ESTADISTICAS DEL JUEGO ----- ")
    elif (opcion == OP_RESET_ESTADISTICAS):
        print ("  ----- RESETEANDO ESTADISTICAS ----- ") 
    else: 
        #Opcion "SALIR"
        print(" ---- ESPERAMOS VERTE PRONTO PARA UNA NUEVA PARTIDA ----- ")
        exit() 

main()