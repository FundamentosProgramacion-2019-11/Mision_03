#Autor: Katia Hernández Barrera
#Descripción: programa que calcula el pago total de unos boletos


def calcularPago (numeroBoletosA, numeroBoletosB, numeroBoletosC):
    boletosA = 3250
    boletosB = 1730
    boletosC = 850
    totalPago = (boletosA * numeroBoletosA) + (boletosB * numeroBoletosB) + (boletosC* numeroBoletosC)
    return totalPago


def main():
    numeroBoletosA = int(input("Número de boletos en zona A: "))
    numeroBoletosB = int(input("Número de boletos en zona B: "))
    numeroBoletosC = int(input("Número de boletos en zona C: "))
    calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $%.2f"%totalPago)

main()
