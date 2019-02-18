#Autor: Cecilia Daniela Olivares Hernández, a01745727
#Descripción: Calcula el precio total a pagar de los boletos comprados para un concierto.

#Esta funcion calcula el precio de cada uno de los boletos y calcula el pago total
def calcularPago(boletosA, boletosB, boletosC):
    pagoA = boletosA * 3250.00
    pagoB = boletosB * 1730.00
    pagoC = boletosC * 850.00
    totalPago = pagoA + pagoB + pagoC
    return totalPago

#Funcion principal que resuelve el problema
def main():
    boletosA = int(input("Número de boletos en zona A: "))
    boletosB = int(input("Número de boletos en zona B: "))
    boletosC = int(input("Número de boletos en zona C: "))
    totalPago = calcularPago(boletosA, boletosB, boletosC)
    print("El costo total es: " + "\x1b[1;30m" + "$%.2f" % (totalPago))

main()
