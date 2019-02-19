# Autor: Itzel Yanabany Castro Becerril
# Calcuar el pago total de un trabajador con sus horas normales y extras
def calcularPagoNormal(horasNormales, horasExtras, pagoHora):
    pagoNormal = pagoHora * horasNormales
    return pagoNormal


def imprimirPagoNormal(horasNormales, horasExtras, pagoHora):
    pagoNormal = calcularPagoNormal(horasNormales, horasExtras, pagoHora)
    print("Pago Normal: %.2f" % (pagoNormal))


def calcularHorasExtras(horasNormales, horasExtras, pagoHora):
    pagoExtra = pagoHora * horasExtras * 1.65
    return pagoExtra


def imprimirPagoExtra(horasNormales, horasExtras, pagoHora):
    pagoExtra = calcularHorasExtras(horasNormales, horasExtras, pagoHora)
    print("Pago Extra: %.2f" % (pagoExtra))


def calcularPagoTotal(horasNormales, horasExtras, pagoHora):
    total = calcularPagoNormal(horasNormales, horasExtras, pagoHora) + calcularHorasExtras(horasNormales, horasExtras,
                                                                                           pagoHora)
    return total


def imprimirPagoTotal(horasNormales, horasExtras, pagoHora):
    total = calcularPagoTotal(horasNormales, horasExtras, pagoHora)
    print("Pago Total: %.2f" % (total))


def main():
    horasNormales = int(input("Teclea las horas normales trabajada: "))
    horasExtras = int(input("Teclea la horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    imprimirPagoNormal(horasNormales, horasExtras, pagoHora)
    imprimirPagoExtra(horasNormales, horasExtras, pagoHora)
    imprimirPagoTotal(horasNormales, horasExtras, pagoHora)


main()

