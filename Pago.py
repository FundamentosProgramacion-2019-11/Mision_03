# Autor: Luis Renteria
# Calcular pago de un trabajador con funciones


def calcularPagoNormal(horasNormalesTrabajadas, pagoPorHoras):
    PagoNormal=(horasNormalesTrabajadas*pagoPorHoras)
    return PagoNormal


def calcularHorasExtras(horasExtrasTrabajadas, pagoPorHoras):
    PagoHorasEextra=(horasExtrasTrabajadas*1.65)
    return PagoHorasEextra


def main():
    horasNormalesTrabajadas=int(input("Pon tus horas trabajadas:"))
    pagoPorHoras=int(input("teclea el pago por horas trabajadas"))
    horasExtrasTrabajadas=int(input("Teclea las horas extras trabajadas"))
    calcularPagoNormal(horasNormalesTrabajadas, pagoPorHoras)
    calcularHorasExtras(horasExtrasTrabajadas, pagoPorHoras)
    PagoTotal=(calcularPagoNormal(horasNormalesTrabajadas, pagoPorHoras))+(calcularHorasExtras(horasExtrasTrabajadas, pagoPorHoras))
    print("El pago total es",PagoTotal)

main()
