#Autor: Michel Antoine Dionne Gutierrez A0174863, Grupo: 03
#Este programa calculara el total a pagar de todos los boletos en cada zona

#Calcula el total a pagar de todos los boletos
def calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC):
    totalPago = (numeroBoletosA*3250)+(numeroBoletosB*1730)+(numeroBoletosC*850)
    return totalPago

def imprimirPago(numeroBoletosA,numeroBoletosB,numeroBoletosC):
    pagoFinal = calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)
    print("El pago total es de",pagoFinal," pesos")

def main():
    numeroBoletosA = int(input("Cuantos boletos de la zona A desea comprar ?"))
    numeroBoletosB = int(input("Cuantos boletos de la zona B desea comprar ?"))
    numeroBoletosC = int(input("Cuantos boletos de la zona C desea comprar ?"))
    calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)
    imprimirPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)

main()