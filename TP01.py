import random 
import time

def main() -> None: 
    #Constantes
    CANTIDAD_OPCIONES_MENU:int = 4
    OP_NUEVA_PARTIDA:int = 1
    OP_MOSTRAR_ESTADISTICAS:int = 2
    OP_RESET_ESTADISTICAS:int = 3
    OP_SALIR_JUEGO:int = 4
    CANTIDAD_FILAS_TABLERO:int = 10
    CANTIDAD_COLUMNAS_TABLERO:int = 10

    #Constante del diccionario con las posiciones de las escaleras y serpientes 
    POS_ESCALERAS_SERPIENTES:dict = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96, 86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}

    #Realizo la creacion del menú 
    print("Bienvenido al entretenido y maravilloso juego de 'SERPIENTES Y ESCALERAS'. Por favor ingrese una opción para continuar: ")
    print("Ingrese (1) para - INICIAR UNA NUEVA PARTIDA -")
    print("Ingrese (2) para - MOSTRAR ESTADÍSTICAS DE CASILLEROS - ")
    print("Ingrese (3) para - RESETEAR ESTADÍSTICAS DE CASILLEROS -")        
    print("Ingrese (4) para - SALIR - ")
    opcion_menu_user:str = input("")
   
    while not (opcion_menu_user.isnumeric()) or int(opcion_menu_user) not in range(1, CANTIDAD_OPCIONES_MENU+1):
        print("Por favor ingrese una opción de menú válida:")
        opcion_menu_user = input("")

    opcion:int = int(opcion_menu_user)

    if (opcion == OP_NUEVA_PARTIDA): 
        print(" ----- INICIANDO NUEVA PARTIDA -----")
        print("")
        hay_ganador:bool = False

        #Obvio falta validar aqui el tema de que sean solo letras
        nombre_jugador_1:str = input("Ingrese el nombre del jugador 1: ")
        nombre_jugador_2:str = input("Ingrese el nombre del jugador 2: ")
        jugador_1:dict = {nombre_jugador_1 : 0} #Nombre : valor_dados
        jugador_2:dict = {nombre_jugador_2 : 0} #Nombre : valor_dados

        while not hay_ganador:
            input(f"{nombre_jugador_1} por favor presiona una tecla para lanzar los dados")
            valor_dados = random.randint(1, 6)
            print(f"{nombre_jugador_1} sacaste un: {valor_dados}")
            time.sleep(1)

            jugador_1 [nombre_jugador_1] += valor_dados
            posicion_a_mover = jugador_1.get(nombre_jugador_1)   

            if (posicion_a_mover in POS_ESCALERAS_SERPIENTES):
                accion:str = "avanzas"
                nombre_casilla = "escalera"

                posicion_nueva = POS_ESCALERAS_SERPIENTES.get(posicion_a_mover, 0)

                if(posicion_a_mover > posicion_nueva):
                    accion = "retrocedes"
                    nombre_casilla = "serpiente"

                posicion_a_mover = posicion_nueva    
                print(f"{nombre_jugador_1} caíste en una {nombre_casilla}, así que {accion} hasta la posicion: {posicion_a_mover}")
            else:
                print(f"{nombre_jugador_1} avanzas hasta la posicion: {posicion_a_mover}")
            
            time.sleep(1)
            jugador_1 [nombre_jugador_1] = posicion_a_mover
            hay_ganador = jugador_1.get(nombre_jugador_1) >= CANTIDAD_FILAS_TABLERO * CANTIDAD_COLUMNAS_TABLERO

            ultima_pos_fila:int = CANTIDAD_FILAS_TABLERO * CANTIDAD_COLUMNAS_TABLERO + 1
        
            for fila in range(1, CANTIDAD_FILAS_TABLERO + 1):
                posicion_desde:int = ultima_pos_fila - 1
                posicion_nueva:int = ultima_pos_fila - CANTIDAD_COLUMNAS_TABLERO - 1
                step:int = -1

                if (fila % 2 == 0):
                    #Si la fila es par, voy en orden descendente
                    posicion_desde = ultima_pos_fila - CANTIDAD_COLUMNAS_TABLERO
                    posicion_nueva = ultima_pos_fila 
                    step = 1

                for posicion in range(posicion_desde, posicion_nueva, step):
                    if (posicion in POS_ESCALERAS_SERPIENTES.keys() or posicion == jugador_1.get(nombre_jugador_1)):
                        if ( posicion in POS_ESCALERAS_SERPIENTES.keys() and posicion < POS_ESCALERAS_SERPIENTES.get(posicion, 0)):
                            #Es una escalera 
                            print(f"| {posicion} (E)", end=' ')
                        elif (posicion in POS_ESCALERAS_SERPIENTES.keys() and posicion > POS_ESCALERAS_SERPIENTES.get(posicion)): 
                            #Es una serpiente (ponele)
                            print(f"| {posicion} (S)", end=' ')                    
                    else:    
                        print(f"| {posicion}", end=' ')

                    if(posicion == jugador_1.get(nombre_jugador_1)):
                        print(f"| {posicion} ({nombre_jugador_1})", end=' ')

                print("|")
                if (fila % 2 == 0):
                    ultima_pos_fila = posicion_desde
                else:
                    ultima_pos_fila = posicion

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