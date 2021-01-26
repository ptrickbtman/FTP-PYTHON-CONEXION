from itertools import cycle

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
        
if( validarRut("xx.xxx.xxx-x")):
  print("VALIDO")
