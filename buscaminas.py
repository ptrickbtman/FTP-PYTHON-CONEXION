
#version  python:  3.8.1
# Notas
# Falta implementar la reutilizacion del metodo rellenar() en otras funciones


numero = ['1' , '2','3','4', '5','6']
fila = ['A','B','C','D','E','F']
data1 = "" #definimos la letra
data2 ="" #definimos el numero

def main():
    prepararJuego()
    bombas = prepararJuego()
    
    comenzarJuegosgame()

def prepararJuego():
    imprimirTabler(tablero)
    bombas = definirBombas()
    bombas = validarBombas2(bombas)
    while comenzarJuegosgame(bombas) == True:
        print ("")

def validarBombas2(bombas):
    if bombas[0] == bombas[2] or bombas[1] == bombas[2]:
       del bombas[2]
       #bombas.Remove(2)  
    if bombas[0] == bombas[1]:
        del bombas[1]
        print ("Se elimina la bomba2")
    return bombas

def comenzarJuegosgame(bombas):
    print ("--------------------->")
    print ("El juego ha comenzado")
    print ("--------------------->")
    game = False
    contadosDeDatosGanador = 0
    while game== False:
        print ("Ingrese Cordenada Unica (B3):")
        espacio = input().upper()
        if int(len(espacio)) == 2 : #
            if validarEspacio(espacio)== True: #validamos si el espacio esta disponible dentro del tablero
                if validarMinaConf(espacio, bombas)== False: #comparamos las minas configuradas con las nuevas, evitamos rebundancia
                    actualizarTablero(espacio, bombas)
                    contadosDeDatosGanador += 1
                    print ("Realizados: " + str(contadosDeDatosGanador))
                    if contadosDeDatosGanador == int(36 - int(len(bombas))):
                        imprimirTableroFinal(bombas)
                        print ("ganaste")
                        game = True
                        #ganar    
                else:
                    imprimirTableroFinal(bombas)
                    print ("--------")
                    print ("Has perdido")
                    return False

            else:
                print ("Datos Invalidos")
        else:
            print ("Error")

# Actualizacion del tablero aqui me quede
def actualizarTablero(espacio, bombas): #BuscarBombasCercanas
   
    if buscarLateral(espacio) == True: #Buscamos las laterales
        datoEsquina = buscarEsquina(espacio)
        if datoEsquina == True: #definimos si es esquina
            actualizarEsquina(espacio, bombas)
        else:
            actualizarLaterales(espacio, bombas) #si no es esquina
    else:
        buscarTableroNoLateral(espacio , bombas) #Si no es esquina



#comenzar a buscar
#Dividimos los datos en 2

def imprimirTableroFinal(bombas):
    for bomba in range (int(len(bombas))):
        datosBomba = obtenerDatos(bombas[bomba])
        numFila = fila.index(datosBomba[0])
        numColum = numero.index(datosBomba[1])

        tablero[numFila+1][numColum+1] = "*"
    
    imprimirTabler(tablero)

def buscarTableroNoLateral(espacio, bombas):
    datos = obtenerDatos(espacio)
    numFila = fila.index(datos[0])
    numColum = numero.index(datos[1])
    #print (numFila , numColum)
    contadorDeBombas = 0
    
    casillaIzquierda = fila[numFila]+ numero[int(numColum) -1 ] 
    casillaDerecha = fila[numFila]+ numero[int(numColum) + 1 ] 
    casillaArriba = fila[numFila - 1]+ numero[int(numColum) ] 
    casillaAbajo = fila[numFila + 1]+ numero[int(numColum) ] 
    casillaEsquinaArribaIzquierda = fila[numFila - 1]+ numero[int(numColum) - 1 ] 
    casillaEsquinaArribaDerecha = fila[numFila - 1]+ numero[int(numColum) + 1 ]
    casillaEsquinaAbajoIzquierda = fila[numFila + 1]+ numero[int(numColum) - 1 ]
    casillaEsquinaAbajoDerecha = fila[numFila + 1]+ numero[int(numColum) + 1 ] 

    #print(casillaIzquierda, casillaDerecha , casillaArriba , casillaAbajo, casillaEsquinaAbajoDerecha,casillaEsquinaAbajoIzquierda, casillaEsquinaArribaDerecha,casillaEsquinaArribaIzquierda)
    
    for bomba in range(int(len(bombas))):
        if bombas[bomba] == casillaIzquierda or bombas[bomba] == casillaDerecha or bombas[bomba] == casillaArriba or bombas[bomba] == casillaAbajo:
            contadorDeBombas +=1
        if  bombas[bomba] == casillaEsquinaAbajoDerecha or bombas[bomba] == casillaEsquinaAbajoIzquierda or bombas[bomba] == casillaEsquinaArribaDerecha or bombas[bomba] == casillaEsquinaArribaIzquierda:
            contadorDeBombas +=1
    

    #print (contadorDeBombas)
    tablero[numFila+1][numColum+1] = str(contadorDeBombas)
    imprimirTabler(tablero)





def obtenerDatos(espacio):
    count  = 0
    dato1 = ""
    dato2 = ""
    for i in espacio:
        if count == 0:
            dato1 = i
              
        if count == 1:
            dato2 = i
                
        count += 1
    return (dato1, dato2)


#BUSQUEDA DE CUADRO LATERAL + ESQUINA

def actualizarLaterales(espacio, bombas):
    espacios = obtenerDatos(espacio)
    numFila = fila.index(espacio[0])
    numColum = numero.index(espacio[1])
    contadorDeBombas = 0
   
    if str(espacios[1]) == "6" or str(espacios[1]) == "1" or str(espacios[0]) == "A" or str(espacios[0]) == "F" :
        
        if str(espacios[0]) == "F":
            # IZQUIERDA DERECHA ARRIBA ABAJO ARRIBAIZQUI ABAJOIZQUI ARRIBADERE ABAJODERE
            rellenar(espacio,bombas,"11101010")

        if str(espacios[0]) == "A":
            rellenar(espacio,bombas,"11010101")

        
        if str(espacios[1]) == "1":
            rellenar(espacio,bombas,"01110011")

        if str(espacios[1]) == "6":
            rellenar(espacios,bombas,"10111100")

            

def rellenar (espacios,bombas,direcciones):
    
    numFila = fila.index(espacios[0])
    numColum = numero.index(espacios[1])

    count = 0
    forContador = 0
    bombasT =0
    for letra in direcciones:
        # IZQUIERDA DERECHA ARRIBA ABAJO ARRIBAIZQUI ABAJOIZQUI ARRIBADERE ABAJODERE
        if forContador == 0 and letra == "1": #izquierda
            casillas = fila[numFila]+ numero[int(numColum) -1 ]
            bombasT +=obtenerBombasTotales(espacios, bombas, casillas )
            

        if forContador == 1 and letra == "1": #derecha
            casillas = fila[numFila]+ numero[int(numColum) + 1 ]
            bombasT +=obtenerBombasTotales(espacios , bombas, casillas )

        if forContador == 2 and letra == "1": #arriba
            casillas = fila[numFila - 1]+ numero[int(numColum)]
            bombasT +=obtenerBombasTotales(espacios, bombas, casillas )
            
        if forContador == 3 and letra == "1": #abajo
            casillas = fila[numFila + 1]+ numero[int(numColum) ]
            bombasT += obtenerBombasTotales(espacios, bombas, casillas )

        if forContador == 4 and letra == "1": #ARRIBAIZQUIda
            casillas = fila[numFila - 1]+ numero[int(numColum) - 1 ]
            bombasT += obtenerBombasTotales(espacios,bombas, casillas )

        if forContador == 5 and letra == "1": #abajoizQUIda
            casillas = fila[numFila + 1]+ numero[int(numColum) - 1 ]
            bombasT += obtenerBombasTotales(espacios,bombas, casillas )
        
        if forContador == 6 and letra == "1": #arribaDerecja
            casillas = fila[numFila - 1]+ numero[int(numColum) + 1 ]
            bombasT += obtenerBombasTotales(espacios,bombas, casillas )

        if forContador == 7 and letra == "1": #abajpDerecha
            casillas = fila[numFila + 1]+ numero[int(numColum) + 1 ]
            bombasT += obtenerBombasTotales(espacios,bombas, casillas)

        forContador += 1
    

    tablero[numFila+1][numColum+1] = str(bombasT)
    imprimirTabler(tablero)

def obtenerBombasTotales(espacios, bombas, casilla):

    numFila = fila.index(espacios[0])
    numColum = numero.index(espacios[1]) 
    contador = 0

    for bomba in range(int(len(bombas))):
        #print (casilla, bombas[bomba])
        #print (bomba)
        if bombas[bomba] == casilla:
            contador += 1
        else:
            contador += 0
    
    return contador
        
    
    

    
   # tablero[numFila+1][numColum+1] = str(bombasTotalesEncontradas)
   # imprimirTabler(tablero)

 
def actualizarEsquina(espacio, bombas):
    print ("actualizando EWSQUINA")
    espacios = obtenerDatos(espacio)
    #print (espacio[0])
    #print (espacio[1])
    numFila = fila.index(espacio[0])
    numColum = numero.index(espacio[1])
    contadorDeBombas = 0
    if str(espacios[1]) == "6" or str(espacios[1]) == "1":

        ###  si es la columnza izquierdaa si es la esquina derecha de las esquinas
        if espacio[1]=="1":
            if str(espacio[0]) == "A": #si es A6
                #podriamos hacer un metodo para las esquinas añadiendo funcion esquina (abajo,arriba,izqueirda, derecha, endiagonales) funciones
                casillaDerecha = fila[numFila]+ numero[int(numColum) +1 ] 
                casillaAbajo = fila[numFila + 1]+ numero[int(numColum) ] 
                casillaEsquinaAbajoDerecha = fila[numFila + 1]+ numero[int(numColum) + 1 ] 

                for bomba in range(int(len(bombas))):
                    if bombas[bomba] == casillaDerecha or bombas[bomba] == casillaAbajo or bombas[bomba] == casillaEsquinaAbajoDerecha:
                        contadorDeBombas +=1

                tablero[numFila+1][numColum+1] = str(contadorDeBombas)
                imprimirTabler(tablero)
               


            if str(espacio[0]) == "F": #si es F5

                casillaDerecha = fila[numFila]+ numero[int(numColum) + 1 ]

                casillaArriba = fila[numFila - 1]+ numero[int(numColum) ] 
                casillaEsquinaArribaDerecha = fila[numFila - 1]+ numero[int(numColum) + 1 ] 

                for bomba in range(int(len(bombas))):
                    if bombas[bomba] == casillaDerecha or bombas[bomba] == casillaArriba or bombas[bomba] == casillaEsquinaArribaDerecha:
                        contadorDeBombas +=1

                tablero[numFila+1][numColum+1] = str(contadorDeBombas)
                imprimirTabler(tablero)
            


        ###  si es la columnza derecha de las esquinas

        if espacio[1]=="6":
            if str(espacio[0]) == "A": #si es A6
                 #podriamos hacer un metodo para las esquinas añadiendo funcion esquina (abajo,arriba,izqueirda, derecha, endiagonales) funciones
                casillaIzquierda = fila[numFila]+ numero[int(numColum) -1 ] 
                casillaAbajo = fila[numFila + 1]+ numero[int(numColum) ] 
                casillaEsquinaAbajoIzquierda = fila[numFila + 1]+ numero[int(numColum) - 1 ] 

                for bomba in range(int(len(bombas))):
                    if bombas[bomba] == casillaIzquierda or bombas[bomba] == casillaAbajo or bombas[bomba] == casillaEsquinaAbajoIzquierda:
                        contadorDeBombas +=1

                tablero[numFila+1][numColum+1] = str(contadorDeBombas)
                imprimirTabler(tablero)
               


            if str(espacio[0]) == "F": #si es F5

                casillaIzquierda = fila[numFila]+ numero[int(numColum) -1 ]

                casillaArriba = fila[numFila - 1]+ numero[int(numColum) ] 
                casillaEsquinaArribaIzquierda = fila[numFila - 1]+ numero[int(numColum) - 1 ] 

                for bomba in range(int(len(bombas))):
                    if bombas[bomba] == casillaIzquierda or bombas[bomba] == casillaArriba or bombas[bomba] == casillaEsquinaArribaIzquierda:
                        contadorDeBombas +=1

                tablero[numFila+1][numColum+1] = str(contadorDeBombas)
                imprimirTabler(tablero)

        
    

def buscarEsquina (espacio):
    if espacio == "F6" or espacio== "F1" or espacio =="A1" or espacio =="A6":
        return (True)
    else:
        return (False)

    
    

def buscarLateral(espacio):
    count  = 0
    for i in espacio:
        if count == 0:
            if i == "F" or i == "A":
              
                return True
                break
            else:
               data1 = i 

        if count == 1:
            if i == "6" or i == "1":
                return True
                break
            else:
               data2 = i 
        
        count += 1

    return False

#FIN BUSQUEDA DE CUADRO LATERAL + ESQUINA

#validaciones de espacio
def validarEspacio(espacio):
    count = 0
    filaCount = 0
    numCount = 0
    for letra in espacio:
        if count == 0:
            for dato in fila:
                if dato == letra:
                    filaCount  += 1

        if count == 1:
            for dato in numero:
                if dato == letra:
                    numCount  += 1
        count +=1
    
    if validarEspacioRep(espacio)== False:
        return False
    else:
        if filaCount == 1 and numCount==1 :
            return True
        else:
            return False

    
    

#fin validacion

def validarEspacioRep(espacio):
    espacios = obtenerDatos(espacio)
    numFila = fila.index(espacio[0])
    numColum = numero.index(espacio[1])

    if tablero[numFila +1 ][numColum +1] == ".":
        return True
    else: 
        print ("Dato Repetido:" + str(espacio))
        return False

   


def validarMinaConf(espacio, bombas):
    for bomba in range(int(len(bombas))):
        if bombas[bomba] == espacio:
            return True
            break
    return False

# tablero
def crearTablero():
    
    tablero = [[0 for x in range(7)] for y in range(7)] 
    
    for filas in range (0, len(tablero)) :
        for columnas in range(0, len(tablero)):
            if (filas ==0 and columnas ==0):
                tablero[filas][columnas] = " "

            if (filas ==0 and columnas > 0):
                tablero[filas][columnas] = str(numero[columnas -1 ])

            if (columnas ==0 and filas > 0):
                tablero[filas][columnas] = str(fila[filas -1 ])

            if (filas !=0 and columnas!=0):
                tablero[filas][columnas] = "."
    return (tablero)

def imprimirTabler(tablero):
    for data in tablero:
        print (data)

# Fin Tablero

#Configuracion de bombas
def definirBombas():
    validacion = False
    while validacion!= True:
        print ("Escriba las posiciones de las 3 bombas, ejemplo: B5 D2 A5")
        bombas = input().upper()
        if (len(bombas) == 8):
            separador = " "
            maximo_numero_de_separaciones = 3
            bombasFinal = bombas.split(separador, maximo_numero_de_separaciones)
            if validarBombas(bombasFinal)== True:
                validacion = True
                return bombasFinal
            else:
                print ("Error de datos invalidos")
            
def validarBombas(bombas):
    contadorLetra = 0
    contadorNum = 0
    #print (int(len(bombas)))
    for bomba in range(int(len(bombas))):
        count = 0
        for letra in bombas[bomba]:
            if count ==0:
                for dato in fila:
                    if dato == letra:
                        contadorLetra += 1
            if count ==1:
                for dato in numero:
                    if dato == letra:
                        contadorNum += 1
            count +=1
    if contadorLetra == int(len(bombas)) and contadorNum == int(len(bombas)):
        return True
    else:
        return False




#creamos el tablero afuera para poder editarlo mas adelante
tablero = crearTablero()

#Fin Configuracion de bombas
prepararJuego();
