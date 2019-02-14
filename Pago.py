#Autor: Mariana Teyssier Cervantes
#Calcular el pago de un trabajador por horas normales y horas extras.

#calcular el pago normal semanal sin horas extras.
def calcularPagoNormal(horasNormales, horasExtras, pagoHora):
    pago = horasNormales * pagoHora
    return pago

#imprimir el pago normal con dos decimales.
def ImprimirPagoNormal(horasNormales, horasExtras, pagoHora):
    pago = calcularPagoNormal(horasNormales, horasExtras, pagoHora)
    print("\nPago normal: $%.2f" % (pago))

#calcular el pago extra por el numero de horas extras trabajadas.
def calcularPagoExtra(horasNormales, horasExtras, pagoHora):
    extra = ((pagoHora*.65)+pagoHora)*horasExtras
    return extra

#imprimir el pago extra con dos decimales.
def ImprimirPagoExtra(horasNormales, horasExtras, pagoHora):
    extra = calcularPagoExtra(horasNormales, horasExtras, pagoHora)
    print("Pago extra: $%.2f" % (extra))

#calcular el pago total de la suma del pago normal y el pago extra.
def calcularPagoTotal (horasNormales, horasExtras, pagoHora):
    extra = ((pagoHora*.65)+pagoHora)*horasExtras
    pago = horasNormales * pagoHora
    total = extra + pago
    return total

#imprimir el pago total con dos decimales.
def ImprimirPagoTotal(horasNormales, horasExtras, pagoHora):
    total = calcularPagoTotal(horasNormales, horasExtras, pagoHora)
    print("\nPago total: $%.2f" % (total))

#preguntar al usuario cuantas horas trabajo normales, cuantas extras y cuanto se paga por hora.
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    ImprimirPagoNormal(horasNormales, horasExtras, pagoHora)
    ImprimirPagoExtra(horasNormales, horasExtras, pagoHora)
    ImprimirPagoTotal(horasNormales, horasExtras, pagoHora)

#Llamar la funcion -main-
main()