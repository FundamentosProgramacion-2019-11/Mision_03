#Autor: Elizabeth Citlalli Zapata Cortes
#Descripción: Calcular e imprime el pago semanal de un trabajador incluyendo las horas extras trabajadas.

def calcularHorasExtra(horasExtras, pagoHora):
    pagoExtra = (pagoHora * 65) / 100
    extras = horasExtras * (pagoHora + pagoExtra)
    return extras

def calcularHorasNormales(horasNormales, pagoHora):
    normales = horasNormales * pagoHora
    return normales

def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    pagoTotal = calcularHorasNormales(horasNormales, pagoHora) + calcularHorasExtra(horasExtras, pagoHora)
    print()
    print("Pago normal: $%.2f" % calcularHorasNormales(horasNormales, pagoHora))
    print ("Pago extra: $%.2f" % calcularHorasExtra(horasExtras, pagoHora))
    print("-----------------------")
    print("Pago total: $%.2f" % pagoTotal)

main()