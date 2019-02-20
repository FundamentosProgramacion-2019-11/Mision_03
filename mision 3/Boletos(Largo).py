#Luis Fernando Duran Castillo
#Calcular el pago de las entradas

def calcularPagoA(boletosA):
    precioA= boletosA * 3250
    return precioA

def calcularPagoB(boletosB):
    precioB = boletosB * 1730
    return precioB

def calcularPagoC(boletosC):
    precioC = boletosC * 850
    return precioC

def totalapagar (boletosA, boletosB, boletosC):
    precioA = calcularPagoA(boletosA)
    precioB = calcularPagoB(boletosB)
    precioC = calcularPagoC(boletosC)
    total= precioA + precioB + precioC
    return total

def imprimirtotaldeboletos (boletosA, boletosB, boletosC):
    total = totalapagar (boletosA, boletosB, boletosC)
    print("el total a pagar es de: ", total)

def main():
    boletosA= int(input("cuantos boletos en la zona A quiere? "))
    boletosB= int(input("cuantos boletos en la zona B quiere? "))
    boletosC= int(input("cuantos boletos en la zona C quiere? "))
    calcularPagoA(boletosA)
    calcularPagoB(boletosB)
    calcularPagoC(boletosC)
    totalapagar(boletosA, boletosB, boletosC)
    imprimirtotaldeboletos(boletosA, boletosB, boletosC)

main()