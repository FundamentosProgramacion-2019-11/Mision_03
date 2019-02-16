#Autor: María Fernanda García Gastélum A01376181
#Calcular el pago de un trabajador

def calcularPagoNormal(horasNormales, pagoPorHora):
    pagoNormal= horasNormales * pagoPorHora
    return pagoNormal

def calcularPagoExtra(pagoPorHora, horasExtra):
    pagoExtra= horasExtra * (pagoPorHora * 1.65)
    return pagoExtra

def main():
    horasNormales= int(input("Teclea las horas normales trabajadas: "))
    horasExtra= int(input("Teclea las horas extra trabajadas: "))
    pagoPorHora= int(input("Teclea el pago por hora: "))
    calcularPagoNormal(horasNormales, pagoPorHora)
    calcularPagoExtra(pagoPorHora, horasExtra)
    pagoTotal = calcularPagoNormal(horasNormales, pagoPorHora) + calcularPagoExtra(pagoPorHora, horasExtra)
    print("\n")
    print("Pago normal: $ %.2f"% (calcularPagoNormal(horasNormales, pagoPorHora)))
    print("Pago extra: $ %.2f"% (calcularPagoExtra(pagoPorHora, horasExtra)))
    print("- - - - - - - - - - - -")
    print("Pago total: $ %.2f" % (pagoTotal))

main()
