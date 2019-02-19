# Autor: Jose Luis Mata Lomeli
# Objetivo: Crear un programa que lea los horas normales, horas extras y el pago por hora de un trabajador


def pagoNormal(horas, pago):
    pagoNormal = horas * pago #Pago tradicional (sin pago extra)
    return pagoNormal

def pagoExtra(horas, pago):
    pagoExtra = horas * pago #Horas extra por el pago por hora
    bonus = pagoExtra * 0.65  #Las horas extra se pagan 65% mas que las normales
    Extra = pagoExtra + bonus
    return Extra #Regresar el pago extra


# Funcion Principal:
def main():

    # Datos dados por el usuario
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))

    # Llamamos a las funciones
    pagoN = pagoNormal(horasNormales,pagoHora)
    pagoExt = pagoExtra(horasExtras, pagoHora)

    # Imprimir los resultados de las funciones
    print("pago normal: $%.2f" %(pagoN))
    print("pago extra: $%.2f" %(pagoExt))

    # Calcular total
    pagoTotal = pagoN + pagoExt
    print("----------------")
    print("pago total: $%.2f" %(pagoTotal)) #Imprimir pago total

main()
