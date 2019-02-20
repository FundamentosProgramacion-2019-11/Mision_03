#Autor: Diego Raul Elizalde Uriarte
#Calcular horas normales, horas extras y el pago por hora de un trabajador


def calcularPagoExtra(horasExtra,pagoPorHora):
    pagoExtra = (horasExtra*(pagoPorHora+(pagoPorHora*.65)))
    return pagoExtra






def calcularPagoNormal(horasNormales,pagoPorHora):
    pagoNormal = horasNormales*pagoPorHora
    return pagoNormal





def calcularTotal(horasExtra,horasNormales,pagoPorHora):
    total = calcularPagoExtra(horasExtra,pagoPorHora)+calcularPagoNormal(horasNormales,pagoPorHora)
    return total





def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))
    calcularPagoNormal(horasNormales,pagoPorHora)
    print("Pago normal: %.2f" % (calcularPagoNormal(horasNormales,pagoPorHora)))
    calcularPagoExtra(horasExtra,pagoPorHora)
    print("Pago extra: %.2f" % (calcularPagoExtra(horasExtra,pagoPorHora)))
    print("-----------------------")
    calcularTotal(horasExtra,horasNormales,pagoPorHora)
    print("Pago total: %.2f " % (calcularTotal(horasExtra,horasNormales,pagoPorHora)))







main()