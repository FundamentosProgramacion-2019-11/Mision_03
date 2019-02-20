# Autor: Luis Renteria
# Funciones para colcular los boletos de un concierto


def calcularPago(boletosA, boletosB, boletosC):
    totalpago =(boletosA*3250)+(boletosB*1730)+(boletosC*850)
    return totalpago


def main():
    boletosA = int(input("escribe la cantidad de boletos requeridos para la zona A"))
    boletosB = int(input("escribe la cantidad de boletos requeridos para la zona B"))
    boletosC = int(input("escribe la cantidad de boletos requeridos para la zona c"))
    calcularPago(boletosA, boletosB, boletosC)
    print ("El pago total de los boletos es: ", calcularPago(boletosA, boletosB, boletosC))

main()


