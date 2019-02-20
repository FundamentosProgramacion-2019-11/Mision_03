# Autor: Rosalía Serrano Herrera
# Calcula el pago de un trabajador dependiendo las horas normales y horas extra de trabajo

def calcularNormal(horasNormales, pago):
    pagoNormal = horasNormales * pago
    return pagoNormal

def calcularExtra(horasExtras, pago):
    extra = (horasExtras * pago) * .65
    pagoExtra = extra + (horasExtras * pago)
    return pagoExtra

def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pago = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularNormal(horasNormales, pago)
    pagoExtra = calcularExtra(horasExtras, pago)
    pagoTotal = pagoNormal + pagoExtra
    print("\n" "Pago normal: $%.2f" % (pagoNormal))
    print("Pago extra: $%.2f" % (pagoExtra))
    print("--------------------")
    print("Pago total: $%.2f" % (pagoTotal))

main()