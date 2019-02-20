#Luis Fernando Duran Castillo
#Ayudar a una perswona con el rendimiento de su auto

def calcularrendimientonormal(kilometros,litros):
    propporcion= kilometros /litros
    return propporcion

def calcularotrorendimiento (kilometros,litros):
    galon= litros*.264
    millas= kilometros/1.6903
    proporcion1= millas/ galon
    return proporcion1

def calcularrecorrido (kilometros,litros,nuevo):
    recorrido= nuevo / calcularrendimientonormal(kilometros,litros)
    return recorrido

def main():
    kilometros= int(input("cuantos kilometros ha recorrito? "))
    litros= int(input("cuantos litros ha gastado? "))
    calcularrendimientonormal(kilometros, litros)
    calcularotrorendimiento(kilometros, litros)
    print("si recorre ", kilometros," kilometros con", litros, " litros su rendimiento fue de:  %.2f " % calcularrendimientonormal(kilometros, litros),"km/l %.2f " % calcularotrorendimiento(kilometros, litros), "mi/gal" )
    nuevo= int(input("cuantos kilometros va a recorer ? "))
    print("para recorrer", nuevo, "se necesitarian %.2f " % calcularrecorrido (kilometros,litros,nuevo), " litros" )

main()