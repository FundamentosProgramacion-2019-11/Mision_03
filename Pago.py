#Luis Adrian Carmona Villalobos
#A01748395

def CalcularPagoNormal(horasNormales,pagoPorHora):
    pagoNormal = horasNormales*pagoPorHora
    return pagoNormal
def CalcularPagoExtra(horasExtras,pagoPorHora):
    pagoExtra = (horasExtras*pagoPorHora)*16
    return pagoExtra
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por horas: "))
    pagoExtra = CalcularPagoExtra(horasExtras, pagoPorHora)
    pagoNormal = CalcularPagoNormal(horasNormales, pagoPorHora)
    print("Pago Normal %.2f"% pagoNormal)
    print("Pago Extra: %.2f"% pagoExtra)
    print("---------------------")
    pagoExtra = CalcularPagoExtra(horasExtras, pagoPorHora)
    pagoNormal = CalcularPagoNormal(horasNormales, pagoPorHora)
    pagoTotal = pagoNormal + pagoExtra
    print("Pago Total: %.2f" % pagoTotal)
main()