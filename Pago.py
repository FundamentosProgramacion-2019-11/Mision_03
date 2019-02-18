# Roberto Emmanuel González Muñoz A01376803
# Escribe un programa que lea las horas normales, las horas extras
# y el pago por hora de un trabajador. Calcula
# e imprime los datos de pago semanal.


def calcularPagoNormal(hrsN,pagoXhora):
    pagoTotal = hrsN * pagoXhora
    return pagoTotal


def calcularPagoExtra(hrsE, pagoXhora):
    pagoXhoraExtra = pagoXhora + (65*pagoXhora/100)
    pagoTotal = hrsE * pagoXhoraExtra
    return pagoTotal


def main():
    # Pregunta los datos al usuario.
    horasNormales = int(input("Teclea las horas nomrales trabajadas: "))
    horasExtra = int(input("Teclea las horas extra trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))

    # Calcula el pago Normal.
    pagoNormal = calcularPagoNormal(horasNormales,pagoPorHora)

    # Calcula el pago Extra.
    pagoExtra = calcularPagoExtra(horasExtra,pagoPorHora)

    # Calcula el pago Total.
    pagoTotal = pagoNormal + pagoExtra

    # Imprime los resultados.
    print("_______________________________")
    print("Pago normal %.2f" % pagoNormal)
    print("Pago Extra: %.2f" % pagoExtra)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print("Pago Total: %.2f " % pagoTotal)


main()