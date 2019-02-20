#Autor: Diego Raul Elizalde Uriarte
#Calcular el total a pagar de boletos


def calcularPago(boletosA,boletosB,boletosC):
    boletosA = boletosA*3250
    boletosB = boletosB*1730
    boletosC = boletosC*850
    totalPago = boletosA+boletosB+boletosC
    return totalPago



def main():
    boletosA = int(input("Numero de boletos en zona A: "))
    boletosB = int(input("Numero de boletos en zona B: "))
    boletosC = int(input("Numero de boletos en zona C: "))
    calcularPago(boletosA,boletosB,boletosC)
    print("El costo total es: $%.2f" % (calcularPago(boletosA,boletosB,boletosC)))



main()