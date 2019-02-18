#Autor: Ivana Olvera Mérida A01746744
#Escribir un programa que pregunte al usuario cuántos boletos quiere comprar para cada zona y que imprima el pago total

def calcularPago (boletosA, boletosB, boletosC):
    costoBoletosA = boletosA * 3250
    costoBoletosB = boletosB * 1730
    costoBoletosC = boletosC * 850
    pagoTotal = (costoBoletosA + costoBoletosB + costoBoletosC)
    return pagoTotal

def main ():
    numBoletosA = int(input("Número de boletos en Zona A: "))
    numBoletosB = int(input("Número de boletos en Zona B: "))
    numBoletosC = int(input("Número de boletos en Zona C: "))
    pagoTotal = calcularPago(numBoletosA, numBoletosB, numBoletosC)
    print("El costo total es: $%.2f" % (pagoTotal))

main()



