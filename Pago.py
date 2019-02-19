#Autor: Marianela Contereras D.
# Programa para calcular el pago semanal de un trabajador.

#función para calcular el pago normal del usuario.
def calcularPagoNormal(horasExtra,horasNormales,pagoHora):
    pagoNormal= horasNormales * pagoHora
    return pagoNormal

#función para calcular el pago extra del usuario.
def calcularPagoExtra(horasExtra,horasNormales,pagoHora):
    pagoNormal= calcularPagoNormal(horasExtra,horasNormales,pagoHora)
    pagoExtra= ((pagoHora*.65)+ pagoHora)*horasExtra
    return pagoExtra

#función para calcular el pago total del usuario, tomando en cuenta el pago normal y el pago extra.
def calcularTotal(horasExtra, horasNormales,pagoHora):
    pagoNormal = calcularPagoNormal(horasExtra,horasNormales,pagoHora)
    pagoExtra = calcularPagoExtra(horasExtra,horasNormales,pagoHora)
    total= pagoNormal + pagoExtra
    return total


##Función principal del programa y la que correrá. Las lecturas e impresiones se hacen en esta función.
def main():
    horasNormales = float(input("Teclea las horas normales trabajadas:"))
    horasExtra = float(input("Teclea las horas extras trabajadas:"))
    pagoHora = float (input("Teclea el pago por hora:"))
    calcularPagoNormal(horasExtra, horasNormales,pagoHora)
    calcularPagoExtra(horasExtra,horasNormales,pagoHora)
    calcularTotal(horasExtra,horasNormales,pagoHora)
    pagoNormal = calcularPagoNormal(horasExtra, horasNormales, pagoHora)
    pagoExtra = calcularPagoExtra(horasExtra, horasNormales, pagoHora)
    total = calcularTotal(horasExtra, horasNormales, pagoHora)
    print("\nPago normal: $%.2f" % pagoNormal)
    print("Pago extra: $%.2f" % pagoExtra)
    print("----------------------------------")
    print("Pago total: $%.2f" % total)



main()
