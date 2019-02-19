#Autor: Yasmín Landaverde Nava
#Descripción: este programa calcula el pago de un trabajador

HORA_EXTRA = .65

def calcularPagoNormal(horasNormales, pagoHora):
    normal = horasNormales * pagoHora
    return normal

def imprimirPagoNormal(horasNormales, pagoHora):
    normal = calcularPagoNormal(horasNormales, pagoHora)
    print ("Pago normal: $ ",  "%.2f" % normal)

def calcularPagoExtra(horasExtra):
    extra = horasExtra * HORA_EXTRA
    return extra

def imprimirExtra(horasExtra):
    extra = calcularPagoExtra(horasExtra)
    print("Pago extra: $ ",  "%.2f" % extra)


def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    calcularPagoNormal(horasNormales, pagoHora)
    imprimirPagoNormal(horasNormales, pagoHora)
    calcularPagoExtra(horasExtra)
    imprimirExtra(horasExtra)
    print ("---------------------")
    totalPago = calcularPagoNormal(horasNormales, pagoHora) +  calcularPagoExtra(horasExtra)
    print ("El pago total es de: $" ,  "%.2f" % totalPago)


main()