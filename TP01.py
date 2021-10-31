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
ACCIONES_CASILLEROS:list = ["avanzas", "retrocedes"]
ACCION_AVANZAR:int = 0
ACCION_RETROCEDER:int = 1

#Constantes casilleros especiales 
TIPOS_TWEAKS:dict = {"CASCARA_BANANA":5, "MAGICO":3, "RUSHERO":1, "HONGOS_LOCOS":1} #Nombre_tweak, cantidad de apariciones
CASCARA_BANANA:str = "CASCARA_BANANA"
MAGICO:str = "MAGICO"
RUSHERO:str = "RUSHERO"
HONGOS_LOCOS:str = "HONGOS_LOCOS"
ESCALERA:str = "ESCALERA"
SERPIENTE:str = "SERPIENTE"


def crear_tablero() -> list:
    """ 
    Crea un tablero de juego con la cantidad de filas y el numero de casilleros (columnas) en cada una

    Parametros
    ----------
    None:    
        En este caso el programa tiene un tamaño definido 
        de filas y columnas para el tablero de juego, por lo tanto utiliza las 
        constantes creadas. (CANTIDAD_FILAS_TABLERO, CANTIDAD_COLUMNAS_TABLERO)

    Retorno
    -------
        tablero: list 
            El tablero con la cantidad de filas definida y los casilleros que pertenecen 
            a cada una de las filas (ordenados) de menor a mayor. 
    """

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
    """ 
    Verifica si el número de casillero ya está siendo ocupado 
    por una casilla especial (escaleras(inicio-fin), serpientes(inicio-fin) o tweaks), 
    ya que en el juego no se pueden sobreponer casilleros especiales. 

    Parametros
    ----------
    casillero: entero positivo 
        Corresponde al casillero que se desea utilizar 
    
    casilleros_tweaks: lista 
        Es la lista de casilleros especiales de tipo tweaks que están actualmente 
        generados en el tablero 

    Retorno
    -------
        casillero_ocupado: bool  
            Retorna true si el numero de casillero ingresado ya está siendo utilizado 
            por un casillero especial, tanto de inicio/fin en las escaleras y 
            serpientes o de algún tweak. Y False si puede ser utilizado libremente 
    """
    casillero_ocupado:bool = False 

    if (casillero in CASILLEROS_ESCALERAS_SERPIENTES.keys() or casillero in CASILLEROS_ESCALERAS_SERPIENTES.values() or casillero in casilleros_tweaks):
        retorna = True

    return casillero_ocupado 

def generar_casilleros_tweaks(maximo_casillero_tablero:int) -> dict:
    """ 
    Se encarga de generar todos los casilleros de tipo tweaks (modificaciones)
    que pueden existir en el juego según las especificaciones y reestricciones establecidas
    para cada uno. Los casilleros tweaks son generados al azar 
    y no pueden sobreponerse con las escaleras o serpientes (tanto inicion como fin
    de las mismas) o entre sí 

    Parametros
    ----------
    maximo_casillero_tablero: entero positivo 
        Corresponde al último casillero del tablero (máxima posición), que también
        puede conocerse como "dimensión del tablero" (filas x columnas)
    
    Retorno
    -------
        casilleros_tweaks: dict
        Retorna un diccionario que contiene el número de casillero (posicion en el tablero)
        y el nombre de tweak que corresponde
        Clave: número_casillero
        Valor: nombre del tweak
   """

    casilleros_tweaks:dict = {} #Retorno
    max_casilleros_piso:range = range(CANTIDAD_COLUMNAS_TABLERO, maximo_casillero_tablero + 1, CANTIDAD_COLUMNAS_TABLERO)
    min_casilleros_piso:range = range(1, maximo_casillero_tablero + 1, CANTIDAD_COLUMNAS_TABLERO)
    primer_casillero_piso_2:int = (2 * CANTIDAD_COLUMNAS_TABLERO + 1)

    for tweak, cantidad_apariciones in TIPOS_TWEAKS.items():
        #Por cada casillero especial 
        for item in range (cantidad_apariciones): 
            casillero_reestringido:bool = True
                
            while (casillero_reestringido): 
                casillero_aleatorio:int = random.randint(1, maximo_casillero_tablero) 

                if (not casillero_ocupado(casillero_aleatorio, casilleros_tweaks)):
                    #Todo va bien, porque no está sobreponiendose con ninguna existente
                    if (tweak == CASCARA_BANANA and casillero_aleatorio > primer_casillero_piso_2):
                        #Este tweak solo se puede colocar a partir del piso 2
                        casillero_reestringido = False
                    elif ( tweak == MAGICO ):
                        #Este tipo de tweak no tiene reestricciones
                        casillero_reestringido = False
                    elif (tweak == RUSHERO and casillero_aleatorio not in max_casilleros_piso):
                        #Este tweak no puede colocarse en los maximos casilleros de cada piso
                        casillero_reestringido = False
                    elif( tweak == HONGOS_LOCOS and  casillero_aleatorio not in min_casilleros_piso):
                        #Este tweak no puede colocarse en los minimos casilleros de cada piso
                        casillero_reestringido = False

                    if (not casillero_reestringido):
                        casilleros_tweaks[casillero_aleatorio] = tweak #El nombre del casillero especial

    return casilleros_tweaks


def obtener_casilleros_especiales(maximo_casillero_tablero:int) -> dict:
    """ 
    Se encarga de unificar todos los casilleros especiales del tablero para 
    tenerlos en un único lugar y acceder de forma más simple. Los casilleros 
    especiales corresponden a "Escaleras, Serpientes, y tweaks (ver constante: TIPOS TWEAKS)"

    Parametros
    ----------
    maximo_casillero_tablero: entero positivo 
        Corresponde al último casillero del tablero (máxima posición), que también
        puede conocerse como "dimensión del tablero" (filas x columnas)
    
    Retorno
    -------
        casilleros_especiales: dict
        Retorna un diccionario que contiene el número de casillero (posicion en el tablero)
        y el nombre del casillero especial que corresponde
        Clave: número del casillero
        Valor: nombre del casillero especial
   """

    #Completo primero con los tweaks 
    casilleros_especiales:dict = generar_casilleros_tweaks(maximo_casillero_tablero)

    #Ahora realizo la lógica de las escaleras/serpientes dadas
    for casillero_inicial, casillero_final in CASILLEROS_ESCALERAS_SERPIENTES.items():
        if (casillero_inicial < casillero_final):
            #Es una escalera
            casilleros_especiales[casillero_inicial] = ESCALERA

        elif (casillero_inicial > casillero_final):
            #Es una serpiente 
            casilleros_especiales[casillero_inicial] = SERPIENTE

    return casilleros_especiales

def imprimir_tablero(tablero:list, casilleros_especiales:dict, jugadores:list) -> None:
    """ 
    Imprime el tablero de juego con el siguiente criterio: las
    filas pares se imprimen de menor a mayor para cumplir con el formato
    deseado. Además, coloca el código y número que ocupan los casilleros especiales 
    y la posición actual que ocupa cada uno de los jugadores.

    Parametros
    ----------
    tablero: list
         El tablero con la cantidad de filas definida y los casilleros que pertenecen 
        a cada una de las filas (ordenados) de menor a mayor. 
    casilleros_especiales: dict 
        El diccionario que contiene todos los casilleros especiales y el nombre 
        correspondiente a cada uno. Para imprimirlo, esta funcion toma sólo 
        la primera letra del nombre del casillero especial.  
    jugadores: list
        Es la lista de jugadores de la partida, que contiene un diccionario 
        con el nombre de cada uno y la posición actual en el tablero 
    
    Retorno
    -------
    None:
        Esta función no retorna nada porque sólo se encarga de imprimir por consola
        el tablero con los casilleros y la posicion actual de los jugadores 
   """
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
                print(f"| {casillero} ({tipoCasillero[0:1]}) ", end=' ')
            else:    
                print(f"| {casillero}", end=' ')

            #Además imprimo los jugadores que están en la casilla actualmente
            for jugador in jugadores:
                datos_jugador:dict = jugador

                for nombre, posicion in datos_jugador.items():
                    if (casillero == posicion):
                        print(f" [{nombre}]", end = '')

        print("")
        print("")

def imprimir_opciones_menu() -> None:
    """ 
    Imprime por consola las opciones del menú principal para que el usuario
    pueda escoger alguna
    """

    print("")
    print("Ingrese (1) para - INICIAR UNA NUEVA PARTIDA -")
    print("Ingrese (2) para - MOSTRAR ESTADÍSTICAS DE CASILLEROS - ")
    print("Ingrese (3) para - RESETEAR ESTADÍSTICAS DE CASILLEROS -")        
    print("Ingrese (4) para - SALIR - ")
    print("")

def opcion_valida(opcion:str) -> bool: 
    """ 
    Valida si el ingreso del usuario por comando es válido como 
    una opción de menú. La opción debe ser alguna de las 4 especificadas, 
    no debe contener caracteres, espacios o ser vacío. 

    Parametros
    ----------
    opcion: str
        La opción que ingresó el usuario    
    Retorno
    -------
    bool:
        Retorna si corresponde a una opción valida del menú mostrado 
   """

    return not (opcion.isspace() or len(opcion) == 0) and (opcion.isnumeric() and int(opcion) in range(1, CANTIDAD_OPCIONES_MENU+1))

def menu() -> int:
    """ 
    Imprime el menú con la bienvenida al juego y todas las opciones 
    que puede escoger el usuario. Le permite al usuario ingresar una 
    y valida que la misma sea correcta y corresponda a alguna de las mostradas.

    Retorno
    -------
    int:
        La opción del usuario ya validada
   """

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
    """ 
    Obtiene el listado de jugadores que van a participar en la partida. Le solicita
    al usuario el nombre de cada uno, y obtiene de forma aleatoria el primero en jugar. 

    Retorno
    -------
    jugadores: list[dict]
        Retorna una lista de jugadores que contiene un diccionario con el nombre del jugador 
        y la posición actual del tablero. Como esta función inicializa los mismos, su posicion
        actual será 0. La lista se retorna ordenada por turno, siendo el primero, el sorteado de 
        forma aleatoria. 
   """
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
    """ 
    Inicia la partida y realiza la lógica del avance o retroceso de los jugadores 
    según los casilleros especiales, imprimiendo en cada paso el tablero para que el
    usuario pueda observar lo que está sucediendo. Tambien se encarga de completar las 
    estadísticas aumentando los contadores por cada casillero especial cuando un jugador 
    cae en una de ellas. 
   
    Parametros
    ----------
    estadisticas_casilleros: dict
    Recibe el diccionario de estadísticas de casilleros especiales que contiene el nombre 
    del casillero especial y el contador de las veces que un jugador cae en el mismo, 
    así las puede ir modificando de manera dinámica.  

    Retorno
    -------
    None: 
        La función por sí sola se encarga de mostrar y ejemplificar los pasos de cada jugador
        imprimiendo toda la información por pantalla.  
   """

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
                #No necesito que lo haga si ya el jugador anterior ganó
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
                    casillero_nuevo:int = 1 #Default
                    accion = ACCIONES_CASILLEROS[ACCION_AVANZAR] #Asi toma el default por cada casillero especial

                    if (tipo_casillero == ESCALERA or tipo_casillero == SERPIENTE):
                        casillero_nuevo = CASILLEROS_ESCALERAS_SERPIENTES.get(casillero_a_mover, 0)
                        
                    elif (tipo_casillero == CASCARA_BANANA):
                        #DEBE CAER DOS PISOS
                       casillero_nuevo = casillero_a_mover - (2*CANTIDAD_COLUMNAS_TABLERO)

                    elif (tipo_casillero == MAGICO):
                        #Calculo una nueva posicion aleatoria
                        #No puede caer en el minimo, maximo ni en el mismo porque genero un bucle
                        casilleros_reestringidos_magico:list = [1, maximo_casillero_tablero, casillero_a_mover]
                        while (casillero_nuevo in casilleros_reestringidos_magico):
                            casillero_nuevo = random.randint(1, 6)
                
                    elif (tipo_casillero == RUSHERO or tipo_casillero == HONGOS_LOCOS):
                        numero_fila_casilla:int  = 0

                        for fila in range(len(tablero)):
                            casilleros_fila:list = tablero[fila]
                            for casilla in casilleros_fila:
                                if (casillero_a_mover == casilla):
                                    numero_fila_casilla = fila

                        if (tipo_casillero == RUSHERO):
                        #Se mueve hasta la maxima casilla de ese piso
                           casillero_nuevo = max(tablero[numero_fila_casilla])
                        
                        if (tipo_casillero == HONGOS_LOCOS):
                        #Se mueve a la minima casilla de ese piso
                            casillero_nuevo = min(tablero[numero_fila_casilla])                                                        
                
                    if(casillero_nuevo < casillero_a_mover):
                        accion = ACCIONES_CASILLEROS[ACCION_RETROCEDER]

                    casillero_a_mover = casillero_nuevo 
                    estadisticas_casilleros[tipo_casillero] += 1
                    print(f"{nombre_jugador} caíste en casillero '{tipo_casillero}', así que {accion} hasta el casillero: {casillero_a_mover}")
                    
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
    """ 
    Imprime las estadísticas de los casilleros especiales. 

    Parametros
    ----------
    estadisticas_casilleros: dict
    Recibe el diccionario de estadísticas de casilleros especiales que contiene el nombre 
    del casillero especial y el contador de las veces que un jugador cae en el mismo.

    Retorno
    -------
    None: 
        La función imprime por pantalla las estadísticas de los casilleros especiales. 
   """

    print("")
    print("")
    print("---- ESTADISTICAS DE LOS CASILLEROS ESPECIALES ---- ")
    for casillero_especial, estadistica in estadisticas_casilleros.items():
        print(f"{casillero_especial} : {estadistica} ")

def reiniciar_estadisticas(estadisticas_casilleros:dict):
    """ 
    Reinicia la estadísticas del juego. Todos los casilleros 
    especiales pasan a estar en 0, es decir, nunca utilizados.

    Parametros
    ----------
    estadisticas_casilleros: dict
    Recibe el diccionario de estadísticas de casilleros especiales que contiene el nombre 
    del casillero especial y el contador de las veces que un jugador cae en el mismo.

    Retorno
    -------
    None: 
        La función sólo se encarga de setear en 0 el diccionario pasado por parámetro
   """

    print("")
    print("")
    print ("  ----- RESETEANDO ESTADISTICAS ----- ")
    
    for tweak in estadisticas_casilleros.keys():
        estadisticas_casilleros[tweak] = 0 
    
    print(" ----- ESTADISTICAS REINICIADAS CON ÉXITO ----- ")


def main() -> None:
    opcion:int = 0
    partidas_jugadas:int = 0
    estadisticas_casilleros:dict =  {SERPIENTE:0, ESCALERA:0, CASCARA_BANANA:0, MAGICO:0, RUSHERO:0, HONGOS_LOCOS:0}

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