import os
from pathlib import Path
import math
from random import randint, uniform,random

tableroEditado =[]
numero = ['1','2','3','4','5','6','7', '8','9','10', '11','12','13' , '14','15','16', '17','18','19' , '20','21','22', '23','24','25','26']
fila =   ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def cargarMensajeInicial():
    data =""
    while (data != "1" and data != "2" and data != "3"):
        data = input("Escoge una opcion: (1) Generar Tablero | (2) Cargar tablero | (3) Salir : ")
       
    return data
    
def guardarGenerar(data):
    
    if data == "1":
        (nombre, tamaño, dificultad) = generarTablero();
        bombas = definirBombas(tamaño, dificultad)
        nuevoFileName =  modificarExtensionArchivo(nombre ,".sal")
        modificarContenido(bombas, nuevoFileName, tamaño)

    if data == "2":
        (tablero, bombas, tamaño) = cargarTablero()
        comenzarJuego(tablero, bombas, tamaño)
    if data == "3":
        exit()



####### fin inicio del programa
###### modificación de archivos
def modificarExtensionArchivo(fileName,ext):
    filename = Path(fileName)
    filename_replace_ext = filename.with_suffix('.sal')
    os.rename(fileName, filename_replace_ext)
    return filename_replace_ext

def modificarContenido(bombas, nuevoFileName , tamaño):
    archivo = open (nuevoFileName , "w")
    archivo = open (nuevoFileName , "a")
    archivo.write(str(tamaño) + os.linesep)
    for bomba in range (int(len(bombas))):
        archivo.write(bombas[bomba] + os.linesep)


###### modificación de archivos

def generarTablero():
    tamaño = 0
    dificultad = ""
    nombre = input("Ingresa nombre del archivo : ")

    if (nombre.find(".txt")== -1):
        nombre+=".txt"

    while (tamaño <= 4 or tamaño>26):
        data = input("Tamaño del tablero (entre 4 y 27) : ")
        if data.isdigit():
            tamaño = int(data);

    while dificultad!='F' and dificultad!='M' and dificultad!='D' and dificultad!='X':
        dificultad = input('Ingrese la dificultad del juego: F) Facil | M) Medio | D) Dificil | X) Maximo : ')
        if dificultad.isalpha():
            dificultad=dificultad.upper()

    crearArchivo(nombre, tamaño,dificultad)
    return (nombre,tamaño,dificultad )

  

def crearArchivo(nombre,tamaño, dificultad):
    file = open(nombre, "w")
    file. write(str(tamaño) + os.linesep)
    file. write(dificultad)
    file. close()

#################### fin de generar archivo - paso 1


def cargarTablero():
    fileName = input("Ingresa nombre del archivo : ")
    existed= False
    fileObj = Path(fileName)
    if fileObj.is_file():
        (tablero,bombas,tamaño) = crearTablero(fileName)
        return (tablero,bombas,tamaño)
    else:
        while existed!=True:
            fileName = input("Archivo no existe, intente nuevamente : ")
            fileObj = Path(fileName)
            if fileObj.is_file():
                (tablero,bombas,tamaño) = crearTablero(fileName)
                return (tablero,bombas,tamaño)


def imprimirTablero(tablero):
    for data in tablero:
        str(data)
        print (str(data))
        
        
        
                

def crearTablero(fileName):
    archivo = open(fileName, "r")
    archivo2 = open(fileName, "r")
    i = 0
    
    
    for linea in archivo.readlines():
        if i == 0:
            tamaño = int(linea)
            break
    
    
    bombas= [None] * math.ceil((tamaño* tamaño)*0.3)
    i=0
    
    for linea2 in archivo2.readlines():
        if i!=0:
            bombas[i] = str(linea2.replace("\n" , ""))

        i+=1
    bombas = [elemento for elemento in bombas if elemento != None]
    print("")
    print("--------------------------------------")
    print("Ayudantia de bombas, para comprobar:  ")
    print (bombas)
    print(" ")

    int(tamaño)
    tamaño +=1;
    tablero = [[0 for x in range(tamaño)] for y in range(tamaño)] 
    
    for filas in range (0, len(tablero)) :
        for columnas in range(0, len(tablero)):
            if (filas ==0 and columnas ==0):
                tablero[filas][columnas] = "   "

            if (filas ==0 and columnas > 0):
                tablero[filas][columnas] = " " + str(numero[columnas -1 ]) + " "

            if (columnas ==0 and filas > 0):
                tablero[filas][columnas] = " "+str(fila[filas -1 ])+ " "

            if (filas !=0 and columnas!=0 and columnas<10):
                tablero[filas][columnas] = " . "

            if (filas !=0 and columnas!=0 and columnas>=10):
                tablero[filas][columnas] = " .  "

    imprimirTablero(tablero)
    return (tablero, bombas, tamaño)




def vacio(file):
    f = open(file, "r")
    i = 0

    if os.stat(file).st_size == 0:
        print('El archivo esta vacío.')
        return False
    
    

#################### fin cargar archivo

########### Bombas
def definirBombas(tamaño,dificultad):
    cantidadMinas = 0;
    
    if dificultad== "F":
        cantidadMinas = validarCantidadBomdas(math.floor(float(int(tamaño)*int(tamaño)) * 0.1),tamaño,0.1)
    
    if dificultad== "M":
        cantidadMinas = validarCantidadBomdas(math.floor(float(int(tamaño)*int(tamaño)) * 0.15),tamaño,0.15) 
    
    if dificultad== "D":
        cantidadMinas = validarCantidadBomdas(math.floor(float(int(tamaño)*int(tamaño)) * 0.2),tamaño,0.2) 
    
    if dificultad== "X":
        cantidadMinas = validarCantidadBomdas(math.floor(float(int(tamaño)*int(tamaño)) * 0.3),tamaño,0.3) 
    
    print("Cantidad de minas: ",cantidadMinas)
    print("creando minas aleatorias: ")
    return (definirMinas(cantidadMinas, tamaño))


def validarCantidadBomdas(cantidadMinas, tamaño, dificultad):
    
    if (cantidadMinas <1):
        print("hay 0 minas, por ende le asignaremos una")
        return (1)

    return (int(cantidadMinas))


def definirMinas(cantidadMinas, tamaño):
    minas = [None]* int(cantidadMinas) 
    minasCrear = ""
    #print (int(tamaño))
    for i in range (int(cantidadMinas)):
        if i == 0:
            minasCrear = str(fila[randint(1,int(tamaño)-1)])
            minasCrear += str((randint(1,int(tamaño)-1)))
            minas[i] = minasCrear
        else:
            validar = False
            while validar!= True :
                minasCrear = str(fila[randint(1,int(tamaño)-1)])
                minasCrear += str((randint(1,int(tamaño)-1)))
                if validarMinasRepetidas(minas, minasCrear):
                    minas[i] = minasCrear
                    validar = True

    #print (minas)
    return (minas)
        
def validarMinasRepetidas(minas, minaUnica):
    for bomba in range(int(len(minas))):
        if (minas[bomba]!=None):
            #print(minas[bomba], " == ", minaUnica)
            if minas[bomba] == minaUnica:
                #print("repetida")
                return False
    #print("paso mina : " ,minaUnica )
    return True


####### fin minas repetidas

#############################comienzo del juego

def comenzarJuego(tablero, bombas, tamaño):
    print ("")
    print ("El juego ha comenzado!")
    print("-----------------------")
    print("cantidad de bombas: ", str(len(bombas)))

    finalGame= False
    
    aciertos = 0 # cantidad de aciertos para ganar = ((int(tamaño)-1)* (int(tamaño)-1) - int(len(bombas)))
    

    while finalGame!= True:
        espacioJugado = input("Selecciona el espacio: " ).capitalize()
        if int(len(espacioJugado))==2 or int(len(espacioJugado))==3:
            if validarEspacioConTablero(str(espacioJugado), tamaño):
                #print("espacio disponible")
                if validarEspacioBomba(bombas,espacioJugado)!= True:
                    if (validarLaterales(espacioJugado,tamaño)!=True):
                        data = "12345678"
                        buscarMinasGeneral (bombas, espacioJugado,tablero, data)
                        aciertos +=1
                        print(aciertos, "de" , ((int(tamaño)-1)* (int(tamaño)-1) - int(len(bombas))))
                        if aciertos ==((int(tamaño)-1)* (int(tamaño)-1) - int(len(bombas))):
                            imprimirTableroFinal(bombas, tablero)
                            print("----------------------------")
                            print("has ganado! felicitaciones :)")
                            print("----------------------------")
                            finalGame= True
                    else:
                        if validarEsquina(espacioJugado,tamaño)!= True:
                            tipoLate = definirLaterales(espacioJugado,tamaño)
                            if tipoLate == "ar":
                                data = "12478"
                                buscarMinasGeneral (bombas, espacioJugado,tablero, data)
                            if tipoLate == "iz":
                                data = "23468"
                                buscarMinasGeneral (bombas, espacioJugado,tablero, data)
                            if tipoLate == "ab":
                                data = "12356"
                                buscarMinasGeneral (bombas, espacioJugado,tablero, data)
                            if  tipoLate == "de":
                                data = "13457"
                                buscarMinasGeneral (bombas, espacioJugado,tablero, data)


                            aciertos +=1
                            print(aciertos, "de" , ((int(tamaño)-1)* (int(tamaño)-1) - int(len(bombas))))
                            if aciertos ==((int(tamaño)-1)* (int(tamaño)-1) - int(len(bombas))):
                                imprimirTableroFinal(bombas, tablero)
                                print("----------------------------")
                                print("has ganado! felicitaciones :)")
                                print("----------------------------")
                                finalGame= True

                            
                        else:
                            esquina = saberEsquina(espacioJugado,tamaño)
                            if esquina == "arIz":
                                data = "248"
                                buscarMinasGeneral (bombas, espacioJugado,tablero, data)
                            if esquina == "arDe":
                                data = "147"
                                buscarMinasGeneral (bombas, espacioJugado,tablero, data)
                            if esquina == "abIz":
                                data = "236"
                                buscarMinasGeneral (bombas, espacioJugado,tablero, data)
                            if esquina == "abDe":
                                data = "135"
                                buscarMinasGeneral (bombas, espacioJugado,tablero, data)

                            aciertos +=1
                            print(aciertos, "de" , ((int(tamaño)-1)* (int(tamaño)-1) - int(len(bombas))))
                            if aciertos ==((int(tamaño)-1)* (int(tamaño)-1) - int(len(bombas))):
                                imprimirTableroFinal(bombas, tablero)
                                print("----------------------------")
                                print("has ganado! felicitaciones :)")
                                print("----------------------------")
                                finalGame= True
                else:
                    print("has perdidooo ); ")
                    imprimirTableroFinal(bombas, tablero)
                    return False
            else:
                print("texto invalido")
  
        else:
            print ("Error de formato")




def saberEsquina(espacioJugado,tamaño):
    (filaLetra, numColum) = espacioSeparado(espacioJugado)
    if filaLetra == "A":
        if int(numColum) == 1:
            return "arIz" 
        else:
             return "arDe"
    
    if filaLetra == fila[int(tamaño)-2]:
        if int(numColum) == 1:
            return "abIz" 
        else:
             return "abDe"

def definirLaterales(espacioJugado,tamaño):
    (filaLetra, numColum) = espacioSeparado(espacioJugado)
    
    if filaLetra == "A":
        return "ar"
    if int(numColum) == 1:
        return "iz"
    if int(numColum) == int(tamaño)-1:
        return "de"
    if filaLetra == fila[int(tamaño)-2]:
        return "ab"

    #print(filaLetra,numColum)

def imprimirTableroFinal(bombas, tablero):
    for bomba in range (int(len(bombas))):
        datosBomba = espacioSeparado(bombas[bomba])
        numFila = fila.index(datosBomba[0])
        numColum = numero.index(datosBomba[1])
        if int(numColum) >=9:
            tablero[int(numFila)+1][int(numColum)+1] = " "+"*"+"  "
        else:
            tablero[int(numFila)+1][int(numColum)+1] = " "+"*"+ " "
        
        tableroEditado = tablero

    imprimirTablero( tableroEditado )


def buscarMinasGeneral(bombas, espacio , tablero, data):
    casillas = [None]* 8
    cantidadCasillas = 0
    minasEncontradas= 0

    datos = espacioSeparado(espacio)
    numFila = fila.index(datos[0])
    numColum = numero.index(datos[1])

    for letra in data:
        if letra.upper() == "1":
            casillas[cantidadCasillas] = fila[numFila]+ numero[int(numColum) -1 ]  #izquirda
            cantidadCasillas+=1
        if letra.upper() == "2":
            casillas[cantidadCasillas] = fila[numFila]+ numero[int(numColum) + 1 ] #derecha
            cantidadCasillas+=1
        if letra.upper() == "3":
            casillas[cantidadCasillas] = fila[numFila - 1]+ numero[int(numColum) ] #arriba
            cantidadCasillas+=1
        if letra.upper() == "4":
            casillas[cantidadCasillas] = fila[numFila + 1]+ numero[int(numColum) ] #abajo
            cantidadCasillas+=1
        if letra.upper() == "5":
            casillas[cantidadCasillas] = fila[numFila - 1]+ numero[int(numColum) - 1 ] #arriba iz
            cantidadCasillas+=1
        if letra.upper() == "6":
            casillas[cantidadCasillas] = fila[numFila - 1]+ numero[int(numColum) + 1 ]   #arriba derecha
            cantidadCasillas+=1   
        if letra.upper() == "7":
            casillas[cantidadCasillas] = fila[numFila + 1]+ numero[int(numColum) - 1 ]#abajo izquierda
            cantidadCasillas+=1
        if letra.upper() == "8":
            casillas[cantidadCasillas] = fila[numFila + 1]+ numero[int(numColum) + 1 ] #abajo derecha izquierda
            cantidadCasillas+=1
    bombas = [elemento for elemento in bombas if elemento != None]
    for bomba in range(int(len(bombas))):
        for casilla in range(int(len(casillas))):
            if str(bombas[bomba]) == str(casillas[casilla]):
                minasEncontradas +=1
    

    numFila = fila.index(datos[0])
    numColum = numero.index(datos[1])
    if int(numColum) >=9:
        tablero[int(numFila)+1][int(numColum)+1] = " "+str(minasEncontradas)+ "  "
    else:
        tablero[int(numFila)+1][int(numColum)+1] = " "+str(minasEncontradas)+ " "
    tableroEditado =tablero
    imprimirTablero(tablero)
    #imprimirTablero(tableroEditado)
     

#### encontrar Esquinas

def validarEsquina(espacioJugado,tamaño):
    print(espacioJugado)
    (filaEspacio, columnaEspacio) = espacioSeparado(espacioJugado)
    ultimaFila= int(tamaño)-2
    ultimaData1 = "A"+ str(int(tamaño)-1)
    ultimaData2=  str(fila[ultimaFila]) +"1"
    ultimaData3 = str(fila[ultimaFila]) + str(tamaño-1)
    if (espacioJugado== "A1" or espacioJugado == ultimaData1 or espacioJugado == ultimaData2 or espacioJugado == ultimaData3):
        return True
    return False



#### encontrarLateral o no lateral

def validarLaterales(cadena, tamaño):
    (filaEspacio, columnaEspacio) = espacioSeparado(cadena)
    ultimaFila= int(tamaño)-2
    #print(ultimaFila)
    if int(columnaEspacio)==1 or int(columnaEspacio) == int(tamaño)-1 or fila[ultimaFila] == filaEspacio or filaEspacio == "A":
        return True
    return False

### validamos el espacio si se encuentra en el tablero 
def validarEspacioConTablero(cadena , tamaño):
    (letra1, numeroColum) = espacioSeparado(cadena)
    i = 0
    for letras in range(int(tamaño)-1):  
        #print(fila[letras].capitalize() , "==", letra1.capitalize() ) 
        if (fila[letras].capitalize() == letra1.capitalize() ):
            if int(numeroColum)>0 and int(numeroColum)<=int(tamaño-1):
                return True            
    return False


def espacioSeparado(data):
    i=0
    filaEspacio= ""
    numeroColum = ""

    for letra in data:
        if i ==0:
            filaEspacio = letra

        if i!=0:
            numeroColum+=letra
        i+=1

    return (filaEspacio, numeroColum)



def validarEspacioBomba(bombas,espacioJugado):
    for bomba in range(int(len(bombas))):
        if bombas[bomba] == espacioJugado:
            return True

    return False
############################## Fin termino de juego

def main():
    game = True
    while game:
        guardarGenerar(cargarMensajeInicial())


    
main();

    

