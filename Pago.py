# Roberto Castro Barrios A01748559
# Descripción: Programa que calcula el pago semanal de un trabajador.

#Esta funcion calcula el pago total sumando el extra y el normal
def total(totalPagoN, totalPagoE) :
    total = totalPagoN + totalPagoE
    return total

#Esta funcion calcula el pago extra
def calcularPagoExtra(hExtras, pago) :
    total = hExtras * (pago * 1.65)
    return total

#Esta funcion calcula el pago normal
def calcularPagoNormal(hNormales, pago) :
    total = hNormales * pago
    return total

#Esta es la funcion principal; encargada de leer, imprimir y recibir las funciones.
def main () :
    hNormales = int(input("Teclea las horas normales trabajadas: "))
    hExtras = int(input("Teclea las horas extras trabajadas: "))
    pago = int(input("Teclea el pago por hora: "))
    calcularPagoNormal(hNormales, pago)
    calcularPagoExtra(hExtras, pago)
    totalPagoN = calcularPagoNormal(hNormales, pago)
    totalPagoE = calcularPagoExtra(hExtras, pago)
    total(totalPagoN, totalPagoE)
    totalPago = total(totalPagoN, totalPagoE)
    print("Pago normal: $ %.2f" %(totalPagoN))
    print("Pago extra: $ %.2f" %(totalPagoE))
    print("Pago total: $ %.2f"%(totalPago))

#Llama a la función -main-
main()
