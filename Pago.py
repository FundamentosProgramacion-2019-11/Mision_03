#Maria Angelica Hernandez Parada
#Calcular el pago de un trabajador

def calcularPagoNormal(horasNormales,pagoHora):
    pagoNormal = horasNormales * pagoHora
    return pagoNormal

def imprimirPagoNormal(horasNormales,pagoHora):
    pagoNormal = calcularPagoNormal(horasNormales,pagoHora)
    print("Pago normal: $ %.2f" % (pagoNormal))

def calcularPagoExtra(horasExtras):
    pagoExtra = horasExtras * 82.5
    return pagoExtra

def imprimirPagoExtra(horasExtras):
    pagoExtra = calcularPagoExtra(horasExtras)
    print("Pago extra: $ %.2f" % (pagoExtra))

def calcularPagoTotal(horasNormales,horasExtras,pagoHora):
    pagoNormal = calcularPagoNormal(horasNormales,pagoHora)
    pagoExtra = calcularPagoExtra(horasExtras)
    pagoTotal = pagoNormal + pagoExtra
    return pagoTotal

def imprimirPagoTotal(horasNormales,horasExtras,pagoHora):
    pagoTotal = calcularPagoTotal(horasNormales,horasExtras,pagoHora)
    print("Pago total: $ %.2f" % (pagoTotal))

def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    #pagoHoraExtra= 82.5
    calcularPagoNormal(horasNormales,pagoHora)
    calcularPagoExtra(horasExtras)
    calcularPagoTotal(horasNormales,horasExtras,pagoHora)
    imprimirPagoNormal(horasNormales,pagoHora)
    imprimirPagoExtra(horasExtras)
    imprimirPagoTotal(horasNormales,horasExtras,pagoHora)

main()