#Autor: Cecilia Daniela Olivares Hernández, a01745727
#Descripción: Calcula el pago semanal de un trabajador más sus horas extras y muestra su pago total.

#Esta funcion calcula el pago de las horas normales
def calcularPagoNormal(horasNormales, horasExtras, pagoHora):
    pagoNormal = horasNormales * pagoHora
    return pagoNormal

#Esta funcion calcula el pago de las horas extras
def calcularPagoExtra(horasNormales, horasExtras, pagoHora):
    pagoExtra = (horasExtras * pagoHora) + ((pagoHora * .65)* horasExtras)
    return pagoExtra

#Funcion principal que resuelve el problema
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal(horasNormales, horasExtras, pagoHora)
    pagoExtra = calcularPagoExtra(horasNormales, horasExtras, pagoHora)
    pagoTotal = pagoNormal + pagoExtra
    print("""
Pago normal: \x1b[1;30m $%.2f""" % (pagoNormal))
    print("\x1b[0;mPago extra: \x1b[1;30m $%.2f" % (pagoExtra))
    print("-----------------------")
    print("\x1b[0;mPago total: \x1b[1;30m $%.2f" % (pagoTotal))

main()