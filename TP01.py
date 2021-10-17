import random 
import time

def crearTablero(cantidad_filas:int, cantidad_columnas:int) -> list:
    #Crea un tablero con la cantidad de filas y el numero de casilleros de cada una
    #Retorna una lista de filas de tamaño "cantidad_columnas"
    ultimo_casillero_fila_anterior:int = 1 
    tablero:list = []

    for fila in range(1, cantidad_filas+1):
        casilleros_fila:list = []

        for casillero in range(ultimo_casillero_fila_anterior, ultimo_casillero_fila_anterior + cantidad_columnas):
            casilleros_fila.append(casillero)
        
        ultimo_casillero_fila_anterior = casillero + 1
        tablero.append(casilleros_fila)

    return tablero

def imprimirTablero(tablero:list, posiciones_especiales:dict, jugadores:list) -> None:
    #Necesito que imprima las filas al reves 
    tablero.sort(reverse=True)

    for fila in range(len(tablero)):
        casilleros_fila:list =  tablero[fila] 
        if (fila % 2 == 0):
            #Si la fila es par, ordeno de manera descendente
            casilleros_fila.sort(reverse=True)
        
        for casillero in casilleros_fila:
            if (casillero in posiciones_especiales.keys()):
                if ( casillero < posiciones_especiales.get(casillero, 0)):
                    #Es una escalera 
                    print(f"| {casillero} (E)", end=' ')
                elif (casillero > posiciones_especiales.get(casillero)): 
                    #Es una serpiente (ponele)
                    print(f"| {casillero} (S)", end=' ')                    
            else:    
                print(f"| {casillero}", end=' ')

            for jugador in jugadores:
                datos_jugador:dict = jugador

                if (casillero in datos_jugador.values()):
                    for nombre in datos_jugador.keys():
                        print(f" ({nombre})", end = '')

        print("")

def main() -> None: 
    #Constantes
    CANTIDAD_OPCIONES_MENU:int = 4
    OP_NUEVA_PARTIDA:int = 1
    OP_MOSTRAR_ESTADISTICAS:int = 2
    OP_RESET_ESTADISTICAS:int = 3
    OP_SALIR_JUEGO:int = 4
    CANTIDAD_FILAS_TABLERO:int = 10
    CANTIDAD_COLUMNAS_TABLERO:int = 10

    #Constante del diccionario con las casilleroes de las escaleras y serpientes 
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
        nombre_jugador_1:str = "Ori" #input("Ingrese el nombre del jugador 1: ")
        nombre_jugador_2:str = "Jesus" #input("Ingrese el nombre del jugador 2: ")
        jugador_1:dict = {nombre_jugador_1 : 0} #Nombre : valor_dados
        jugador_2:dict = {nombre_jugador_2 : 0} #Nombre : valor_dados
        jugadores:list = [jugador_1, jugador_2]
        tablero:list = crearTablero(CANTIDAD_FILAS_TABLERO, CANTIDAD_COLUMNAS_TABLERO)

        while not hay_ganador:
            #input(f"{nombre_jugador_1} por favor presiona una tecla para lanzar los dados")
            valor_dados = random.randint(1, 6)
            print(f"{nombre_jugador_1} sacaste un: {valor_dados}")
            time.sleep(1)

            jugador_1 [nombre_jugador_1] += valor_dados
            casillero_a_mover = jugador_1.get(nombre_jugador_1)   

            if (casillero_a_mover in POS_ESCALERAS_SERPIENTES):
                accion:str = "avanzas"
                nombre_casilla = "escalera"

                casillero_nueva = POS_ESCALERAS_SERPIENTES.get(casillero_a_mover, 0)

                if(casillero_a_mover > casillero_nueva):
                    accion = "retrocedes"
                    nombre_casilla = "serpiente"

                casillero_a_mover = casillero_nueva    
                print(f"{nombre_jugador_1} caíste en una {nombre_casilla}, así que {accion} hasta la casillero: {casillero_a_mover}")
            else:
                print(f"{nombre_jugador_1} avanzas hasta la casillero: {casillero_a_mover}")
            
            time.sleep(1)
            jugador_1 [nombre_jugador_1] = casillero_a_mover
            hay_ganador = jugador_1.get(nombre_jugador_1) >= CANTIDAD_FILAS_TABLERO * CANTIDAD_COLUMNAS_TABLERO

            imprimirTablero(tablero, POS_ESCALERAS_SERPIENTES, jugadores)
            
    elif (opcion == OP_MOSTRAR_ESTADISTICAS):
        print(" ----- ESTADISTICAS DEL JUEGO ----- ")
    elif (opcion == OP_RESET_ESTADISTICAS):
        print ("  ----- RESETEANDO ESTADISTICAS ----- ") 
    else: 
        #Opcion "SALIR"
        print(" ---- ESPERAMOS VERTE PRONTO PARA UNA NUEVA PARTIDA ----- ")
        exit() 

main()