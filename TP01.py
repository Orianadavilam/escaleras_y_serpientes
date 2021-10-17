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

def menu() -> int:
    #Crea el menu y retorna la opcion escogida por el usuario
    #Realizo la creacion del menú 
    CANTIDAD_OPCIONES_MENU:int = 4
    print("Bienvenido al entretenido y maravilloso juego de 'SERPIENTES Y ESCALERAS'. Por favor ingrese una opción para continuar: ")
    print("Ingrese (1) para - INICIAR UNA NUEVA PARTIDA -")
    print("Ingrese (2) para - MOSTRAR ESTADÍSTICAS DE CASILLEROS - ")
    print("Ingrese (3) para - RESETEAR ESTADÍSTICAS DE CASILLEROS -")        
    print("Ingrese (4) para - SALIR - ")
    opcion_menu_user:str = input("")
   
    while not (opcion_menu_user.isnumeric()) or int(opcion_menu_user) not in range(1, CANTIDAD_OPCIONES_MENU+1):
        print("Por favor ingrese una opción de menú válida:")
        opcion_menu_user = input("")

    return int(opcion_menu_user)


def main() -> None: 
    #Constantes
    OP_NUEVA_PARTIDA:int = 1
    OP_MOSTRAR_ESTADISTICAS:int = 2
    OP_RESET_ESTADISTICAS:int = 3
    OP_SALIR_JUEGO:int = 4
    CANTIDAD_FILAS_TABLERO:int = 5
    CANTIDAD_COLUMNAS_TABLERO:int = 5 

    #Constante del diccionario con las casilleroes de las escaleras y serpientes 
    POS_ESCALERAS_SERPIENTES:dict = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96, 86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}
    opcion:int = menu()

    if (opcion == OP_NUEVA_PARTIDA): 
        print(" ----- INICIANDO NUEVA PARTIDA -----")
        print("")
        hay_ganador:bool = False
        tablero:list = crearTablero(CANTIDAD_FILAS_TABLERO, CANTIDAD_COLUMNAS_TABLERO)

        #Obvio falta validar aqui el tema de que sean solo letras
        maximo_casillero_tablero = CANTIDAD_FILAS_TABLERO * CANTIDAD_COLUMNAS_TABLERO #Dimension del tablero
        nombre_jugador_1:str = input("Ingrese el nombre del jugador 1: ")
        nombre_jugador_2:str = input("Ingrese el nombre del jugador 2: ")
        jugador_1:dict = {nombre_jugador_1 : 0} #Nombre : casillero
        jugador_2:dict = {nombre_jugador_2 : 0} #Nombre : casillero
        jugadores:list = [jugador_1, jugador_2]
        ganador_absoluto:str = ""
    
        while not hay_ganador:
            for jugador in jugadores:
                if (len(ganador_absoluto) == 0):
                    #No necesito que lo haga si ya hay un ganador
                    for nombre in jugador.keys():
                        nombre_jugador:str = nombre
                    
                    input(f"{nombre_jugador} por favor presiona enter para lanzar los dados")
                    valor_dados = random.randint(1, 6)
                    print(f"{nombre_jugador} sacaste un: {valor_dados}")
                    jugador[nombre_jugador] += valor_dados
                    casillero_a_mover = jugador.get(nombre_jugador)   

                    if (casillero_a_mover in POS_ESCALERAS_SERPIENTES):
                        accion:str = "avanzas"
                        nombre_casilla = "escalera"
                        casillero_nuevo = POS_ESCALERAS_SERPIENTES.get(casillero_a_mover, 0)

                        if(casillero_nuevo < casillero_a_mover):
                            accion = "retrocedes"
                            nombre_casilla = "serpiente"

                        casillero_a_mover = casillero_nuevo    
                        print(f"{nombre_jugador} caíste en una {nombre_casilla}, así que {accion} hasta la casillero: {casillero_a_mover}")
                    elif casillero_a_mover < maximo_casillero_tablero :
                        print(f"{nombre_jugador} avanzas hasta la casillero: {casillero_a_mover}")               

                    if (casillero_a_mover >= maximo_casillero_tablero):
                        ganador_absoluto = nombre_jugador
                        hay_ganador = True
                        casillero_a_mover = CANTIDAD_FILAS_TABLERO * CANTIDAD_COLUMNAS_TABLERO #Para que quede en la ultima posicion del tablero
                    
                    jugador[nombre_jugador] = casillero_a_mover
                    imprimirTablero(tablero, POS_ESCALERAS_SERPIENTES, jugadores)
            
        print(f"FELICIDADES {ganador_absoluto}, GANASTE EN ESTA OPORTUNIDAD")
        print("")
        menu()
            
    elif (opcion == OP_MOSTRAR_ESTADISTICAS):
        print(" ----- ESTADISTICAS DEL JUEGO ----- ")
    elif (opcion == OP_RESET_ESTADISTICAS):
        print ("  ----- RESETEANDO ESTADISTICAS ----- ") 
    else: 
        print(" ---- ESPERAMOS VERTE PRONTO PARA UNA NUEVA PARTIDA ----- ")
        exit() 

main()