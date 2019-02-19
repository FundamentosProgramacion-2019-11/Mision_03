#Autor: Michel Antoine Dionne Gutierrez A0174863, Grupo: 03
#Este programa calculara el total a pagar de todos los boletos en cada zona

#Esta funcion calcula el total a pagar de las horas normales de la jornada semanal
def calcularPagoNormal(horasNormales,pagoPorHora):
    pagoTotalNormal = horasNormales*pagoPorHora
    return pagoTotalNormal

#Esta funcion calcula el total a pagar de las horas extra de la jornada semanal
def calcularPagoExtra(horasExtra,pagoPorHora):
    pagoTotalExtra = (horasExtra*pagoPorHora)*.65+(horasExtra*pagoPorHora)
    return pagoTotalExtra

def main():
    horasNormales = int(input("Teclea las horas normales trabajadas"))
    horasExtra = int(input("Teclea las horas extras"))
    pagoPorHora = int(input("Teclea el pago pr hora"))
    pagoNormal=calcularPagoNormal(horasNormales,pagoPorHora)
    pagoExtra=calcularPagoExtra(horasExtra,pagoPorHora)
    pagoFinalSemanal = calcularPagoNormal(pagoPorHora,horasNormales)+calcularPagoExtra(horasExtra,pagoPorHora)
    print("El pago de las horas normales es de %.2f"%pagoNormal)
    print("El pago de las horas extra es de %.2f" % pagoExtra)
    print("El pago de todas las horas de la semana es de %.2f" % pagoFinalSemanal)

main()