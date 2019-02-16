# Autor: Alan Giovanni Rodriguez Camacho A01748185
# Descripcion: Total a pagar de cierto numero de boletos para zonas distintas.

def numeroBoletosA(a):#Te da el costo total dependiendo del numero de boletos de etsa zona
    atotal=a*3250
    return atotal

def numeroBoletosB(b):#Te da el costo total dependiendo del numero de boletos de etsa zona
    btotal=b*1730
    return btotal

def numeroBoletosC(c):#Te da el costo total dependiendo del numero de boletos de etsa zona
    ctotal=c*850
    return ctotal

def calcularPago(a,b,c):#Calcula el precio total a pagar entre todos los boletos
    precioTotal= numeroBoletosA(a)+numeroBoletosB(b)+numeroBoletosC(c)
    return precioTotal

def main():
    a= int(input("¿Cuantos boletos quiere de la zona A?: "))
    b= int(input("¿Cuantos boletos quiere de la zona B?: "))
    c= int(input("¿Cuantos boletos quiere de la zona C?: "))
    calcularPago(a,b,c)
    precioTotal=calcularPago(a,b,c)
    print("Número de boletos en zona A: {0} ".format(a))
    print("Número de boletos en zona B: {0} ".format(b))
    print("Número de boletos en zona C: {0} ".format(c))
    print("El costo total es: $%.2f"%precioTotal)

main()


