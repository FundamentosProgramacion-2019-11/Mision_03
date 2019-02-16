#Maria Angelica Hernandez Parada
#Costo de boletos para concierto dependiendo la zona y la cantidad


def calcularPago (numeroBoletosA, numeroBoletosB, numeroBoletosC):
    totalPago= ((numeroBoletosA*3250)+(numeroBoletosB*1730)+(numeroBoletosC*850))
    return totalPago

def imprimirTotalPago (numeroBoletosA, numeroBoletosB, numeroBoletosC):
    totalPago =  calcularPago (numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $ %.2f" % (totalPago))

def main():
    numeroBoletosA = int(input("Número de boletos en zona A: "))
    numeroBoletosB = int(input("Número de boletos en zona B: "))
    numeroBoletosC = int(input("Número de boletos en zona C: "))
    calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    imprimirTotalPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)

main()
