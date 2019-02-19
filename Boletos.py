# Autor: Marianela Contreras D.
# Programa para calcular el total de pago de los boletos de un concierto.


#función para calcular el pago total de los boletos.
def calcularPago(boletosA, boletosB, boletosC):
    totalPago= (boletosA * 3250) + (boletosB * 1730) + (boletosC * 850)
    return totalPago

#función principal del programa y la que se correrá. Las lecturas e impresiones se hacen en esta función.
def main ():
    boletosA = int(input("Número de boletos en zona A:"))
    boletosB = int(input("Número de boletos en zona B:"))
    boletosC = int(input("Número de boletos en zona C:"))
    calcularPago(boletosA, boletosB, boletosC)
    totalPago = calcularPago(boletosA, boletosB, boletosC)
    print("El costo total es: $%.2f" % totalPago)

main ()
