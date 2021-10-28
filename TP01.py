import random 

#Constantes para las opciones del menú
CANTIDAD_OPCIONES_MENU:int = 4
OPCION_NUEVA_PARTIDA:int = 1
OPCION_MOSTRAR_ESTADISTICAS:int = 2
OPCION_RESET_ESTADISTICAS:int = 3
OPCION_SALIR_JUEGO:int = 4

#Constantes configuracion tablero 
CANTIDAD_FILAS_TABLERO:int = 10
CANTIDAD_COLUMNAS_TABLERO:int = 10

#Constantes configuracion del juego
CANTIDAD_JUGADORES:int = 2 
CASILLEROS_ESCALERAS_SERPIENTES:dict = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96, 86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}
TIPOS_CASILLAS_ESPECIALES:dict 
TIPOS_TWEAKS:dict = {"CASCARA_BANANA":5, "MAGICO":3, "RUSHERO":1, "HONGOS_LOCOS":1} #Nombre_tweak, cantidad de apariciones
ACCIONES_CASILLEROS:list = ["avanzas", "retrocedes"]
ACCION_AVANZAR:int = 0
ACCION_RETROCEDER:int = 1    

def crear_tablero() -> list:
    #Crea un tablero con la cantidad de filas y el numero de casilleros de cada una
    #Retorna una lista de filas de tamaño "cantidad_columnas" (lista de listas)
    ultimo_casillero_fila_anterior:int = 1 
    tablero:list = []

    for fila in range(1, CANTIDAD_FILAS_TABLERO+1):
        casilleros_fila:list = []

        for casillero in range(ultimo_casillero_fila_anterior, ultimo_casillero_fila_anterior + CANTIDAD_COLUMNAS_TABLERO):
            casilleros_fila.append(casillero)
        
        ultimo_casillero_fila_anterior = casillero + 1
        tablero.append(casilleros_fila)

    return tablero

def casillero_ocupado(casillero:int, casilleros_tweaks:list) -> bool:
    #Retorna true si el casillero ya está ocupado por alguno especial 
    retorna:bool = False 

    if (casillero in CASILLEROS_ESCALERAS_SERPIENTES.keys() or casillero in CASILLEROS_ESCALERAS_SERPIENTES or casillero in casilleros_tweaks):
        retorna = True

    return retorna 

def generar_casilleros_tweaks(maximo_casillero_tablero:int) -> dict:
    # Esta funcion es la encargada de generar todos los casilleros especiales de forma aleatoria, según la cantidad especifica de cada uno 
    # Retorna un diccionario con el numero de casillero y el código de tweak correspondiente 
    casilleros_tweaks:dict = {} #Retorno
    max_casilleros_piso:range = range(CANTIDAD_COLUMNAS_TABLERO, maximo_casillero_tablero + 1, CANTIDAD_COLUMNAS_TABLERO)
    min_casilleros_piso:range = range(1, maximo_casillero_tablero + 1, CANTIDAD_COLUMNAS_TABLERO)
    primer_casillero_piso_2:int = (2 * CANTIDAD_COLUMNAS_TABLERO + 1)

    for tweak, cantidad in TIPOS_TWEAKS.items():
        #Por cada casillero especial 
        for item in range (cantidad): 
            casillero_reestringido:bool = True
                
            while (casillero_reestringido): 
                casillero_aleatorio:int = random.randint(1, maximo_casillero_tablero) 

                if (not casillero_ocupado(casillero_aleatorio, casilleros_tweaks)):
                    #Todo va bien, porque no está sobreponiendose con ninguna existente
                    codigo_casillero:str = ""

                    if (tweak == "CASCARA_BANANA" and casillero_aleatorio > primer_casillero_piso_2):
                        #Este tweak solo se puede colocar a partir del piso 2
                        casillero_reestringido = False
                        codigo_casillero = "C"
                    elif ( tweak == "MAGICO" ):
                        casillero_reestringido = False
                        codigo_casillero = "M"
                    elif (tweak == "RUSHERO" and casillero_aleatorio not in max_casilleros_piso):
                        casillero_reestringido = False
                        codigo_casillero = "R"
                    elif( tweak == "HONGOS_LOCOS" and  casillero_aleatorio not in min_casilleros_piso):
                        casillero_reestringido = False
                        codigo_casillero = "H"

                    if (not casillero_reestringido):
                        casilleros_tweaks[casillero_aleatorio] = codigo_casillero

    return casilleros_tweaks

def obtener_casilleros_especiales(maximo_casillero_tablero:int) -> dict:
    #Esta funcion me unifica en un diccionario todos los casilleros especiales en el tablero clave:numero_casillero, valor: codigo de casillero
    #Completo primero con los tweaks 
    casilleros_especiales:dict = generar_casilleros_tweaks(maximo_casillero_tablero)

    #Ahora realizo la lógica de las escaleras/serpientes
    for casillero_inicial, casillero_final in CASILLEROS_ESCALERAS_SERPIENTES.items():
        if (casillero_inicial < casillero_final):
            #Es una escalera
            casilleros_especiales[casillero_inicial] = "E"

        elif (casillero_inicial > casillero_final):
            #Es una serpiente 
            casilleros_especiales[casillero_inicial] = "S"

    return casilleros_especiales

def imprimir_tablero(tablero:list, casilleros_especiales:dict, jugadores:list) -> None:
    #Necesito que imprima las filas al reves para cumplir con el formato
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

            #Además imprimo los jugadores que están en la casilla actualmente
            for jugador in jugadores:
                datos_jugador:dict = jugador

                for nombre, posicion in datos_jugador.items():
                    if (casillero == posicion):
                        print(f" ({nombre})", end = '')

        print("")
        print("")

def opcion_valida(opcion:str) -> bool: 
    #Retorna si la opción ingresada para el menú es válida 
    return not (opcion.isspace() or len(opcion) == 0) and (opcion.isnumeric() and int(opcion) in range(1, CANTIDAD_OPCIONES_MENU+1))

def imprimir_opciones_menu() -> None:
    #Imprime las opciones del menú 
    print("")
    print("Ingrese (1) para - INICIAR UNA NUEVA PARTIDA -")
    print("Ingrese (2) para - MOSTRAR ESTADÍSTICAS DE CASILLEROS - ")
    print("Ingrese (3) para - RESETEAR ESTADÍSTICAS DE CASILLEROS -")        
    print("Ingrese (4) para - SALIR - ")
    print("")

def menu() -> int:
    #Crea el menu y retorna la opcion escogida por el usuario
    print("")
    print("Bienvenido al entretenido y maravilloso juego de 'SERPIENTES Y ESCALERAS'. Por favor ingrese una opción para continuar: ")
    imprimir_opciones_menu()
    opcion_menu_user:str = input("")
   
    while not opcion_valida(opcion_menu_user):
        print("Por favor ingrese una opción de menú válida: ")
        imprimir_opciones_menu()
        opcion_menu_user = input("")

    return int(opcion_menu_user)

def obtener_jugadores() -> list:
    #Le pide al usuario los nombres de los jugadores
    #Devuelve la lista de jugadores ordenados por turno
    jugadores_ingresados:list = []
    jugadores:list = []
    print("Por favor, ingresa los nombres de los jugadores para sortear quién tendrá el primer turno en la partida")
    
    for item in range(CANTIDAD_JUGADORES):
        #El jugador es un diccionario con clave:nombre, valor: posicion_actual
        data_jugador:dict = {}         
        nombre_jugador:str = input(f"Ingrese el nombre del jugador {item+1}: ")
        data_jugador[nombre_jugador] = 0 #Inicializo la posicion en el tablero
        jugadores_ingresados.append(data_jugador)

    primer_jugador:int = random.randint(0, CANTIDAD_JUGADORES-1)
    
    for nombre in jugadores_ingresados[primer_jugador].keys():
        print(f"Felicidades {nombre}, jugarás de primero")

    #Primero agrego en la lista, el jugador que salió sorteado para primer turno    
    jugadores.append(jugadores_ingresados[primer_jugador])
     #Después termino de agregar el resto en el orden de ingreso       
    for jugador in jugadores_ingresados:
        if (not jugador in jugadores):
            #No esta en la lista final, lo agrego 
            jugadores.append(jugador)

    return jugadores    

def iniciar_partida(estadisticas_casilleros:dict) -> None: 
    print("")
    print(" ----- INICIANDO NUEVA PARTIDA -----")
    print("")

    hay_ganador:bool = False
    maximo_casillero_tablero = CANTIDAD_FILAS_TABLERO * CANTIDAD_COLUMNAS_TABLERO #Dimension del tablero
    tablero:list = crear_tablero()
    casilleros_especiales:dict = obtener_casilleros_especiales(maximo_casillero_tablero)
    jugadores:list = obtener_jugadores()   
    ganador_absoluto:str = ""
    #Imprimo las instrucciones y el tablero por primera vez asi los jugadores observan las casillas especiales
    imprimir_tablero(tablero, casilleros_especiales, jugadores)

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
                accion:str = ACCIONES_CASILLEROS[ACCION_AVANZAR] #default    

                while (casillero_a_mover in casilleros_especiales):
                    tipo_casillero:str = casilleros_especiales.get(casillero_a_mover)
                    nombre_casillero:str = ""
                    casillero_nuevo:int = 1 #Default
                    accion = ACCIONES_CASILLEROS[ACCION_AVANZAR] #Asi toma el default por cada casillero especial

                    if (tipo_casillero == "E" or tipo_casillero == "S"):
                        casillero_nuevo = CASILLEROS_ESCALERAS_SERPIENTES.get(casillero_a_mover, 0)
                        if (tipo_casillero == "E"):
                            nombre_casillero = "ESCALERA"
                        else:
                            nombre_casillero = "SERPIENTE"

                    elif (tipo_casillero == "C"):
                        #DEBE CAER DOS PISOS
                        nombre_casillero = "CASCARA_BANANA"
                        casillero_nuevo = casillero_a_mover - (2*CANTIDAD_COLUMNAS_TABLERO)      
                    elif (tipo_casillero == "M"):
                        #Calculo un nuevo numero de dados
                        nombre_casillero = "MAGICO"
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
                            nombre_casillero = "RUSHERO"
                            casillero_nuevo = max(tablero[numero_fila_casilla])
                        
                        if (tipo_casillero == "H"):
                        #Se mueve a la minima casilla de ese piso
                            nombre_casillero = "HONGOS_LOCOS"
                            casillero_nuevo = min(tablero[numero_fila_casilla])                                                        
                
                    if(casillero_nuevo < casillero_a_mover):
                        accion = ACCIONES_CASILLEROS[ACCION_RETROCEDER]

                    casillero_a_mover = casillero_nuevo 
                    estadisticas_casilleros[nombre_casillero] += 1
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

def imprimir_estadisticas(estadisticas_casilleros:dict) -> None:
    #Imprime las estadisticas del juego
    print("")
    print("")
    print("---- ESTADISTICAS DE LOS CASILLEROS ESPECIALES ---- ")
    for casillero_especial, estadistica in estadisticas_casilleros.items():
        print(f"{casillero_especial} : {estadistica} ")

def reiniciar_estadisticas(estadisticas_casilleros:dict):
    print("")
    print("")
    print ("  ----- RESETEANDO ESTADISTICAS ----- ")
    
    for tweak in estadisticas_casilleros.keys():
        estadisticas_casilleros[tweak] = 0 


def main() -> None: 
    opcion:int = 0
    partidas_jugadas:int = 0
    estadisticas_casilleros:dict =  {"SERPIENTE":0, "ESCALERA":0, "CASCARA_BANANA":0, "MAGICO":0, "RUSHERO":0, "HONGOS_LOCOS":0}

    while not (opcion == OPCION_SALIR_JUEGO):
        opcion = menu()

        if (opcion == OPCION_NUEVA_PARTIDA): 
            partidas_jugadas += 1
            iniciar_partida(estadisticas_casilleros) 

        elif (opcion == OPCION_MOSTRAR_ESTADISTICAS):
            if(partidas_jugadas >= 1):
                imprimir_estadisticas(estadisticas_casilleros)
            else:
              print("Todavía no se ha jugado ninguna partida. No hay estadísticas para mostrar.")

        elif (opcion == OPCION_RESET_ESTADISTICAS):
            reiniciar_estadisticas(estadisticas_casilleros)

    #Al salir del while indica que el usuario decidió salir del juego
    print(" ---- ESPERAMOS VERTE PRONTO PARA UNA NUEVA PARTIDA ----- ")
     
main()