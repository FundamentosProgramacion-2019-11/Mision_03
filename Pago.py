# Autor: Juan Carlos Flores García A01376511. Grupo 02.
# Programa que calcula el pago de un trabajador.

# Función que calcula el pago normal.
def calcularPagoNormal(horasNormales, pagoPorHora):
    totalNormal = horasNormales * pagoPorHora
    return totalNormal

# Función que calcula el pago extra.
def calcularPagoExtra(horasExtras, pagoPorHora):
    extra = (pagoPorHora * 0.65) + pagoPorHora
    totalExtra = horasExtras * extra
    return totalExtra

# Función que calcula el pago total.
def calcularPagoTotal(pagoNormal, pagoExtra):
    total = pagoNormal + pagoExtra
    return total

# Función principal.
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal(horasNormales, pagoPorHora)
    pagoExtra = calcularPagoExtra(horasExtras, pagoPorHora)
    pagoTotal = calcularPagoTotal(pagoNormal, pagoExtra)

    print("Pago normal: $%.2f" % (pagoNormal))
    print("Pago extra: $%.2f" % (pagoExtra))
    print("-----------------------")
    print("Pago total: $%.2f" % (pagoTotal))

# Llamada a la función principal.
main()

