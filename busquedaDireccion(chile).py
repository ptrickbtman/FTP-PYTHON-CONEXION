import sys
import requests
from bs4 import BeautifulSoup
from itertools import cycle


# valdiador de rut
def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11



def validarRut(rut):
    rut = rut.replace(".", "")
    rut = rut.split("-")
    #print(digito_verificador(rut[0]) , rut[1] )
    if (str(digito_verificador(rut[0]))== rut[1]):
        return True;
    if (rut[1].title() == "K" and digito_verificador(rut[0])== 10 ):
        return True;


# fin de validar rut
# webscraping

def peticionHttpRut(rut):
    payload = {'term': rut}
    r = requests.post("https://www.nombrerutyfirma.com/rut", data=payload)

    soup = BeautifulSoup(r.text, "lxml")
    #print(soup)
    for sub_heading in soup.find_all('td'):
        print(sub_heading.text)



def searchRut():
    if(validarRut(sys.argv[2])):
        peticionHttpRut(sys.argv[2])
    else: 
        print ("EL RUT NO ES VALIDO UWU")

def peticionHttpNa(data):
    payload = {'term': data}
    r = requests.post("https://www.nombrerutyfirma.com/buscar", data=payload)

    soup = BeautifulSoup(r.text, "lxml")
    count = 0;
    #print(soup)
    for sub_heading in soup.find_all('td'):
        if (count%5==0):
            print("----------------")
        print(sub_heading.text)
        count +=1

def searchNa():
    data = ""
    for i in range (2,len(sys.argv)):
        data += sys.argv[i] + " "
    if(data!=""):
        peticionHttpNa(data)
        

def main():
    if(len(sys.argv)>1):
        if ( sys.argv[1] == "-RUT" ):
            searchRut()
        if ( sys.argv[1] == "-NA" ):
            searchNa()
    else:
        print("Ejecución ejemplo")
        print("Rut: python3 archive.py -RUT xx.xxx.xxx-1 ")
        print("Nombre: python3 archive.py -NA NOM1 NOM2 APE1 APE2")
        print ("PARA BUSQUEDA DE NOMBRE ES OBLIGATORIO EL NOM1")
    
    

if __name__ == "__main__":
    main()
