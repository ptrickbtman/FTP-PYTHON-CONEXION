from random import randint
import random
import string

def buscarLetra(letra):
    dicc= [" ","a" , "b" , "c" , "d" ,"e" ,"f" , "g" , "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i=0
    while  dicc[i] != letra:
        i+=1     
    return encriptar(i)

def encriptar(num):
    dicc = ["h--k","k&-h","y-&r","a-&b","M--a","e&-e","d&&E","T--h","a--C","b&-a","i--b","m-&t","a&-m","o$-d", "f--a","f--b","p&-p","h&-p","r-&t","t--s","v--a","s-&d","d--v","k--t","a--c","d&-n"]
    return modelar(dicc[num])

def modelar(texto):
    texto = texto.replace("-",random.choice(string.ascii_letters))
    texto = texto.replace("&" , str(randint(0,9)) )
    return texto

def main():
    texto = "wena hermano encriptado"
    cantidad = len(texto)
    encript ="&"+str(3)
    for letra in texto:
        encript+=buscarLetra(letra)
    print()
    print("pass encriptada:", encript)
    print()
    return (encript)

def BuscarPatro(palabra):
    print (palabra)

def revolcar(palabra):
    ronda =0
    if ronda ==0:
        dos = 4
        i=1
        cinco = 5
        suma=0
        cambio=""
        for letra in palabra:  
            if i%dos ==0:
                letra = "-"
            if i==cinco+suma:
                letra = "-"
                suma+=4
            cambio+=letra
            i+=1    
        #print (cambio.split("&3")[1])
        count =1
        auxiliar=""
        des = ""
        for mm in cambio.split("&3")[1]:
            auxiliar+=mm
            if count%4 ==0:
                #print (count, auxiliar)
                des+=str(reintentar(auxiliar))
                auxiliar=""
            #print (count, auxiliar)
            count+=1
        print()
        print ("palabra desencriptada: ",des)
        print()
            
def reintentar(palabrota):
    dicc = ["h--k","k&-h" , "y-&r" , "a-&b" , "M--a" ,"e&-e","d&&E","T--h","a--C","b&-a","i--b","m-&t","a&-m","o&-d", "f--a","f--b","p&-p","h&-p","r-&t","t--s","v--a","s-&d","d--v","k--t","a--c","d&-n"]
    dicc2= [" ","a" , "b" , "c" , "d" ,"e" ,"f" , "g" , "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i=0
    for com in dicc:
        if palabrota == com.replace("&","-"):
            return dicc2[i]
        i+=1

revolcar("&3kVVte6iefwwak7ahhNNkabbCe3derI8to$odk7uhfIIafQQbhJJke1Xefzzaak0brm7tb8xap3mpvnnak9JhMMMafvvb")
#main()