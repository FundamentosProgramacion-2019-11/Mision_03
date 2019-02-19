# Autor: Itzel Yanabany Castro Becerril
# Calcular el pago total de la compra de los boletos

def calcularPago(boletosA, boletosB, boletosC):
    ZonaA = boletosA * 3250
    ZonaB = boletosB * 1730
    ZonaC = boletosC * 850
    total = ZonaA + ZonaB + ZonaC
    return total


def imprimirResultado(boletosA, boletosB, boletosC):
    total = calcularPago(boletosA, boletosB, boletosC)
    print("El costo total ee: ", total)


def main():
    boletosA = int(input("Numero de boletos en zona A: "))
    boletosB = int(input("Numero de boletos en zona B: "))
    boletosC = int(input("Numero de Boletos en zona C: "))
    imprimirResultado(boletosA, boletosB, boletosC)


main()
