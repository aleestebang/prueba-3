import math

from mechas import *
import numpy as np
listado_mechas=np.array([])


#######################################

def salir():
    print("muchas gracias por preferir a mechas locas ♥")
    return False


def grabar(listado_mechas):
    m=mechas()
    c = False
    while c == False:
        c = m.setnumero_de_atencion(input("ingrese codigo de atencion Ej.A-000"))
    c = False
    while c == False:
        c = m.setcosto(input("ingrese el costo "))
    c = False
    while c == False:
        c = m.setnombre_cliente(input("ingrese su nombre "))
    m.fecha=input("ingrese fecha")
    m.descripcion_atencion=input("ingrese la descripcion ")
    return np.append(listado_mechas,m)
def buscar():
    a=input("ingrese su codigo de atencion Ej. A-000")
    for m in listado_mechas:
        if m.setnumero_de_atencion == a:
            print(f" numero de atencion {m.setnumero_de_atencion}")
            print(f" ingrese la fecha {m.fecha}")
            print(f" ingrese su nombro {m.setnombre_cliente}")
            print(f" ingrese el costo {m.setcosto}")
            if m.costo >= 45000:
                print(" si el costo de atencion es mayor a 45000 usted recibe un masaje facial gratis mi amor ")

def imprimir_atencion(listado_mechas):
    print("1) numero de atencion ")
    print("2) costo ")
    c = False
    while c == False:
        c = m.setnumero_de_atencion (input(f"numero de atencion"))
    c = False
    while c == False:
        c= m.setcosto(input(f"ingrese costo"))
#######################################
ciclo=True
while ciclo:
    print("mechas locas")
    print("1) grabar ")
    print("2) buscar ")
    print("3) imprimir atencion ")
    print("4) salir ")
    try:
        op=int(input(print(" seleccione (1-4) ")))
        match op:
            case 1:
                print("grabar")
                listado_mechas = grabar(listado_mechas)
            case 2:
                print("buscar")
                buscar()
            case 3:
                print(" imprimir atencion ")
                imprimir_atencion(listado_mechas)
            case 4:
                print("salir")
                salir()
            case _:
                print("numero de ingresado incorrecto ")
    except BaseException as error:
        print(f"error{error}")