# Autor: Paulina Guerrero Ruiz
# Calcular el pago de un trabajador




def calcularPagoNormal(horasNormales,pagoPorHora):
    PagoNormal = horasNormales * pagoPorHora
    return PagoNormal

def calcularPagoExtra (pagoPorHora, horasExtras):
    PagoExtra = ((pagoPorHora * 1.65)* horasExtras)
    return PagoExtra

def imprimirTotal (PagoNormal, PagoExtra):
    Total = PagoNormal + PagoExtra
    print "El total es: ", "$" ,Total


def main():
    horasNormales = int(input("Teclea horas normales trabajadas: "))
    horasExtras =int(input("Teclea horas extras trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))
    PagoNormal = calcularPagoNormal(horasNormales, pagoPorHora)
    PagoExtra = calcularPagoExtra(pagoPorHora, horasExtras)
    print ("Pago normal: ", "$", PagoNormal)
    print ("Pago extra: ", "$", PagoExtra)
    imprimirTotal(PagoNormal, PagoExtra)



main()