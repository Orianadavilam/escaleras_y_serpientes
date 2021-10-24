import random 

def crear_tablero(cantidad_filas:int, cantidad_columnas:int) -> list:
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

def obtener_casilleros_tweaks(POS_ESCALERAS_SERPIENTES:dict, TIPOS_TWEAKS:dict, maximo_casillero_tablero:int, CANTIDAD_COLUMNAS_TABLERO:int) -> dict:
    max_casilleros_piso:range = range(CANTIDAD_COLUMNAS_TABLERO, maximo_casillero_tablero + 1, CANTIDAD_COLUMNAS_TABLERO)
    min_casilleros_piso:range = range(1, maximo_casillero_tablero + 1, CANTIDAD_COLUMNAS_TABLERO)
    casilleros_tweaks:dict = {} #Retorno

    for tweak, cantidad in TIPOS_TWEAKS.items():
            #Por cada casillero especial 
        for item in range (cantidad): 
            posicion_reestringida:bool = True
                
            while (posicion_reestringida): 
                pos_aleatoria:int = random.randint(1, maximo_casillero_tablero) 

                if (pos_aleatoria not in POS_ESCALERAS_SERPIENTES.keys() and pos_aleatoria not in POS_ESCALERAS_SERPIENTES.values() and pos_aleatoria not in casilleros_tweaks):
                    #Todo va bien, porque no está sobreponiendose con ninguna existente
                    codigo_casillero:str = ""
                    if (tweak == "CASCARA_BANANA" and pos_aleatoria > (2 * CANTIDAD_COLUMNAS_TABLERO + 1)):
                        posicion_reestringida = False
                        codigo_casillero = "C"
                    elif ( tweak == "MAGICO" ):
                        posicion_reestringida = False
                        codigo_casillero = "M"
                    elif (tweak == "RUSHERO" and pos_aleatoria not in max_casilleros_piso):
                        posicion_reestringida = False
                        codigo_casillero = "R"
                    elif( tweak == "HONGOS_LOCOS" and  pos_aleatoria not in min_casilleros_piso):
                        posicion_reestringida = False
                        codigo_casillero = "H"

                    if (not posicion_reestringida):
                        casilleros_tweaks[pos_aleatoria] = codigo_casillero

    return casilleros_tweaks

def obtener_casilleros_especiales(POS_ESCALERAS_SERPIENTES:dict, TIPOS_TWEAKS:dict,  maximo_casillero_tablero:int, CANTIDAD_COLUMNAS_TABLERO:int) -> dict:
    #Completo primero con los tweaks
    casilleros_especiales:dict = obtener_casilleros_tweaks(POS_ESCALERAS_SERPIENTES, TIPOS_TWEAKS, maximo_casillero_tablero, CANTIDAD_COLUMNAS_TABLERO)

    #Ahora realizo la lógica de las escaleras/serpientes
    for casillero_inicial, casillero_final in POS_ESCALERAS_SERPIENTES.items():
        if (casillero_inicial < casillero_final):
            #Es una escalera
            casilleros_especiales[casillero_inicial] = "E"

        elif (casillero_inicial > casillero_final):
            #Es una serpiente 
            casilleros_especiales[casillero_inicial] = "S"

    return casilleros_especiales


def imprimir_tablero(tablero:list, casilleros_especiales:dict, jugadores:list) -> None:
    #Necesito que imprima las filas al reves 
    tablero.sort(reverse=True)

    for fila in range(len(tablero)):
        casilleros_fila:list = tablero[fila] 
        if (fila % 2 == 0):
            #Si la fila es par, ordeno de manera descendente
            casilleros_fila.sort(reverse=True)
        
        for casillero in casilleros_fila:
            if (casillero in casilleros_especiales.keys()):
                tipoCasillero:str = casilleros_especiales.get(casillero)
                print(f"| {casillero} ({tipoCasillero}) ", end=' ')
            else:    
                print(f"| {casillero}", end=' ')

            for jugador in jugadores:
                datos_jugador:dict = jugador

                if (casillero in datos_jugador.values()):
                    for nombre in datos_jugador.keys():
                        print(f" ({nombre})", end = '')

        print("")
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
    CANTIDAD_FILAS_TABLERO:int = 10
    CANTIDAD_COLUMNAS_TABLERO:int = 10 

    #Constante del diccionario dado con las casilleros de las escaleras y serpientes 
    POS_ESCALERAS_SERPIENTES:dict = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96, 86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}    
    opcion:int = 0

    while not (opcion == OP_SALIR_JUEGO):
        opcion = menu()

        if (opcion == OP_NUEVA_PARTIDA): 
            print(" ----- INICIANDO NUEVA PARTIDA -----")
            print("")
            hay_ganador:bool = False
            tablero:list = crear_tablero(CANTIDAD_FILAS_TABLERO, CANTIDAD_COLUMNAS_TABLERO) #Genera el tablero dinamicamente segun las filas y columnas
            maximo_casillero_tablero = CANTIDAD_FILAS_TABLERO * CANTIDAD_COLUMNAS_TABLERO #Dimension del tableros
            TIPOS_TWEAKS:dict = {"CASCARA_BANANA":5, "MAGICO":3, "RUSHERO":1, "HONGOS_LOCOS":1} #Nombre_tweak, cantidad
            casilleros_especiales:dict = obtener_casilleros_especiales(POS_ESCALERAS_SERPIENTES, TIPOS_TWEAKS,  maximo_casillero_tablero, CANTIDAD_COLUMNAS_TABLERO)
        
            #Obvio falta validar aqui el tema de que sean solo letras
            nombre_jugador_1:str = input("Ingrese el nombre del jugador 1: ")
            nombre_jugador_2:str = input("Ingrese el nombre del jugador 2: ")
            jugador_1:dict = {nombre_jugador_1 : 0} #Nombre : casillero_actual
            jugador_2:dict = {nombre_jugador_2 : 0} #Nombre : casillero_actual
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
                        accion:str = "avanzas" #Por default 

                        while (casillero_a_mover in casilleros_especiales):
                            tipo_casillero:str = casilleros_especiales.get(casillero_a_mover)
                            nombre_casillero:str = ""
                            casillero_nuevo:int 

                            if (tipo_casillero == "E" or tipo_casillero == "S"):
                                casillero_nuevo = POS_ESCALERAS_SERPIENTES.get(casillero_a_mover, 0)
                                if (tipo_casillero == "E"):
                                    nombre_casillero = "escalera"
                                else:
                                    nombre_casillero = "serpiente"

                            elif (tipo_casillero == "C"):
                                #DEBE CAER DOS PISOS
                                nombre_casillero = "cáscara de banana"
                                casillero_nuevo = casillero_a_mover - (2*CANTIDAD_COLUMNAS_TABLERO)      
                            elif (tipo_casillero == "M"):
                                #Calculo un nuevo numero de dados
                                nombre_casillero = "mágico"
                                #No puede caer en el minimo, maximo ni en el mismo porque genero un bucle
                                casilleros_reestringidos_magico:list = [1, maximo_casillero_tablero, casillero_a_mover]
                                while (casillero_nuevo in casilleros_reestringidos_magico):
                                    casillero_nuevo = random.randint(1, 6)
                        
                            elif (tipo_casillero == "R" or tipo_casillero == "H"):
                                numero_fila_casilla:int  = 0
                                for fila in range(len(tablero)):
                                    casilleros_fila:list = tablero[fila]
                                    for casilla in casilleros_fila:
                                        if (casillero_a_mover == casilla):
                                            numero_fila_casilla = fila

                                if (tipo_casillero == "R"):
                                #Se mueve hasta la maxima casilla de ese piso
                                    nombre_casillero = "rushero"
                                    casillero_nuevo = max(tablero[numero_fila_casilla])
                                
                                if (tipo_casillero == "H"):
                                #Se mueve a la minima casilla de ese piso
                                    nombre_casillero = "hongos locos"
                                    casillero_nuevo = min(tablero[numero_fila_casilla])                                                        
                        
                            if(casillero_nuevo < casillero_a_mover):
                                accion = "retrocedes"

                            casillero_a_mover = casillero_nuevo 

                            print(f"{nombre_jugador} caíste en casillero '{nombre_casillero}', así que {accion} hasta el casillero: {casillero_a_mover}")
                          
                        if casillero_a_mover < maximo_casillero_tablero :
                            print(f"{nombre_jugador} {accion} hasta la casillero: {casillero_a_mover}")               

                        if (casillero_a_mover >= maximo_casillero_tablero):
                            ganador_absoluto = nombre_jugador
                            hay_ganador = True
                            casillero_a_mover = maximo_casillero_tablero #Para que quede en la ultima posicion del tablero y no en una pos que no existe
                        
                        jugador[nombre_jugador] = casillero_a_mover
                        imprimir_tablero(tablero, casilleros_especiales, jugadores)
                
            print(f"FELICIDADES {ganador_absoluto}, GANASTE EN ESTA OPORTUNIDAD")
            print("")
        elif (opcion == OP_MOSTRAR_ESTADISTICAS):
            print(" ----- ESTADISTICAS DEL JUEGO ----- ")
        elif (opcion == OP_RESET_ESTADISTICAS):
            print ("  ----- RESETEANDO ESTADISTICAS ----- ") 

    print(" ---- ESPERAMOS VERTE PRONTO PARA UNA NUEVA PARTIDA ----- ")
     
main()