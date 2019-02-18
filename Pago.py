# Autor: Ronaldo Estefano Lira Buendia
# Calcular el total de pago de nomina de un trabajador

def calcularPagoNormal(horasN, pagoH):
    pago = horasN * pagoH
    return pago

def calcularPagoExtra(horasE, pagoH):
    x = (horasE * pagoH)*.65
    pago = (horasE * pagoH) + x
    return pago

def main():
    horasN = int(input("Teclea las horas normales trabajadas: "))
    horasE = int(input("Reclea las horas extras trabajadas: "))
    pagoH = int(input("Teclea el pago por hora: "))
    pagoN = calcularPagoNormal(horasN, pagoH)
    print("Pago normal: ${0:.2f}".format(pagoN))
    pagoE = calcularPagoExtra(horasE, pagoH)
    print("Pago extra: ${0:.2f}".format(pagoE))
    total = pagoN + pagoE
    print("Pago total: ${0:.2f}".format(total))


main ()