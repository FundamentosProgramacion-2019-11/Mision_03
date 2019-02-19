#Autor: Yasmín Landaverde Nava
#Descripción: este programa calcula el cosoto toal de los boletos para un concierto.


def calcularPago(boletosA, boletosB, boletosC):
    costoA = boletosA * 3250
    costoB = boletosB * 1730
    costoC = boletosC * 850
    totalPago = costoA + costoB + costoC
    return totalPago

def imprimirPago(boletosA, boletosB, boletosC):
    totalPago = calcularPago(boletosA, boletosB, boletosC)
    print("El costo total es: $", totalPago )


def main():
    boletosA = int(input("¿Cuántos bolestos en sección A quieres?: "))
    boletosB = int(input("¿Cuántos bolestos en sección B quieres?: "))
    boletosC = int(input("¿Cuántos bolestos en sección C quieres?: "))
    calcularPago(boletosA, boletosB, boletosC)
    imprimirPago(boletosA, boletosB, boletosC)

main()