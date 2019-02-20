#Luis Fernando Duran Castillo
#Calcular el pago de las entradas

def CalcularPago(boletosA, boletosB, boletosC):
    precioA = boletosA * 3250
    precioB = boletosB * 1730
    precioC = boletosC * 850
    total= precioA + precioB + precioC
    return total


def imprimirtotaldeboletos (boletosA, boletosB, boletosC):
    total = CalcularPago(boletosA, boletosB, boletosC)
    print("el total a pagar es de: ", total)

def main():
    boletosA= int(input("cuantos boletos en la zona A quiere? "))
    boletosB= int(input("cuantos boletos en la zona B quiere? "))
    boletosC= int(input("cuantos boletos en la zona C quiere? "))
    CalcularPago(boletosA, boletosB, boletosC)
    imprimirtotaldeboletos(boletosA, boletosB, boletosC)

main()