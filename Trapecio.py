#Autor Sofía Trujillo Vargas
#Escribir un programa que saque el área y el perimetro de un trapecio

import math

def ArTrap(baseMen,baseMay,altura):
    pp =((baseMay*baseMen)/2)*altura
    return pp

def PerTrap(baseMen,baseMay,altura):
    pe=baseMay-baseMen
    po=pe/2
    pu=math.sqrt((altura**2)+(po**2))
    pl=baseMay+baseMen+(2*pu)
    return pl

def main():
    x=float(input("Dame la Base Mayor de tu trapecio: "))
    y=float(input("Dame la base menor de tu trapecio: "))
    z=float(input("Dame la altura de tu trapecio: "))
    alt=ArTrap(y,x,z)
    per=PerTrap(y,x,z)
    print("El area de tu trapecio es: ",round(alt,2))
    print("El perimetro es igual a: ",round(per,2))
main()

