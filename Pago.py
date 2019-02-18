# Autor: YadiraFuentesCalderón, A01745235
# Descripcion: Calcular el pago normal, extra y total a un trabajador.

def calcularPagoNormal(horasNormales, pagoPorHora):
    pagoHorasNormales= horasNormales*pagoPorHora
    return pagoHorasNormales

def calcularPagoExtra (horasExtras, pagoPorHora):
    pagoHorasExtra= horasExtras*(pagoPorHora*1.65)
    return pagoHorasExtra

def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))

    pagoHorasNormales= calcularPagoNormal(horasNormales, pagoPorHora)
    pagoHorasExtra= calcularPagoExtra(horasExtras, pagoPorHora)

    pagoTotal= pagoHorasNormales+pagoHorasExtra

    print ("Pago normal: $%.2f"% (pagoHorasNormales))
    print("Pago extra: $%.2f"% (pagoHorasExtra))
    print("-----------------------")
    print ("Total pago: $%.2f"% (pagoTotal))
main()