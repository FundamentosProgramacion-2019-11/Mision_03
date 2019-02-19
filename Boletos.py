#Sofía Trujillo Vargas
#En este problema se hara un sistema de pagos para comprar boletos

def calcularPago(boletosA,boletosB,boletosC):
    a=boletosA*3250
    b=boletosB*1730
    c=boletosC*850
    totalPago = a+b+c
    return totalPago
def main():
    aa=int(input("¿Cuantos boletos quieres de la zona A: "))
    bb=int(input("¿Cuantos boletos quieres de la zona B: "))
    cc=int(input("¿Cuantos boletos quieres de la zona C: "))
    x=calcularPago(aa,bb,cc)
    print("Este es el total de tu compra: ",round(x,2))
main()