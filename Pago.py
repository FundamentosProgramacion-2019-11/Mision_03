#Autor: Luis Alberto Zepeda Hernandez, A01328616.
#Descripcion: Escribe un programa que lea las horas normales, las horas extras y el pago por hora de un trabajador.
# Calcula e imprime los datos de pago semanal. Formatea correctamente las cantidades.

#Se encarga de realizar la operación para calcular el pago total, llamando a otras dos funciones. Regresa el resultado
def calculaPagoTotal(horasExtras, horasNormales, pagoHora):
    pagoTotal = calculaPagoExtra(horasExtras,pagoHora) + calculaPagoNormal(horasNormales,pagoHora)
    return pagoTotal

#Se encarga de calcular el pago de horas extras, y regresa el resultado
def calculaPagoExtra(horasExtra,pagoHora):
    pagoExtra = (65 * pagoHora) / 100
    pagoExtra = horasExtra * (pagoHora + pagoExtra)
    return pagoExtra

#Se encarga de calcular el pago por las horas de trabajo normal, con los datos pedidos en la función main, y regresa el resultado.
def calculaPagoNormal(horasNormales, pagoHoras):
    pagoNormal = horasNormales * pagoHoras
    return pagoNormal

#Se encarga de pedir la información al usuario, llamar a las funciones para realizar la operaciones y obtener los resultados e imprimirlos.
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    print()

    pagoNormal = calculaPagoNormal(horasNormales, pagoHora)
    pagoExtra = calculaPagoExtra(horasExtras, pagoHora)
    pagoTotal = calculaPagoTotal(horasExtras, horasNormales, pagoHora)

    print("Pago normal: " "$" "{0:.2f}".format(pagoNormal))
    print("Pago extra: " "$" "{0:.2f}".format(pagoExtra))
    print("--------------------------------")
    print("Pago total: " "$" "{0:.2f}".format(pagoTotal))


main()
