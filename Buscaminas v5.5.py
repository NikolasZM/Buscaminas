import random
def generar_campoNum():         #Generamos un campo con 0's
    campo1=[0,0,0,0,0,0,0,0,0,0]
    campo=[]
    for i in range(len(campo1)):
        x=campo1.copy()
        campo.append(x)
    return campo            #regresamos la lista con las 10 sublistas, cada una con el número 0 repetido 10 veces.

def genera_minas(): 
    i=0
    minas=[]
    while i<10:
        _1=random.randint(0,9)  #Generamos dos números aleatorios para crear una mina
        _2=random.randint(0,9)
        if [_1,_2]not in minas:     #si la mina no existe se agrega a la lista, pero si ya existe, se genera otra
            minas.append([_1,_2])
            i+=1
        else:
            continue
    return minas  

def modificar_campo(campo,minas):   #Creamos una funcion que meta las minas dentro del tablero
    for i in range(10):
        x=minas[i][0]
        y=minas[i][1]
        campo[x][y]="X"
    return campo

def casillas_lateral(casilla):      #creamos una función auxiliar
    laterales=[]            #Al ingresar una casilla, la funcíon devolverá las casillas que esten alrededor
    for i in range(-1,2):               
        x=[casilla[0]-1,casilla[1]+i]
        laterales.append(x)
    x=[casilla[0],casilla[1]+1]
    laterales.append(x)
    for i in range(2):
        x=[casilla[0]+i,casilla[1]-1]
        laterales.append(x)
        x=[casilla[0]+1,casilla[1]+i]
        laterales.append(x)     
    borrar=[]
    for i in range(len(laterales)):
        if laterales[i][1]<0 or laterales[i][0]<0:      #Si la casilla da un número negativo o 10, se borra de la lista
            borrar.append(laterales[i])
        if laterales[i][1]==10 or laterales[i][0]==10:
            borrar.append(laterales[i])
    for i in borrar:
        if i in laterales:
            laterales.remove(i)
    return laterales         
      
def numeros(tablero,minas):     #Esta funcion identifica si una casilla tiene una mina y suma 1 a su valor
    for x in minas:
        lados=casillas_lateral(x)
        for x in range(len(lados)):
            try:
                tablero[lados[x][0]][lados[x][1]]+=1        
            except:
                pass
    return tablero             

def imprimir_campo(campo):      #La funcion se encarga de imprimir los números y el tablero para jugar
    n=range(0,10)
    print("  | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |  ".format(*n))
    print("-"*45)
    for i in range(len(campo)):
        print(n[i],"|"," | ".join([str(p) for p in campo[i]]),"|")#Aqui convertimos todos los miembros de campo en strings, despues las separamos con .join para imprimirlas.
    print("-"*45)

def generar_campoVacío():       #generamos un campo vacío para mostrar al jugador
    campo1=[" "," "," "," "," "," "," "," "," "," ",]
    campo=[]
    for i in range(len(campo1)):
        x=campo1.copy()
        campo.append(x)
    return campo

def disponibles(tablero):       #Generamos una función que se encarga de analizar las casillas que fueron minadas.
    disponibles=[]
    for i in tablero:
        for x in i:
            disponibles.append(x)
    disponibles1=[]
    for x in disponibles:
        if type(x)==int:
            disponibles1.append(x)
    if len(disponibles1)==90:       #Si las casillas minadas son 90(100 casillas en total menos las 10 minas), el juego terminará
        return True
    return False

def jugar():        #Creamos la funcion que realice el juego
    x=genera_minas()
    y=numeros(modificar_campo(generar_campoNum(),x),x)
    y1=generar_campoVacío()        #Creamos dos campus, uno con numeros y minas y otro vacío, cuando el jugador mine una casilla, la reemplazará con su valor
    while True:
        if disponibles(y1)==True:       #Comrobamos la cantidad de casillas minadas
            print("-"*45)
            print("Felicidades!! Ganaste el juego.")
            print("-"*45)
            imprimir_campo(y)
            print("-"*45)
            break
        imprimir_campo(y1)
        cc1=input("Escoge las coordenadas de la casilla que quieres minar (Ejemplo: 5 5): ")    #Pedimos al jugador ingresar la casilla que desea minar
        try:
            cc2=cc1.split(" ")      
            cc=[int(cc2[0]),int(cc2[1])]
        except:
            print("-"*45)
            print("Ingrese una casilla valida.")
            print("-"*45)
            continue
        if cc[0]>9 or cc[1]>9:
            print("-"*45)
            print("Escoge valores aceptables.")
            print("-"*45)
            continue
        if y[cc[0]][cc[1]]=="X":        #Si la casilla es una mina, el juego termina y el jugador pierde.
            imprimir_campo(y)
            print("-"*45)
            print("Ups, minaste una mina. El juego termino.!!!!!")
            print("-"*45)
            break
        if y[cc[0]][cc[1]]>0:           #Si la casilla es un numero diferente de 0, la casilla se reemplaza por su valor
            y1[cc[0]][cc[1]]=y[cc[0]][cc[1]]
        if y[cc[0]][cc[1]]==0:      #Si la casilla es 0, la casilla y todas a su alrededor se reemplazan por su valor
            y1[cc[0]][cc[1]]=0
            x=casillas_lateral(cc)
            for i in x:
                if y[i[0]][i[1]]!="X":
                    y1[i[0]][i[1]]=y[i[0]][i[1]]

jugar()